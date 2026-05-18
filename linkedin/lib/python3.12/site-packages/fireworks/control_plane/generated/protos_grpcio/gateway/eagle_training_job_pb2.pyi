from ..buf.validate import validate_pb2 as _validate_pb2
from . import deployment_pb2 as _deployment_pb2
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

class EagleTrainingJob(_message.Message):
    __slots__ = ("name", "display_name", "create_time", "expire_time", "created_by", "state", "status", "input_draft_model", "training_dataset", "base_model", "output_draft_model", "epochs_count", "learning_rate", "wandb_config", "early_stop_config", "accelerator_type", "accelerator_count", "update_time", "region", "is_turbo")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    INPUT_DRAFT_MODEL_FIELD_NUMBER: _ClassVar[int]
    TRAINING_DATASET_FIELD_NUMBER: _ClassVar[int]
    BASE_MODEL_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_DRAFT_MODEL_FIELD_NUMBER: _ClassVar[int]
    EPOCHS_COUNT_FIELD_NUMBER: _ClassVar[int]
    LEARNING_RATE_FIELD_NUMBER: _ClassVar[int]
    WANDB_CONFIG_FIELD_NUMBER: _ClassVar[int]
    EARLY_STOP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ACCELERATOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCELERATOR_COUNT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    IS_TURBO_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    create_time: _timestamp_pb2.Timestamp
    expire_time: _timestamp_pb2.Timestamp
    created_by: str
    state: _status_pb2.JobState
    status: _status_pb2.Status
    input_draft_model: str
    training_dataset: str
    base_model: str
    output_draft_model: str
    epochs_count: float
    learning_rate: float
    wandb_config: _wandb_pb2.WandbConfig
    early_stop_config: _training_pb2.EarlyStopConfig
    accelerator_type: _deployment_pb2.AcceleratorType
    accelerator_count: int
    update_time: _timestamp_pb2.Timestamp
    region: _deployment_pb2.Region
    is_turbo: bool
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[str] = ..., state: _Optional[_Union[_status_pb2.JobState, str]] = ..., status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., input_draft_model: _Optional[str] = ..., training_dataset: _Optional[str] = ..., base_model: _Optional[str] = ..., output_draft_model: _Optional[str] = ..., epochs_count: _Optional[float] = ..., learning_rate: _Optional[float] = ..., wandb_config: _Optional[_Union[_wandb_pb2.WandbConfig, _Mapping]] = ..., early_stop_config: _Optional[_Union[_training_pb2.EarlyStopConfig, _Mapping]] = ..., accelerator_type: _Optional[_Union[_deployment_pb2.AcceleratorType, str]] = ..., accelerator_count: _Optional[int] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., region: _Optional[_Union[_deployment_pb2.Region, str]] = ..., is_turbo: bool = ...) -> None: ...

class GetEagleTrainingJobRequest(_message.Message):
    __slots__ = ("name", "read_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class CreateEagleTrainingJobRequest(_message.Message):
    __slots__ = ("parent", "eagle_training_job", "eagle_training_job_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EAGLE_TRAINING_JOB_FIELD_NUMBER: _ClassVar[int]
    EAGLE_TRAINING_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    eagle_training_job: EagleTrainingJob
    eagle_training_job_id: str
    def __init__(self, parent: _Optional[str] = ..., eagle_training_job: _Optional[_Union[EagleTrainingJob, _Mapping]] = ..., eagle_training_job_id: _Optional[str] = ...) -> None: ...

class ListEagleTrainingJobsRequest(_message.Message):
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

class ListEagleTrainingJobsResponse(_message.Message):
    __slots__ = ("eagle_training_jobs", "next_page_token", "total_size")
    EAGLE_TRAINING_JOBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    eagle_training_jobs: _containers.RepeatedCompositeFieldContainer[EagleTrainingJob]
    next_page_token: str
    total_size: int
    def __init__(self, eagle_training_jobs: _Optional[_Iterable[_Union[EagleTrainingJob, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class UpdateEagleTrainingJobRequest(_message.Message):
    __slots__ = ("eagle_training_job", "update_mask")
    EAGLE_TRAINING_JOB_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    eagle_training_job: EagleTrainingJob
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, eagle_training_job: _Optional[_Union[EagleTrainingJob, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteEagleTrainingJobRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
