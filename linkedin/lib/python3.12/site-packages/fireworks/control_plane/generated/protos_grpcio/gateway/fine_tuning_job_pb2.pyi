from ..buf.validate import validate_pb2 as _validate_pb2
from . import options_pb2 as _options_pb2
from . import status_pb2 as _status_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.api import visibility_pb2 as _visibility_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FineTuningJob(_message.Message):
    __slots__ = ("name", "display_name", "create_time", "state", "dataset", "datasets", "status", "created_by", "container_version", "model_id", "legacy_job", "text_completion", "text_classification", "conversation", "draft_model_data", "draft_model", "genie", "base_model", "warm_start_from", "early_stop", "epochs", "learning_rate", "lr_scheduler_type", "warmup_steps", "lora_alpha", "lora_rank", "lora_target_modules", "batch_size", "micro_batch_size", "mask_token", "pad_token", "cutoff_length", "wandb_url", "wandb_entity", "wandb_api_key", "wandb_project", "evaluation", "evaluation_split", "evaluation_dataset", "dependent_jobs")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[FineTuningJob.State]
        CREATING: _ClassVar[FineTuningJob.State]
        PENDING: _ClassVar[FineTuningJob.State]
        RUNNING: _ClassVar[FineTuningJob.State]
        COMPLETED: _ClassVar[FineTuningJob.State]
        FAILED: _ClassVar[FineTuningJob.State]
        DELETING: _ClassVar[FineTuningJob.State]
    STATE_UNSPECIFIED: FineTuningJob.State
    CREATING: FineTuningJob.State
    PENDING: FineTuningJob.State
    RUNNING: FineTuningJob.State
    COMPLETED: FineTuningJob.State
    FAILED: FineTuningJob.State
    DELETING: FineTuningJob.State
    class Dataset(_message.Message):
        __slots__ = ("dataset",)
        DATASET_FIELD_NUMBER: _ClassVar[int]
        dataset: str
        def __init__(self, dataset: _Optional[str] = ...) -> None: ...
    class LegacyJob(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class TextCompletion(_message.Message):
        __slots__ = ("input_template", "output_template")
        INPUT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
        input_template: str
        output_template: str
        def __init__(self, input_template: _Optional[str] = ..., output_template: _Optional[str] = ...) -> None: ...
    class TextClassification(_message.Message):
        __slots__ = ("text", "label")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        text: str
        label: str
        def __init__(self, text: _Optional[str] = ..., label: _Optional[str] = ...) -> None: ...
    class DraftModelData(_message.Message):
        __slots__ = ("deployment_name", "jinja_template", "cleanup_deployment")
        DEPLOYMENT_NAME_FIELD_NUMBER: _ClassVar[int]
        JINJA_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
        CLEANUP_DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
        deployment_name: str
        jinja_template: str
        cleanup_deployment: bool
        def __init__(self, deployment_name: _Optional[str] = ..., jinja_template: _Optional[str] = ..., cleanup_deployment: bool = ...) -> None: ...
    class DraftModel(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Conversation(_message.Message):
        __slots__ = ("jinja_template",)
        JINJA_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
        jinja_template: str
        def __init__(self, jinja_template: _Optional[str] = ...) -> None: ...
    class Genie(_message.Message):
        __slots__ = ("pipeline_name",)
        PIPELINE_NAME_FIELD_NUMBER: _ClassVar[int]
        pipeline_name: str
        def __init__(self, pipeline_name: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DATASET_FIELD_NUMBER: _ClassVar[int]
    DATASETS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_VERSION_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    LEGACY_JOB_FIELD_NUMBER: _ClassVar[int]
    TEXT_COMPLETION_FIELD_NUMBER: _ClassVar[int]
    TEXT_CLASSIFICATION_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    DRAFT_MODEL_DATA_FIELD_NUMBER: _ClassVar[int]
    DRAFT_MODEL_FIELD_NUMBER: _ClassVar[int]
    GENIE_FIELD_NUMBER: _ClassVar[int]
    BASE_MODEL_FIELD_NUMBER: _ClassVar[int]
    WARM_START_FROM_FIELD_NUMBER: _ClassVar[int]
    EARLY_STOP_FIELD_NUMBER: _ClassVar[int]
    EPOCHS_FIELD_NUMBER: _ClassVar[int]
    LEARNING_RATE_FIELD_NUMBER: _ClassVar[int]
    LR_SCHEDULER_TYPE_FIELD_NUMBER: _ClassVar[int]
    WARMUP_STEPS_FIELD_NUMBER: _ClassVar[int]
    LORA_ALPHA_FIELD_NUMBER: _ClassVar[int]
    LORA_RANK_FIELD_NUMBER: _ClassVar[int]
    LORA_TARGET_MODULES_FIELD_NUMBER: _ClassVar[int]
    BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    MICRO_BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    MASK_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAD_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CUTOFF_LENGTH_FIELD_NUMBER: _ClassVar[int]
    WANDB_URL_FIELD_NUMBER: _ClassVar[int]
    WANDB_ENTITY_FIELD_NUMBER: _ClassVar[int]
    WANDB_API_KEY_FIELD_NUMBER: _ClassVar[int]
    WANDB_PROJECT_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_SPLIT_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_DATASET_FIELD_NUMBER: _ClassVar[int]
    DEPENDENT_JOBS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    create_time: _timestamp_pb2.Timestamp
    state: FineTuningJob.State
    dataset: str
    datasets: _containers.RepeatedCompositeFieldContainer[FineTuningJob.Dataset]
    status: _status_pb2.Status
    created_by: str
    container_version: str
    model_id: str
    legacy_job: FineTuningJob.LegacyJob
    text_completion: FineTuningJob.TextCompletion
    text_classification: FineTuningJob.TextClassification
    conversation: FineTuningJob.Conversation
    draft_model_data: FineTuningJob.DraftModelData
    draft_model: FineTuningJob.DraftModel
    genie: FineTuningJob.Genie
    base_model: str
    warm_start_from: str
    early_stop: bool
    epochs: float
    learning_rate: float
    lr_scheduler_type: str
    warmup_steps: int
    lora_alpha: int
    lora_rank: int
    lora_target_modules: _containers.RepeatedScalarFieldContainer[str]
    batch_size: int
    micro_batch_size: int
    mask_token: str
    pad_token: str
    cutoff_length: int
    wandb_url: str
    wandb_entity: str
    wandb_api_key: str
    wandb_project: str
    evaluation: bool
    evaluation_split: float
    evaluation_dataset: str
    dependent_jobs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., state: _Optional[_Union[FineTuningJob.State, str]] = ..., dataset: _Optional[str] = ..., datasets: _Optional[_Iterable[_Union[FineTuningJob.Dataset, _Mapping]]] = ..., status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., created_by: _Optional[str] = ..., container_version: _Optional[str] = ..., model_id: _Optional[str] = ..., legacy_job: _Optional[_Union[FineTuningJob.LegacyJob, _Mapping]] = ..., text_completion: _Optional[_Union[FineTuningJob.TextCompletion, _Mapping]] = ..., text_classification: _Optional[_Union[FineTuningJob.TextClassification, _Mapping]] = ..., conversation: _Optional[_Union[FineTuningJob.Conversation, _Mapping]] = ..., draft_model_data: _Optional[_Union[FineTuningJob.DraftModelData, _Mapping]] = ..., draft_model: _Optional[_Union[FineTuningJob.DraftModel, _Mapping]] = ..., genie: _Optional[_Union[FineTuningJob.Genie, _Mapping]] = ..., base_model: _Optional[str] = ..., warm_start_from: _Optional[str] = ..., early_stop: bool = ..., epochs: _Optional[float] = ..., learning_rate: _Optional[float] = ..., lr_scheduler_type: _Optional[str] = ..., warmup_steps: _Optional[int] = ..., lora_alpha: _Optional[int] = ..., lora_rank: _Optional[int] = ..., lora_target_modules: _Optional[_Iterable[str]] = ..., batch_size: _Optional[int] = ..., micro_batch_size: _Optional[int] = ..., mask_token: _Optional[str] = ..., pad_token: _Optional[str] = ..., cutoff_length: _Optional[int] = ..., wandb_url: _Optional[str] = ..., wandb_entity: _Optional[str] = ..., wandb_api_key: _Optional[str] = ..., wandb_project: _Optional[str] = ..., evaluation: bool = ..., evaluation_split: _Optional[float] = ..., evaluation_dataset: _Optional[str] = ..., dependent_jobs: _Optional[_Iterable[str]] = ...) -> None: ...

class GetFineTuningJobRequest(_message.Message):
    __slots__ = ("name", "read_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class CreateFineTuningJobRequest(_message.Message):
    __slots__ = ("parent", "fine_tuning_job", "debug", "fine_tuning_job_id", "update_time")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FINE_TUNING_JOB_FIELD_NUMBER: _ClassVar[int]
    DEBUG_FIELD_NUMBER: _ClassVar[int]
    FINE_TUNING_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    parent: str
    fine_tuning_job: FineTuningJob
    debug: bool
    fine_tuning_job_id: str
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, parent: _Optional[str] = ..., fine_tuning_job: _Optional[_Union[FineTuningJob, _Mapping]] = ..., debug: bool = ..., fine_tuning_job_id: _Optional[str] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListFineTuningJobsRequest(_message.Message):
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

class ListFineTuningJobsResponse(_message.Message):
    __slots__ = ("fine_tuning_jobs", "next_page_token", "total_size")
    FINE_TUNING_JOBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    fine_tuning_jobs: _containers.RepeatedCompositeFieldContainer[FineTuningJob]
    next_page_token: str
    total_size: int
    def __init__(self, fine_tuning_jobs: _Optional[_Iterable[_Union[FineTuningJob, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class UpdateFineTuningJobRequest(_message.Message):
    __slots__ = ("fine_tuning_job", "update_mask")
    FINE_TUNING_JOB_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    fine_tuning_job: FineTuningJob
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, fine_tuning_job: _Optional[_Union[FineTuningJob, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteFineTuningJobRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
