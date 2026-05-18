import asyncio
import time
from typing import Optional, Union, TYPE_CHECKING
from fireworks._const import FIREWORKS_API_BASE_URL
from fireworks._util import generate_time_str
from fireworks.gateway import Gateway
from fireworks.dataset import Dataset
from fireworks.control_plane.generated.protos.gateway import (
    JobState,
)
from fireworks.control_plane.generated.protos_grpcio.gateway.reinforcement_fine_tuning_job_pb2 import (
    ListReinforcementFineTuningJobsRequest as SyncListReinforcementFineTuningJobsRequest,
    CreateReinforcementFineTuningJobRequest as SyncCreateReinforcementFineTuningJobRequest,
    ReinforcementFineTuningJob as SyncReinforcementFineTuningJob,
)
from fireworks.control_plane.generated.protos_grpcio.gateway.status_pb2 import (
    JobState as SyncJobState,
)
from fireworks._logger import logger

# Type checking imports to avoid circular imports
if TYPE_CHECKING:
    from fireworks.llm.llm import LLM


class ReinforcementFineTuningJob:
    """
    Wrapper around proto for a reinforcement fine-tuning job in Fireworks. Can be
    constructed from a name, LLM, and dataset. Can be used to sync the job state
    to Fireworks and query the current state.
    """

    def __init__(
        self,
        llm: "LLM",
        proto: SyncReinforcementFineTuningJob,
        dataset_or_id: Union[Dataset, str],
        id: Optional[str],
        evaluation_dataset_or_id: Optional[Union[Dataset, str]] = None,
        api_key: Optional[str] = None,
        gateway: Optional[Gateway] = None,
    ):
        """
        Args:
            llm: The LLM object that created this job.
            proto: The proto object that represents the fine-tuning job.
            dataset_or_id: The dataset or dataset ID to use for the fine-tuning job.
            evaluation_dataset_or_id: The dataset or dataset ID to use for the evaluation dataset.
            api_key: The API key to use for the fine-tuning job.
            gateway: If you want to reuse caches saved on a Gateway instance
        """
        self.llm = llm
        self._id = id
        self.dataset_or_id = dataset_or_id if isinstance(dataset_or_id, Dataset) else dataset_or_id
        self.evaluation_dataset_or_id = (
            evaluation_dataset_or_id if isinstance(evaluation_dataset_or_id, Dataset) else evaluation_dataset_or_id
        )
        self._api_key = api_key
        if gateway:
            self._gateway = gateway
        else:
            self._gateway = Gateway(api_key=api_key)
        self._proto = proto

    @classmethod
    async def adelete_by_id(cls, id: str, api_key: Optional[str] = None):
        gateway = Gateway(api_key=api_key)
        gateway.delete_reinforcement_fine_tuning_job_sync(id)
        # Wait for deletion to complete
        while True:
            job = gateway.get_reinforcement_fine_tuning_job_sync(id)
            if job is None:
                break
            await asyncio.sleep(1)

    @classmethod
    def delete_by_id(cls, id: str, api_key: Optional[str] = None):
        gateway = Gateway(api_key=api_key)
        gateway.delete_reinforcement_fine_tuning_job_sync(id)
        # Wait for deletion to complete
        while True:
            job = gateway.get_reinforcement_fine_tuning_job_sync(id)
            if job is None:
                break
            time.sleep(1)

    def delete(self):
        if self._proto is None:
            raise ValueError("Call sync() before deleting")
        self.delete_by_id(self.id, self._api_key)

    async def adelete(self):
        if self._proto is None:
            raise ValueError("Call sync() before deleting")
        await self.adelete_by_id(self.id, self._api_key)

    def sync(self) -> "ReinforcementFineTuningJob":
        """
        Creates the job if it doesn't exist, otherwise returns the existing job.
        If previous job failed, deletes it and creates a new one.
        """
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
        job_proto = self._gateway.create_reinforcement_fine_tuning_job_sync(request)
        self._proto = job_proto

        new_job = self.get()
        if new_job is None:
            raise ValueError(f"Failed to create reinforcement fine-tuning job {self.display_name}")
        return new_job

    @property
    def id(self) -> str:
        if self._id is not None:
            return self._id
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
        if not self.id:
            return f"https://{FIREWORKS_API_BASE_URL}/dashboard/fine-tuning"
        base_url = "dev.fireworks.ai" if "dev." in FIREWORKS_API_BASE_URL else "app.fireworks.ai"
        return f"https://{base_url}/dashboard/fine-tuning/reinforcement/{self.id}"

    def _create_request(self) -> SyncCreateReinforcementFineTuningJobRequest:
        request = SyncCreateReinforcementFineTuningJobRequest(
            reinforcement_fine_tuning_job=self._proto,
            reinforcement_fine_tuning_job_id=self.id,
        )
        return request

    def wait_for_completion(self) -> "ReinforcementFineTuningJob":
        """
        Synchronously poll for job completion.
        """
        while self._proto.state != JobState.COMPLETED:
            if self._proto.state == JobState.FAILED:
                raise ValueError(f'Reinforcement fine-tuning job "{self.display_name}" failed')
            if self._proto.create_time is not None:
                curr_time = time.time()
                create_time = self._proto.create_time.seconds + self._proto.create_time.nanos / 1e9
                delta_seconds = int(curr_time - create_time)
                minutes = delta_seconds // 60
                seconds = delta_seconds % 60
                logger.debug(
                    f'Reinforcement fine-tuning job "{self.display_name}" is in state {SyncJobState.Name(self._proto.state)}. Job was created {generate_time_str(minutes, seconds)} ago.'
                )
            time.sleep(5)
            updated_job = self.get()
            if updated_job is None:
                raise ValueError(f'Reinforcement fine-tuning job "{self.display_name}" not found')
            self = updated_job
        return self

    async def await_for_completion(self) -> "ReinforcementFineTuningJob":
        """
        Asynchronously poll for job completion.
        """
        while self._proto.state != JobState.COMPLETED:
            if self._proto.state == JobState.FAILED:
                raise ValueError(f'Reinforcement fine-tuning job "{self.display_name}" failed')
            if self._proto.create_time is not None:
                curr_time = time.time()
                create_time = self._proto.create_time.seconds + self._proto.create_time.nanos / 1e9
                delta_seconds = int(curr_time - create_time)
                minutes = delta_seconds // 60
                seconds = delta_seconds % 60
                logger.debug(
                    f'Reinforcement fine-tuning job "{self.display_name}" is in state {SyncJobState.Name(self._proto.state)}. Job was created {generate_time_str(minutes, seconds)} ago.'
                )
            await asyncio.sleep(5)
            updated_job = self.get()
            if updated_job is None:
                raise ValueError(f'Reinforcement fine-tuning job "{self.display_name}" not found')
            self = updated_job
        return self

    @property
    def output_llm(self) -> "LLM":
        # Import here to avoid circular import
        from fireworks.llm.llm import LLM

        if self._proto.training_config.output_model is None:
            raise ValueError(f'Fine-tuning job "{self.display_name}" did not create an output model')
        if self.llm.addons_enabled:
            return LLM(model=self._proto.training_config.output_model, deployment_type="on-demand-lora")
        return LLM(model=self._proto.training_config.output_model, deployment_type=self.llm.deployment_type)

    def get(self) -> Optional["ReinforcementFineTuningJob"]:
        """
        Get the reinforcement fine-tuning job by ID using the direct get method,
        unlike supervised fine-tuning which uses a list and filter approach.
        """
        if not self.id:
            return None
        job_proto = self._gateway.get_reinforcement_fine_tuning_job_sync(self.id)
        if job_proto is None:
            return None
        return ReinforcementFineTuningJob(
            llm=self.llm,
            proto=job_proto,
            dataset_or_id=self.dataset_or_id,
            evaluation_dataset_or_id=self.evaluation_dataset_or_id,
            id=self.id,
            api_key=self._api_key,
            gateway=self._gateway,
        )
