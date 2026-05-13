from . import batch_inference_job_pb2 as _batch_inference_job_pb2
from . import job_progress_pb2 as _job_progress_pb2
from . import options_pb2 as _options_pb2
from . import status_pb2 as _status_pb2
from . import training_pb2 as _training_pb2
from . import wandb_pb2 as _wandb_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.api import visibility_pb2 as _visibility_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReinforcementFineTuningJob(_message.Message):
    __slots__ = ("name", "display_name", "create_time", "completed_time", "dataset", "evaluation_dataset", "eval_auto_carveout", "state", "status", "created_by", "training_config", "evaluator", "wandb_config", "output_stats", "job_progress", "inference_parameters", "chunk_size", "output_stats_internal", "output_metrics", "mcp_server", "use_temporal_workflow")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_TIME_FIELD_NUMBER: _ClassVar[int]
    DATASET_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_DATASET_FIELD_NUMBER: _ClassVar[int]
    EVAL_AUTO_CARVEOUT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    TRAINING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_FIELD_NUMBER: _ClassVar[int]
    WANDB_CONFIG_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_STATS_FIELD_NUMBER: _ClassVar[int]
    JOB_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    INFERENCE_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_STATS_INTERNAL_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_METRICS_FIELD_NUMBER: _ClassVar[int]
    MCP_SERVER_FIELD_NUMBER: _ClassVar[int]
    USE_TEMPORAL_WORKFLOW_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    create_time: _timestamp_pb2.Timestamp
    completed_time: _timestamp_pb2.Timestamp
    dataset: str
    evaluation_dataset: str
    eval_auto_carveout: bool
    state: _status_pb2.JobState
    status: _status_pb2.Status
    created_by: str
    training_config: _training_pb2.BaseTrainingConfig
    evaluator: str
    wandb_config: _wandb_pb2.WandbConfig
    output_stats: str
    job_progress: _job_progress_pb2.JobProgress
    inference_parameters: _batch_inference_job_pb2.InferenceParameters
    chunk_size: int
    output_stats_internal: str
    output_metrics: str
    mcp_server: str
    use_temporal_workflow: bool
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., completed_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., dataset: _Optional[str] = ..., evaluation_dataset: _Optional[str] = ..., eval_auto_carveout: bool = ..., state: _Optional[_Union[_status_pb2.JobState, str]] = ..., status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., created_by: _Optional[str] = ..., training_config: _Optional[_Union[_training_pb2.BaseTrainingConfig, _Mapping]] = ..., evaluator: _Optional[str] = ..., wandb_config: _Optional[_Union[_wandb_pb2.WandbConfig, _Mapping]] = ..., output_stats: _Optional[str] = ..., job_progress: _Optional[_Union[_job_progress_pb2.JobProgress, _Mapping]] = ..., inference_parameters: _Optional[_Union[_batch_inference_job_pb2.InferenceParameters, _Mapping]] = ..., chunk_size: _Optional[int] = ..., output_stats_internal: _Optional[str] = ..., output_metrics: _Optional[str] = ..., mcp_server: _Optional[str] = ..., use_temporal_workflow: bool = ...) -> None: ...

class GetReinforcementFineTuningJobRequest(_message.Message):
    __slots__ = ("name", "read_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class CreateReinforcementFineTuningJobRequest(_message.Message):
    __slots__ = ("parent", "reinforcement_fine_tuning_job", "debug", "reinforcement_fine_tuning_job_id", "skip_validations")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REINFORCEMENT_FINE_TUNING_JOB_FIELD_NUMBER: _ClassVar[int]
    DEBUG_FIELD_NUMBER: _ClassVar[int]
    REINFORCEMENT_FINE_TUNING_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    SKIP_VALIDATIONS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    reinforcement_fine_tuning_job: ReinforcementFineTuningJob
    debug: bool
    reinforcement_fine_tuning_job_id: str
    skip_validations: bool
    def __init__(self, parent: _Optional[str] = ..., reinforcement_fine_tuning_job: _Optional[_Union[ReinforcementFineTuningJob, _Mapping]] = ..., debug: bool = ..., reinforcement_fine_tuning_job_id: _Optional[str] = ..., skip_validations: bool = ...) -> None: ...

class ListReinforcementFineTuningJobsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by", "read_mask")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListReinforcementFineTuningJobsResponse(_message.Message):
    __slots__ = ("reinforcement_fine_tuning_jobs", "next_page_token", "total_size")
    REINFORCEMENT_FINE_TUNING_JOBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    reinforcement_fine_tuning_jobs: _containers.RepeatedCompositeFieldContainer[ReinforcementFineTuningJob]
    next_page_token: str
    total_size: int
    def __init__(self, reinforcement_fine_tuning_jobs: _Optional[_Iterable[_Union[ReinforcementFineTuningJob, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class DeleteReinforcementFineTuningJobRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ResumeReinforcementFineTuningJobRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DebugReinforcementFineTuningJobRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DebugReinforcementFineTuningJobResponse(_message.Message):
    __slots__ = ("name", "failed_job_name")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FAILED_JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    failed_job_name: str
    def __init__(self, name: _Optional[str] = ..., failed_job_name: _Optional[str] = ...) -> None: ...
