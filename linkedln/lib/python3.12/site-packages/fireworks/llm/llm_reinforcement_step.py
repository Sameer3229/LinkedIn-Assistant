from typing import Literal, Optional

from fireworks._literals import AcceleratorTypeLiteral, ReinforcementAcceleratorTypeLiteral
from fireworks._util import generate_model_resource_name
from fireworks.control_plane.generated.protos_grpcio.gateway.status_pb2 import JobState
from fireworks.dataset.dataset import Dataset
from fireworks.gateway import Gateway
from fireworks.llm.llm import LLM
from fireworks.control_plane.generated.protos_grpcio.gateway.deployment_pb2 import (
    AcceleratorType as SyncAcceleratorType,
)
from fireworks.control_plane.generated.protos_grpcio.gateway.rlor_trainer_job_pb2 import (
    RlorTrainerJob as RlorTrainerJobProto,
    CreateRlorTrainerJobRequest as CreateRlorTrainerJobRequestProto,
)
from fireworks.control_plane.generated.protos_grpcio.gateway.training_pb2 import (
    BaseTrainingConfig as BaseTrainingConfigProto,
)


class LLMReinforcementStep:
    """
    Class that provides reinforcement learning step functionality.
    This uses composition instead of inheritance for cleaner separation.
    """

    def __init__(self, llm: LLM):
        """
        Initialize with an LLM instance.

        Args:
            llm: The LLM instance to work with
        """
        self.llm = llm

    def reinforcement_step(
        self,
        dataset: Dataset,
        output_model: str,
        lora_rank: int = 16,
        learning_rate: float = 0.0001,
        max_context_length: int = 8192,
        epochs: int = 1,
        batch_size: int = 32768,
        accelerator_count: int = 1,
        accelerator_type: ReinforcementAcceleratorTypeLiteral = "NVIDIA_H200_141GB",
    ) -> "ReinforcementStep":
        """
        Perform a reinforcement learning step with the given dataset.

        Args:
            dataset: The dataset to use for the reinforcement learning step

        Returns:
            Dict containing the step results and any additional information
        """
        # check if the model already exists
        account_id = self.llm._gateway.account_id()
        model = self.llm._gateway.get_model_sync(generate_model_resource_name(account_id, output_model))
        if model is not None:
            raise ValueError(f"Model {output_model} already exists")

        training_config = BaseTrainingConfigProto()
        training_config.output_model = f"accounts/{self.llm._gateway.account_id()}/models/{output_model}"
        if self.llm.is_peft_addon():
            training_config.warm_start_from = self.llm.model
        else:
            training_config.base_model = self.llm.model
        training_config.lora_rank = lora_rank
        training_config.learning_rate = learning_rate
        training_config.max_context_length = max_context_length
        training_config.epochs = epochs
        training_config.batch_size = batch_size
        training_config.accelerator_type = getattr(SyncAcceleratorType, accelerator_type)
        training_config.accelerator_count = accelerator_count
        rlor_trainer_job = RlorTrainerJobProto(
            training_config=training_config,
            dataset=dataset.name,
        )
        create_rlor_trainer_job_request = CreateRlorTrainerJobRequestProto(
            rlor_trainer_job=rlor_trainer_job,
        )
        job = self.llm._gateway.create_rlor_trainer_job_sync(create_rlor_trainer_job_request)
        return ReinforcementStep(job, self.llm._gateway)


class ReinforcementStep:
    """
    Class that represents a RLOR trainer job.
    This is a wrapper around the RlorTrainerJobProto class.
    """

    def __init__(self, job: RlorTrainerJobProto, gateway: Gateway):
        self.job = job
        self.gateway = gateway

    def get(self) -> Optional["ReinforcementStep"]:
        job = self.gateway.get_rlor_trainer_job_sync(self.job.name)
        if job is None:
            return None
        return ReinforcementStep(job, self.gateway)

    @property
    def state(self) -> str:
        return JobState.Name(self.job.state)

    @property
    def output_model(self):
        return self.job.training_config.output_model

    @property
    def is_completed(self):
        return self.job.state == JobState.JOB_STATE_COMPLETED

    def raise_if_bad_state(self):
        """
        Raises a RuntimeError if the job is in a failed, cancelled, or otherwise bad state.
        """
        bad_states = {
            JobState.JOB_STATE_FAILED,
            JobState.JOB_STATE_FAILED_CLEANING_UP,
            JobState.JOB_STATE_CANCELLED,
            JobState.JOB_STATE_EXPIRED,
            JobState.JOB_STATE_EXPIRED_CLEANING_UP,
            JobState.JOB_STATE_DELETING_CLEANING_UP,
        }
        if self.state in bad_states:
            raise RuntimeError(f"RLORTrainerJob is in a bad state: {self.state}. Message: {self.job.status.message}")
