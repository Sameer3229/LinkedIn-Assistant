import asyncio
from copy import deepcopy
import time
from typing import Optional, Union, TYPE_CHECKING
from fireworks._const import FIREWORKS_API_BASE_URL
from fireworks._util import generate_time_str
from fireworks.gateway import Gateway
from fireworks.dataset import Dataset
from fireworks.control_plane.generated.protos.gateway import (
    JobState,
)
from fireworks.control_plane.generated.protos_grpcio.gateway.supervised_fine_tuning_job_pb2 import (
    ListSupervisedFineTuningJobsRequest as SyncListSupervisedFineTuningJobsRequest,
    CreateSupervisedFineTuningJobRequest as SyncCreateSupervisedFineTuningJobRequest,
    SupervisedFineTuningJob as SyncSupervisedFineTuningJob,
)
from fireworks.control_plane.generated.protos_grpcio.gateway.status_pb2 import (
    JobState as SyncJobState,
)
from fireworks._logger import logger

# Type checking imports to avoid circular imports
if TYPE_CHECKING:
    from fireworks.llm.llm import LLM


class SupervisedFineTuningJob:
    """
    Wrapper around proto for a supervised fine-tuning job in Fireworks. Can be
    constructed from a name, LLM, and dataset. Can be used to sync the job state
    to Fireworks and query the current state.
    """

    def __init__(
        self,
        llm: "LLM",
        proto: SyncSupervisedFineTuningJob,
        dataset_or_id: Union[Dataset, str],
        evaluation_dataset_or_id: Optional[Union[Dataset, str]] = None,
        api_key: Optional[str] = None,
    ):
        """
        Args:
            llm: The LLM object that created this job.
            proto: The proto object that represents the fine-tuning job.
            dataset_or_id: The dataset or dataset ID to use for the fine-tuning job.
            evaluation_dataset: The evaluation dataset or dataset ID to use for the fine-tuning job.
            api_key: The API key to use for the fine-tuning job.
        """
        self.llm = llm
        self.dataset_or_id = dataset_or_id
        self.evaluation_dataset_or_id = evaluation_dataset_or_id
        self._api_key = api_key
        self._gateway = Gateway(api_key=api_key)
        self._proto = proto

    @property
    def output_model(self) -> Optional[str]:
        if self._proto is None:
            return None
        if self._proto.output_model is None:
            return None
        if self._proto.output_model.startswith("accounts/"):
            return self._proto.output_model
        return f"accounts/{self._gateway.account_id()}/models/{self._proto.output_model}"

    @classmethod
    async def adelete_by_name(cls, name: str, api_key: Optional[str] = None):
        gateway = Gateway(api_key=api_key)
        await gateway.delete_supervised_fine_tuning_job(name)
        job = await gateway.get_supervised_fine_tuning_job(name)
        while job is not None:
            await asyncio.sleep(1)

    @classmethod
    def delete_by_name(cls, name: str, api_key: Optional[str] = None):
        gateway = Gateway(api_key=api_key)
        gateway.delete_supervised_fine_tuning_job_sync(name)
        job = gateway.get_supervised_fine_tuning_job_sync(name)
        while job is not None:
            time.sleep(1)

    def delete(self):
        if self._proto is None:
            raise ValueError("Call sync() before deleting")
        self.delete_by_name(self._proto.name, self._api_key)

    async def adelete(self):
        if self._proto is None:
            raise ValueError("Call sync() before deleting")
        await self.adelete_by_name(self._proto.name, self._api_key)

    def sync(self) -> "SupervisedFineTuningJob":
        """
        Creates the job if it doesn't exist, otherwise returns the existing job.
        If previous job failed, deletes it and creates a new one.
        """
        # Make sure the datasets are synced before creating the job
        if isinstance(self.dataset_or_id, Dataset):
            self.dataset_or_id.sync()
        if isinstance(self.evaluation_dataset_or_id, Dataset):
            self.evaluation_dataset_or_id.sync()

        existing_job = self.get()
        if existing_job is not None:
            if (
                existing_job._proto.state == JobState.FAILED
                or existing_job._proto.state == JobState.FAILED_CLEANING_UP
                or existing_job._proto.state == JobState.CANCELLED
                or existing_job._proto.state == JobState.DELETING
                or existing_job._proto.state == JobState.DELETING_CLEANING_UP
                or existing_job._proto.state == JobState.UNSPECIFIED
            ):
                self.delete()
            else:
                return existing_job
        request = self._create_request()
        self._gateway.create_supervised_fine_tuning_job_sync(request)
        new_job = self.get()
        if new_job is None:
            raise ValueError(f"Failed to create supervised fine-tuning job {self.display_name}")
        return new_job

    @property
    def id(self) -> str:
        if self._proto is None:
            raise ValueError("Call sync() before accessing id")
        return self._proto.name.split("/")[-1]

    @property
    def display_name(self) -> str:
        if self._proto is None:
            raise ValueError("Call sync() before accessing display_name")
        return self._proto.display_name

    @property
    def name(self) -> str:
        if self._proto is None:
            raise ValueError("Call sync() before accessing name")
        return self._proto.name

    @property
    def url(self) -> str:
        base_url = "dev.fireworks.ai" if "dev." in FIREWORKS_API_BASE_URL else "app.fireworks.ai"
        if self.id is None:
            return f"https://{base_url}/dashboard/fine-tuning"
        return f"https://{base_url}/dashboard/fine-tuning/supervised/{self.id}"

    def _create_request(self) -> SyncCreateSupervisedFineTuningJobRequest:
        
        # Gateway doesn't allow you to have the name field set, so we need to remove it
        # before sending the request. But self.id should be equal to the id in the name field
        # so everything should match up with the current state of self.name
        proto = deepcopy(self._proto)
        proto.name = ""

        request = SyncCreateSupervisedFineTuningJobRequest(
            supervised_fine_tuning_job=proto,
            supervised_fine_tuning_job_id=self.id,
        )
        return request

    @property
    def output_llm(self) -> "LLM":
        # Import here to avoid circular import
        from fireworks.llm.llm import LLM

        if self.output_model is None:
            raise ValueError(f'Fine-tuning job "{self.display_name}" did not create an output model')
        if self.llm.addons_enabled:
            return LLM(model=self.output_model, deployment_type="on-demand-lora", base_id=self.llm.deployment_id)
        return LLM(model=self.output_model, deployment_type=self.llm.deployment_type, base_id=self.llm.deployment_id)

    def wait_for_completion(self) -> "SupervisedFineTuningJob":
        """
        Synchronously poll for job completion.
        """
        while self._proto.state != JobState.COMPLETED:
            if self._proto.state == JobState.FAILED:
                raise ValueError(f'Fine-tuning job "{self.display_name}" failed')
            if self._proto.create_time is not None:
                curr_time = time.time()
                create_time = self._proto.create_time.seconds + self._proto.create_time.nanos / 1e9
                delta_seconds = int(curr_time - create_time)
                minutes = delta_seconds // 60
                seconds = delta_seconds % 60
                logger.debug(
                    f'Fine-tuning job "{self.display_name}" is in state {SyncJobState.Name(self._proto.state)}. Job was created {generate_time_str(minutes, seconds)} ago.'
                )
            time.sleep(5)
            updated_job = self.get()
            if updated_job is None:
                raise ValueError(f'Fine-tuning job "{self.display_name}" not found')
            self = updated_job
        return self

    async def await_for_completion(self) -> "SupervisedFineTuningJob":
        """
        Asynchronously poll for job completion.
        """
        while self._proto.state != JobState.COMPLETED:
            if self._proto.state == JobState.FAILED:
                raise ValueError(f'Fine-tuning job "{self.display_name}" failed')
            if self._proto.create_time is not None:
                curr_time = time.time()
                create_time = self._proto.create_time.seconds + self._proto.create_time.nanos / 1e9
                delta_seconds = int(curr_time - create_time)
                minutes = delta_seconds // 60
                seconds = delta_seconds % 60
                logger.debug(
                    f'Fine-tuning job "{self.display_name}" is in state {SyncJobState.Name(self._proto.state)}. Job was created {generate_time_str(minutes, seconds)} ago.'
                )
            await asyncio.sleep(5)
            updated_job = self.get()
            if updated_job is None:
                raise ValueError(f'Fine-tuning job "{self.display_name}" not found')
            self = updated_job
        return self

    def get(self) -> Optional["SupervisedFineTuningJob"]:
        job = self._gateway.get_supervised_fine_tuning_job_sync(self.name)
        if job is None:
            return None
        return SupervisedFineTuningJob(
            llm=self.llm,
            proto=job,
            dataset_or_id=self.dataset_or_id,
            api_key=self._api_key,
        )