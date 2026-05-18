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

class ReinforcementFineTuningEpoch(_message.Message):
    __slots__ = ("name", "create_time", "completed_time", "dataset", "evaluation_dataset", "eval_auto_carveout", "state", "status", "created_by", "update_time", "training_config", "evaluator", "wandb_config", "rollout_n", "ending_assistant_messages", "reinforcement_fine_tuning_job_id", "job_progress", "inference_parameters")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_TIME_FIELD_NUMBER: _ClassVar[int]
    DATASET_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_DATASET_FIELD_NUMBER: _ClassVar[int]
    EVAL_AUTO_CARVEOUT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    TRAINING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_FIELD_NUMBER: _ClassVar[int]
    WANDB_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ROLLOUT_N_FIELD_NUMBER: _ClassVar[int]
    ENDING_ASSISTANT_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    REINFORCEMENT_FINE_TUNING_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    INFERENCE_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    completed_time: _timestamp_pb2.Timestamp
    dataset: str
    evaluation_dataset: str
    eval_auto_carveout: bool
    state: _status_pb2.JobState
    status: _status_pb2.Status
    created_by: str
    update_time: _timestamp_pb2.Timestamp
    training_config: _training_pb2.BaseTrainingConfig
    evaluator: str
    wandb_config: _wandb_pb2.WandbConfig
    rollout_n: int
    ending_assistant_messages: str
    reinforcement_fine_tuning_job_id: str
    job_progress: _job_progress_pb2.JobProgress
    inference_parameters: _batch_inference_job_pb2.InferenceParameters
    def __init__(self, name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., completed_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., dataset: _Optional[str] = ..., evaluation_dataset: _Optional[str] = ..., eval_auto_carveout: bool = ..., state: _Optional[_Union[_status_pb2.JobState, str]] = ..., status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., created_by: _Optional[str] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., training_config: _Optional[_Union[_training_pb2.BaseTrainingConfig, _Mapping]] = ..., evaluator: _Optional[str] = ..., wandb_config: _Optional[_Union[_wandb_pb2.WandbConfig, _Mapping]] = ..., rollout_n: _Optional[int] = ..., ending_assistant_messages: _Optional[str] = ..., reinforcement_fine_tuning_job_id: _Optional[str] = ..., job_progress: _Optional[_Union[_job_progress_pb2.JobProgress, _Mapping]] = ..., inference_parameters: _Optional[_Union[_batch_inference_job_pb2.InferenceParameters, _Mapping]] = ...) -> None: ...

class GetReinforcementFineTuningEpochRequest(_message.Message):
    __slots__ = ("name", "read_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class CreateReinforcementFineTuningEpochRequest(_message.Message):
    __slots__ = ("parent", "reinforcement_fine_tuning_epoch", "debug", "reinforcement_fine_tuning_epoch_id", "skip_validations")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REINFORCEMENT_FINE_TUNING_EPOCH_FIELD_NUMBER: _ClassVar[int]
    DEBUG_FIELD_NUMBER: _ClassVar[int]
    REINFORCEMENT_FINE_TUNING_EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
    SKIP_VALIDATIONS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    reinforcement_fine_tuning_epoch: ReinforcementFineTuningEpoch
    debug: bool
    reinforcement_fine_tuning_epoch_id: str
    skip_validations: bool
    def __init__(self, parent: _Optional[str] = ..., reinforcement_fine_tuning_epoch: _Optional[_Union[ReinforcementFineTuningEpoch, _Mapping]] = ..., debug: bool = ..., reinforcement_fine_tuning_epoch_id: _Optional[str] = ..., skip_validations: bool = ...) -> None: ...

class ListReinforcementFineTuningEpochsRequest(_message.Message):
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

class ListReinforcementFineTuningEpochsResponse(_message.Message):
    __slots__ = ("reinforcement_fine_tuning_epochs", "next_page_token", "total_size")
    REINFORCEMENT_FINE_TUNING_EPOCHS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    reinforcement_fine_tuning_epochs: _containers.RepeatedCompositeFieldContainer[ReinforcementFineTuningEpoch]
    next_page_token: str
    total_size: int
    def __init__(self, reinforcement_fine_tuning_epochs: _Optional[_Iterable[_Union[ReinforcementFineTuningEpoch, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class DeleteReinforcementFineTuningEpochRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
