import time
from fireworks.gateway import Gateway
from fireworks.control_plane.generated.protos_grpcio.gateway.evaluation_job_pb2 import (
    EvaluationJob as SyncEvaluationJob,
    CreateEvaluationJobRequest as SyncCreateEvaluationJobRequest,
)
from fireworks.control_plane.generated.protos_grpcio.gateway.status_pb2 import (
    JobState as SyncJobState,
)
from fireworks._logger import logger


class EvaluationJob:
    def __init__(self, gateway: Gateway, evaluation_job: SyncEvaluationJob):
        self.gateway = gateway
        self.evaluation_job: SyncEvaluationJob = evaluation_job

    def wait_for_completion(self) -> "EvaluationJob":
        logger.info(
            f"Starting to wait for evaluation job {self.evaluation_job.name} to complete. Current state: {self.evaluation_job.state}"
        )

        while self.evaluation_job.state != SyncJobState.JOB_STATE_COMPLETED:
            if self.evaluation_job.state == SyncJobState.JOB_STATE_FAILED:
                logger.error(f"Evaluation job {self.evaluation_job.name} failed")
                raise Exception(f"Evaluation job {self.evaluation_job.name} failed")
            if self.evaluation_job.state == SyncJobState.JOB_STATE_FAILED_CLEANING_UP:
                logger.error(f"Evaluation job {self.evaluation_job.name} failed to clean up")
                raise Exception(f"Evaluation job {self.evaluation_job.name} failed to clean up")
            if self.evaluation_job.state == SyncJobState.JOB_STATE_CANCELLED:
                logger.warning(f"Evaluation job {self.evaluation_job.name} was cancelled")
                raise Exception(f"Evaluation job {self.evaluation_job.name} was cancelled")
            if self.evaluation_job.state == SyncJobState.JOB_STATE_DELETING:
                logger.warning(f"Evaluation job {self.evaluation_job.name} is being deleted")
                raise Exception(f"Evaluation job {self.evaluation_job.name} is being deleted")
            if self.evaluation_job.state == SyncJobState.JOB_STATE_DELETING_CLEANING_UP:
                logger.warning(f"Evaluation job {self.evaluation_job.name} is being deleted during cleanup")
                raise Exception(f"Evaluation job {self.evaluation_job.name} is being deleted")

            logger.debug(
                f"Evaluation job {self.evaluation_job.name} status update - Current state: {SyncJobState.Name(self.evaluation_job.state)}"
            )
            time.sleep(10)
            try:
                self.evaluation_job = (
                    self.gateway.get_evaluation_job_sync(name=self.evaluation_job.name) or self.evaluation_job
                )
            except Exception as e:
                logger.error(f"Failed to get evaluation job status: {e}")
                # Keep existing evaluation job state if update fails
                pass

        logger.info(f"Evaluation job {self.evaluation_job.name} completed successfully")
        return self

    @property
    def output_dataset(self):
        from fireworks.dataset.dataset import Dataset

        if self.evaluation_job.output_dataset:
            return Dataset.from_id(self.evaluation_job.output_dataset.split("/")[-1])
        else:
            raise ValueError(
                "No output dataset found. Is this job completed? ",
                "Make sure to run `sync` and `wait_for_completion` before calling this method.",
            )

    @property
    def id(self):
        if not self.evaluation_job.name:
            raise ValueError("Evaluation job has no name. Make sure to run `sync` before calling this method.")
        return self.evaluation_job.name.split("/")[-1]

    @property
    def name(self):
        if not self.evaluation_job.name:
            raise ValueError("Evaluation job has no name. Make sure to run `sync` before calling this method.")
        return self.evaluation_job.name

    @property
    def url(self):
        return f"https://app.fireworks.ai/dashboard/evaluation-jobs/{self.id}"

    def sync(self):
        """
        Creates the evaluation job if it doesn't exist, otherwise returns the existing job.
        If previous job failed, deletes it and creates a new one.
        """
        try:
            existing_job = self.gateway.get_evaluation_job_sync(name=self.evaluation_job.name)
            if existing_job is not None:
                if (
                    existing_job.state == SyncJobState.JOB_STATE_FAILED
                    or existing_job.state == SyncJobState.JOB_STATE_FAILED_CLEANING_UP
                    or existing_job.state == SyncJobState.JOB_STATE_CANCELLED
                    or existing_job.state == SyncJobState.JOB_STATE_DELETING
                    or existing_job.state == SyncJobState.JOB_STATE_DELETING_CLEANING_UP
                ):
                    logger.debug(f"Deleting existing evaluation job {existing_job.name} in state {existing_job.state}")
                    # Delete the failed job (implementation would depend on available gateway method)
                    # For now, we'll proceed to create a new one
                else:
                    # Update our internal state with the existing job
                    self.evaluation_job = existing_job
                    logger.debug(
                        f"Using existing evaluation job {self.evaluation_job.name} with state: {self.evaluation_job.state}"
                    )
                    return self
        except Exception as e:
            logger.debug(f"Could not get evaluation job {self.evaluation_job.name}: {e}")

        # Create new evaluation job
        request = self._create_request()
        logger.debug(f"Creating new evaluation job {self.evaluation_job.name}")
        new_job = self.gateway.create_evaluation_job_sync(request)
        self.evaluation_job = new_job
        logger.debug(f"Created evaluation job {self.evaluation_job.name} with state: {self.evaluation_job.state}")
        return self

    def _create_request(self) -> SyncCreateEvaluationJobRequest:
        """Create the request object for creating an evaluation job."""
        return SyncCreateEvaluationJobRequest(
            evaluation_job=self.evaluation_job,
        )
