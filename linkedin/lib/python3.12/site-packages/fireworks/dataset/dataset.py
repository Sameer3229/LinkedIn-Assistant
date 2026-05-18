from datetime import datetime
import io
import json
import logging
import os
from functools import cache as sync_cache
from fireworks._util import (
    make_valid_resource_name,
)
from fireworks.evaluation_job.evaluation_job import EvaluationJob
from fireworks.evaluator.evaluator import Evaluator
import httpx
import atexit
from typing import List, Literal, Optional, Union, BinaryIO, Callable, overload
from fireworks.control_plane.generated.protos.gateway import (
    CreateDatasetRequest,
    ListDatasetsRequest,
    Dataset as DatasetProto,
)
from fireworks.control_plane.generated.protos_grpcio.gateway.dataset_pb2 import (
    Dataset as SyncDataset,
    ListDatasetsRequest as SyncListDatasetsRequest,
    CreateDatasetRequest as SyncCreateDatasetRequest,
)
from fireworks.control_plane.generated.protos_grpcio.gateway.evaluation_job_pb2 import (
    CreateEvaluationJobRequest as SyncCreateEvaluationJobRequest,
    GetEvaluationJobRequest as SyncGetEvaluationJobRequest,
    EvaluationJob as SyncEvaluationJob,
)

import mmh3

from fireworks.gateway import Gateway

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.propagate = False  # Prevent duplicate logs

if os.environ.get("FIREWORKS_SDK_DEBUG"):
    logger.setLevel(logging.DEBUG)


class Dataset:
    def __init__(
        self,
        api_key: Optional[str] = None,
        path: Optional[str] = None,
        data: Optional[Union[str, list]] = None,
        id: Optional[str] = None,
        _internal=False,
    ):
        """
        A "smart" Dataset class that helps developers upload datasets and
        fine-tune on Fireworks. It has the following features:

        1. Works nicely with the `fireworks.llm.LLM` class.
        2. Automatically names dataset based on the contents of the dataset and the filename of the file if provided.
        3. Automatically uploads dataset to Fireworks if it doesn't already exist.

        To instantiate a Dataset, use the `from_*` class methods:
        - `from_dict(data: list)`
        - `from_file(path: str)`
        - `from_string(data: str)`
        - `from_id(id: str)`

        Args:
            path: Path to the local directory containing the dataset.
            data: Data to be uploaded to the dataset. Can be a string in JSONL format with OpenAI chat completion
                  message compatible JSON, or a list of OpenAI chat completion message compatible objects.
            id: The ID of an existing dataset on Fireworks.
        TODO: support various remote paths to cloud storage.
        """
        if not _internal:
            raise ValueError(
                "Dataset is not meant to be instantiated directly, use Dataset.from_dict() or Dataset.from_file() instead"
            )
        self._data: Optional[str] = None
        self._path: Optional[str] = None
        self._id: Optional[str] = id
        self._gateway = Gateway(api_key=api_key)
        self._file_stream: Optional[BinaryIO] = None
        atexit.register(self._gateway.close)

        # Ensure exactly one of path, data, or id is provided
        provided_params = [path is not None, data is not None, id is not None]
        if sum(provided_params) == 0:
            raise ValueError("Must provide exactly one of: path, data, or id")
        if sum(provided_params) > 1:
            raise ValueError("Must provide exactly one of: path, data, or id (cannot provide multiple)")

        if path and not path.endswith(".jsonl"):
            raise ValueError("File must be a JSONL file")

        if path:
            self._path = path
        elif isinstance(data, list):
            # Convert list to newline delimited JSON string
            self._data = "\n".join(json.dumps(item) for item in data)
        elif isinstance(data, str):
            self._data = data
        elif id:
            self._id = id

    @classmethod
    def from_string(cls, data: str):
        return cls(data=data, _internal=True)

    @classmethod
    def from_list(cls, data: list):
        """
        Create a dataset from a list of dictionaries.

        Args:
            data: List of dictionaries to be converted to a JSONL string where each dictionary is a line in the jsonl file.

        Returns:
            Dataset: A new Dataset object.
        """
        return cls(data=data, _internal=True)

    @classmethod
    def from_id(cls, id: str):
        return cls(id=id, _internal=True)

    @classmethod
    def from_file(cls, path: str):
        if not path.endswith(".jsonl"):
            raise ValueError("File must be a JSONL file")
        return cls(path=path, _internal=True)

    def get(self) -> Optional[SyncDataset]:
        """
        Get this dataset from Fireworks by hash
        - If filename of dataset changes, it still matches the hash
        """
        request = SyncListDatasetsRequest()
        datasets: List[SyncDataset] = []
        datasets_response = self._gateway.list_datasets_sync(request)
        datasets.extend(datasets_response.datasets)
        while datasets_response.next_page_token:
            request.page_token = datasets_response.next_page_token
            datasets_response = self._gateway.list_datasets_sync(request)
            datasets.extend(datasets_response.datasets)
        for dataset in datasets:
            if dataset.name.endswith(self.id):
                logger.debug(f"Found dataset with matching hash: {dataset.name}")
                return dataset
        logger.debug(f"No dataset found with matching hash: {hash(self)}")
        return None

    @property
    def url(self) -> str:
        return f"https://app.fireworks.ai/dashboard/datasets/{self.id}"

    def sync(self):
        """
        Upload this dataset to Fireworks if it doesn't already exist.
        """
        # check if dataset exists by hash
        dataset = self.get()
        if dataset:
            logger.debug(f"Dataset already exists: {dataset.name}, no need to upload")
            return
        logger.debug(f"No dataset found with matching hash: {hash(self)}, creating new dataset")
        dataset = SyncDataset(
            format=self._detect_dataset_format(),
            example_count=min(self._line_count(), 50_000_000),
        )
        # upload dataset since it doesn't exist
        logger.debug(f"Creating dataset: {self.id}")
        request = SyncCreateDatasetRequest(dataset=dataset, dataset_id=self.id)
        dataset = self._gateway.create_dataset_sync(request)
        logger.debug(f"Dataset created: {dataset.name}")
        logger.debug(f"Uploading dataset: {self.id}")
        filename_to_size = {self.filename(): self.file_size()}
        signed_urls = self._gateway.get_dataset_upload_endpoint_sync(self.id, filename_to_size)
        self._upload_file_using_signed_url(signed_urls[self.filename()])
        logger.debug(f"Dataset uploaded: {self.id}")
        self._gateway.validate_dataset_sync(self.id)
        logger.debug(f"Dataset validated: {self.id}")

    def _upload_file_using_signed_url(self, signed_url: str) -> None:
        """
        Upload a file to a signed URL using async streaming to avoid loading the entire file into memory.

        Args:
            signed_url: The signed URL to upload the file to.
        """
        logger.debug(f"Uploading file to signed URL: {signed_url}")

        file = self._get_stream()
        try:
            # Get file size for content length
            file.seek(0, os.SEEK_END)
            size = file.tell()
            file.seek(0)

            # Prepare the HTTP request
            headers = {
                "Content-Type": "application/octet-stream",
                "X-Goog-Content-Length-Range": f"{size},{size}",
            }

            # Upload the file with streaming
            with httpx.Client() as client:
                response = client.put(signed_url, content=file, headers=headers)
                if response.status_code != 200:
                    raise RuntimeError(f"Failed to upload file: {response.status_code} - {response.text}")

            logger.debug("File upload completed successfully")
        finally:
            file.close()

    def filename(self) -> str:
        """
        Returns the filename of the dataset if path is provided, otherwise returns "inmemory"
        to indicate this dataset was created from an in-memory data structure rather than a file.
        """
        if self._path:
            return os.path.basename(self._path)
        return "inmemory.jsonl"

    @property
    def id(self):
        """
        Generates an id for this dataset in the form of "dataset-{hash(self)}-{filename}"
        For datasets created from an existing ID, extracts the name from the ID.
        If the ID includes the prefix "accounts/<account>/datasets/", it is removed from the output.
        """
        if self._id:
            # Remove "accounts/<account>/datasets/" prefix if present
            # Pattern: accounts/{account_id}/datasets/{dataset_id}
            if self._id.startswith("accounts/") and "/datasets/" in self._id:
                parts = self._id.split("/")
                if len(parts) >= 4 and parts[0] == "accounts" and parts[2] == "datasets":
                    # Extract the part after "/datasets/"
                    return self._id.split("/datasets/", 1)[1]
            return self._id
        return f"dataset-{hash(self)}-{make_valid_resource_name(self.filename())}"

    @property
    @sync_cache
    def name(self):
        return self.construct_name(self._gateway.account_id(), self.id)

    @classmethod
    def construct_name(cls, account_id: str, id: str):
        if id.startswith("accounts/"):
            raise ValueError(f"ID cannot start with 'accounts/': {id}")
        return f"accounts/{account_id}/datasets/{id}"

    @property
    def stream(self) -> BinaryIO:
        """
        Returns a cached file-like object for the dataset content.
        For backward compatibility - prefer using get_stream() with a context manager.
        """
        if self._file_stream is not None and not self._file_stream.closed:
            self._file_stream.seek(0)
            return self._file_stream

        self._file_stream = self._get_stream()
        return self._file_stream

    def _line_count(self) -> int:
        """
        Returns the number of lines in the dataset
        """
        with self._get_stream() as stream:
            count = 0
            for _ in stream:
                count += 1
            return count

    def _detect_dataset_format(self) -> SyncDataset.Format:
        """
        Detects the format of the dataset by examining its content.

        Returns:
            A string representing the dataset format:
            - "CHAT" for chat completion format
            - "COMPLETION" for completion format
            - "FORMAT_UNSPECIFIED" if the format cannot be determined
        """

        try:
            with self._get_stream() as file:
                for line in file:
                    try:
                        data = json.loads(line.decode("utf-8"))

                        # Check for completion format (prompt + completion)
                        if "prompt" in data and "completion" in data:
                            return SyncDataset.Format.COMPLETION

                        # Check for chat format (messages array)
                        if "messages" in data and isinstance(data["messages"], list) and len(data["messages"]) > 0:
                            return SyncDataset.Format.CHAT

                        # If we reach here, the format doesn't match either completion or chat
                        return SyncDataset.Format.FORMAT_UNSPECIFIED
                    except json.JSONDecodeError:
                        return SyncDataset.Format.FORMAT_UNSPECIFIED

                # If we've read the entire file without determining a format, it's unspecified
                return SyncDataset.Format.FORMAT_UNSPECIFIED
        except Exception as e:
            logger.error(f"Error detecting dataset format: {e}")
            return SyncDataset.Format.FORMAT_UNSPECIFIED

    def _get_stream(self) -> BinaryIO:
        """
        Returns a fresh file-like object for the dataset content.
        For in-memory data, returns a BytesIO object.
        For file paths, returns a file object.
        This is intended to be used with a context manager to ensure proper cleanup.
        """
        if self._data:
            return io.BytesIO(self._data.encode("utf-8"))
        elif self._path:
            return open(self._path, "rb")
        elif self._id:
            # Validate account access if the ID contains an account prefix
            if self._id.startswith("accounts/") and "/datasets/" in self._id:
                parts = self._id.split("/")
                if len(parts) >= 4 and parts[0] == "accounts" and parts[2] == "datasets":
                    account_id = parts[1]
                    api_key_account_id = self._gateway.account_id()

                    # Check if the account ID in the dataset path matches the API key's account
                    if account_id != api_key_account_id:
                        raise ValueError(
                            f"Dataset belongs to account '{account_id}' but API key is for account '{api_key_account_id}'. "
                            f"Please use the correct API key for the dataset's account."
                        )

            response = self._gateway.get_dataset_download_endpoint_sync(self.id)
            if not response:
                raise ValueError(f'Dataset with id "{self._id}" does not exist')
            signed_url = next(iter(response.filename_to_signed_urls.values()))
            # download file to in-memory bytesio
            with httpx.Client() as client:
                response = client.get(signed_url)
                return io.BytesIO(response.content)
        else:
            raise ValueError("No data or path provided")

    def __iter__(self):
        """
        Make the dataset iterable, yielding parsed JSON objects from each line.

        Yields:
            dict: Parsed JSON object from each line in the dataset

        Example:
            for record in dataset:
                print(record)  # Each record is a parsed JSON dict
        """
        stream = self.stream  # Use the cached stream property
        stream.seek(0)  # Ensure we start from the beginning
        for line in stream:
            line_str = line.decode("utf-8").strip()
            if line_str:  # Skip empty lines
                try:
                    yield json.loads(line_str)
                except json.JSONDecodeError as e:
                    logger.warning(f"Failed to parse JSON line: {line_str[:100]}... Error: {e}")
                    continue

    def file_size(self) -> int:
        """
        Returns the size of the dataset in bytes without reading the entire file
        """
        # Use optimized path for files since we can get size without reading
        if self._path:
            return os.path.getsize(self._path)

        # For in-memory data, get the size from the stream
        with self._get_stream() as stream:
            stream.seek(0, io.SEEK_END)
            size = stream.tell()
            return size

    def __hash__(self) -> int:
        """
        Computes a hash of the dataset contents
        """
        # Read the entire file content for hashing
        content = self.read()
        # Ensure the hash is positive by using the unsigned value (& with MAXINT)
        return mmh3.hash(content) & 0x7FFFFFFF

    def delete(self):
        """
        Delete this dataset from Fireworks
        """
        # if dataset doesn't exist, don't delete
        dataset = self.get()
        if not dataset:
            logger.debug(f"Dataset does not exist: {self.id}, no need to delete")
            return
        self._gateway.delete_dataset_sync(self.id)

    def read(self, size: Optional[int] = None) -> bytes:
        """
        Read content from the dataset

        Args:
            size: Number of bytes to read, or None to read the entire file
                 (use cautiously with large files)

        Returns:
            The content as bytes
        """
        with self._get_stream() as stream:
            if size is not None:
                return stream.read(size)
            return stream.read()

    def preview_evaluator(self, reward_function: Callable, samples: Optional[int] = None):
        """
        Preview the evaluator for the dataset
        """
        if samples:
            new_dataset = self.head(samples, as_dataset=True)
            return new_dataset.preview_evaluator(reward_function)

        evaluator = Evaluator(gateway=self._gateway, reward_function=reward_function)
        evaluator.sync()
        return evaluator.preview(self)

    def create_evaluation_job(self, reward_function: Callable, samples: Optional[int] = None) -> EvaluationJob:
        """
        Create an evaluation job using a reward function for this dataset

        Args:
            reward_function: A callable decorated with @reward_function
            samples: Optional number of samples to evaluate (creates a subset dataset)

        Returns:
            EvaluationJob: The created evaluation job
        """
        # if samples is provided, create a new dataset with only those samples
        # and create an evaluation job on that dataset
        if samples:
            new_dataset = self.head(samples, as_dataset=True)
            return new_dataset.create_evaluation_job(reward_function)

        self.sync()

        # Create and sync the evaluator
        evaluator = Evaluator(gateway=self._gateway, reward_function=reward_function)
        evaluator.sync()

        # Create the evaluation job
        output_dataset_id = datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")
        evaluation_job_proto = SyncEvaluationJob(
            evaluator=evaluator.name,
            input_dataset=self.name,
            output_dataset=self.construct_name(self._gateway.account_id(), output_dataset_id),
            display_name=output_dataset_id,
        )

        # create evaluation job with evaluator
        evaluation_job = EvaluationJob(
            gateway=self._gateway,
            evaluation_job=evaluation_job_proto,
        )
        evaluation_job.sync()
        return evaluation_job

    @overload
    def head(self, n: int = 5, as_dataset: Literal[False] = False) -> list: ...

    @overload
    def head(self, n: int = 5, as_dataset: Literal[True] = True) -> "Dataset": ...

    def head(self, n: int = 5, as_dataset: bool = False) -> Union[list, "Dataset"]:
        """
        Return the first n rows of the dataset.

        Args:
            n: Number of rows to return (default: 5)
            as_dataset: If True, return a Dataset object; if False, return a list (default: False)

        Returns:
            list or Dataset: List of dictionaries if as_dataset=False, Dataset object if as_dataset=True

        Example:
            dataset = Dataset.from_file("data.jsonl")
            first_5_rows = dataset.head(5)  # Returns list
            first_5_dataset = dataset.head(5, as_dataset=True)  # Returns Dataset
        """
        rows = []
        for i, row in enumerate(self):
            if i >= n:
                break
            rows.append(row)

        if as_dataset:
            return Dataset.from_list(rows)
        return rows

    def __getitem__(self, key):
        """
        Support slice notation and indexing for the dataset.

        Args:
            key: Either a slice object (e.g., [:5], [2:10], [::2]) or an integer index

        Returns:
            list: For slices, returns a list of dictionaries representing the sliced rows
            dict: For single index, returns a single dictionary representing that row

        Examples:
            dataset[:5]    # Returns first 5 rows (calls head(5))
            dataset[2:7]   # Returns rows 2-6
            dataset[10]    # Returns the 10th row (0-indexed)
        """
        if isinstance(key, slice):
            start = key.start or 0
            stop = key.stop
            step = key.step or 1

            if start == 0 and step == 1 and stop is not None:
                # Simple case: [:n] - can use head method for efficiency
                return self.head(stop)
            else:
                # More complex slicing - need to iterate through dataset
                rows = []
                for i, row in enumerate(self):
                    if stop is not None and i >= stop:
                        break
                    if i >= start and (step == 1 or (i - start) % step == 0):
                        rows.append(row)
                return rows
        else:
            # Handle single index access
            if key < 0:
                raise IndexError("Negative indexing not supported for Dataset")
            for i, row in enumerate(self):
                if i == key:
                    return row
            raise IndexError(f"Index {key} out of range")

    def __eq__(self, other):
        """
        Check if two datasets are equal.

        Args:
            other: The other dataset to compare with.

        Returns:
            bool: True if the datasets are equal, False otherwise
        """
        if not isinstance(other, Dataset):
            return False
        return self.id == other.id and self.file_size() == other.file_size()
