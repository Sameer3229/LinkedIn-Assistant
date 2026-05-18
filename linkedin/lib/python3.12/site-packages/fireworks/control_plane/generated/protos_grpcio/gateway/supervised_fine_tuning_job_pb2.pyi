from ..buf.validate import validate_pb2 as _validate_pb2
from . import deployment_pb2 as _deployment_pb2
from . import job_progress_pb2 as _job_progress_pb2
from . import options_pb2 as _options_pb2
from . import status_pb2 as _status_pb2
from . import wandb_pb2 as _wandb_pb2
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

class SupervisedFineTuningJob(_message.Message):
    __slots__ = ("name", "display_name", "create_time", "completed_time", "dataset", "state", "status", "created_by", "output_model", "base_model", "warm_start_from", "jinja_template", "early_stop", "epochs", "learning_rate", "max_context_length", "lora_rank", "base_model_weight_precision", "wandb_config", "evaluation_dataset", "accelerator_type", "accelerator_count", "is_turbo", "eval_auto_carveout", "region", "update_time", "nodes", "batch_size", "mtp_enabled", "mtp_num_draft_tokens", "mtp_freeze_base_model", "job_progress", "custom_image_tag", "precision", "extra_args", "metrics_file_signed_url")
    class WeightPrecision(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        WEIGHT_PRECISION_UNSPECIFIED: _ClassVar[SupervisedFineTuningJob.WeightPrecision]
        BFLOAT16: _ClassVar[SupervisedFineTuningJob.WeightPrecision]
        INT8: _ClassVar[SupervisedFineTuningJob.WeightPrecision]
        NF4: _ClassVar[SupervisedFineTuningJob.WeightPrecision]
        FP8: _ClassVar[SupervisedFineTuningJob.WeightPrecision]
        FP4_FP8: _ClassVar[SupervisedFineTuningJob.WeightPrecision]
    WEIGHT_PRECISION_UNSPECIFIED: SupervisedFineTuningJob.WeightPrecision
    BFLOAT16: SupervisedFineTuningJob.WeightPrecision
    INT8: SupervisedFineTuningJob.WeightPrecision
    NF4: SupervisedFineTuningJob.WeightPrecision
    FP8: SupervisedFineTuningJob.WeightPrecision
    FP4_FP8: SupervisedFineTuningJob.WeightPrecision
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_TIME_FIELD_NUMBER: _ClassVar[int]
    DATASET_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_MODEL_FIELD_NUMBER: _ClassVar[int]
    BASE_MODEL_FIELD_NUMBER: _ClassVar[int]
    WARM_START_FROM_FIELD_NUMBER: _ClassVar[int]
    JINJA_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    EARLY_STOP_FIELD_NUMBER: _ClassVar[int]
    EPOCHS_FIELD_NUMBER: _ClassVar[int]
    LEARNING_RATE_FIELD_NUMBER: _ClassVar[int]
    MAX_CONTEXT_LENGTH_FIELD_NUMBER: _ClassVar[int]
    LORA_RANK_FIELD_NUMBER: _ClassVar[int]
    BASE_MODEL_WEIGHT_PRECISION_FIELD_NUMBER: _ClassVar[int]
    WANDB_CONFIG_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_DATASET_FIELD_NUMBER: _ClassVar[int]
    ACCELERATOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCELERATOR_COUNT_FIELD_NUMBER: _ClassVar[int]
    IS_TURBO_FIELD_NUMBER: _ClassVar[int]
    EVAL_AUTO_CARVEOUT_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    MTP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    MTP_NUM_DRAFT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    MTP_FREEZE_BASE_MODEL_FIELD_NUMBER: _ClassVar[int]
    JOB_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_IMAGE_TAG_FIELD_NUMBER: _ClassVar[int]
    PRECISION_FIELD_NUMBER: _ClassVar[int]
    EXTRA_ARGS_FIELD_NUMBER: _ClassVar[int]
    METRICS_FILE_SIGNED_URL_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    create_time: _timestamp_pb2.Timestamp
    completed_time: _timestamp_pb2.Timestamp
    dataset: str
    state: _status_pb2.JobState
    status: _status_pb2.Status
    created_by: str
    output_model: str
    base_model: str
    warm_start_from: str
    jinja_template: str
    early_stop: bool
    epochs: int
    learning_rate: float
    max_context_length: int
    lora_rank: int
    base_model_weight_precision: SupervisedFineTuningJob.WeightPrecision
    wandb_config: _wandb_pb2.WandbConfig
    evaluation_dataset: str
    accelerator_type: _deployment_pb2.AcceleratorType
    accelerator_count: int
    is_turbo: bool
    eval_auto_carveout: bool
    region: _deployment_pb2.Region
    update_time: _timestamp_pb2.Timestamp
    nodes: int
    batch_size: int
    mtp_enabled: bool
    mtp_num_draft_tokens: int
    mtp_freeze_base_model: bool
    job_progress: _job_progress_pb2.JobProgress
    custom_image_tag: str
    precision: SupervisedFineTuningJob.WeightPrecision
    extra_args: _containers.RepeatedScalarFieldContainer[str]
    metrics_file_signed_url: str
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., completed_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., dataset: _Optional[str] = ..., state: _Optional[_Union[_status_pb2.JobState, str]] = ..., status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., created_by: _Optional[str] = ..., output_model: _Optional[str] = ..., base_model: _Optional[str] = ..., warm_start_from: _Optional[str] = ..., jinja_template: _Optional[str] = ..., early_stop: bool = ..., epochs: _Optional[int] = ..., learning_rate: _Optional[float] = ..., max_context_length: _Optional[int] = ..., lora_rank: _Optional[int] = ..., base_model_weight_precision: _Optional[_Union[SupervisedFineTuningJob.WeightPrecision, str]] = ..., wandb_config: _Optional[_Union[_wandb_pb2.WandbConfig, _Mapping]] = ..., evaluation_dataset: _Optional[str] = ..., accelerator_type: _Optional[_Union[_deployment_pb2.AcceleratorType, str]] = ..., accelerator_count: _Optional[int] = ..., is_turbo: bool = ..., eval_auto_carveout: bool = ..., region: _Optional[_Union[_deployment_pb2.Region, str]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., nodes: _Optional[int] = ..., batch_size: _Optional[int] = ..., mtp_enabled: bool = ..., mtp_num_draft_tokens: _Optional[int] = ..., mtp_freeze_base_model: bool = ..., job_progress: _Optional[_Union[_job_progress_pb2.JobProgress, _Mapping]] = ..., custom_image_tag: _Optional[str] = ..., precision: _Optional[_Union[SupervisedFineTuningJob.WeightPrecision, str]] = ..., extra_args: _Optional[_Iterable[str]] = ..., metrics_file_signed_url: _Optional[str] = ...) -> None: ...

class GetSupervisedFineTuningJobRequest(_message.Message):
    __slots__ = ("name", "read_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class CreateSupervisedFineTuningJobRequest(_message.Message):
    __slots__ = ("parent", "supervised_fine_tuning_job", "debug", "supervised_fine_tuning_job_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SUPERVISED_FINE_TUNING_JOB_FIELD_NUMBER: _ClassVar[int]
    DEBUG_FIELD_NUMBER: _ClassVar[int]
    SUPERVISED_FINE_TUNING_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    supervised_fine_tuning_job: SupervisedFineTuningJob
    debug: bool
    supervised_fine_tuning_job_id: str
    def __init__(self, parent: _Optional[str] = ..., supervised_fine_tuning_job: _Optional[_Union[SupervisedFineTuningJob, _Mapping]] = ..., debug: bool = ..., supervised_fine_tuning_job_id: _Optional[str] = ...) -> None: ...

class ListSupervisedFineTuningJobsRequest(_message.Message):
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

class ListSupervisedFineTuningJobsResponse(_message.Message):
    __slots__ = ("supervised_fine_tuning_jobs", "next_page_token", "total_size")
    SUPERVISED_FINE_TUNING_JOBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    supervised_fine_tuning_jobs: _containers.RepeatedCompositeFieldContainer[SupervisedFineTuningJob]
    next_page_token: str
    total_size: int
    def __init__(self, supervised_fine_tuning_jobs: _Optional[_Iterable[_Union[SupervisedFineTuningJob, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class DeleteSupervisedFineTuningJobRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
