from . import deployment_pb2 as _deployment_pb2
from . import job_progress_pb2 as _job_progress_pb2
from . import options_pb2 as _options_pb2
from . import status_pb2 as _status_pb2
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

class BatchInferenceJob(_message.Message):
    __slots__ = ("name", "display_name", "create_time", "expire_time", "created_by", "state", "status", "model", "input_dataset_id", "output_dataset_id", "append_to_messages", "inference_parameters", "update_time", "ending_assistant_messages", "region", "max_replica_count", "accelerator_type", "accelerator_count", "precision", "reinforcement_fine_tuning_epoch_id", "skip_dataset_validation", "job_progress", "priority", "toleration", "deployment_extra_args", "mcp_server", "continued_from_job_name")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    INPUT_DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    APPEND_TO_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    INFERENCE_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ENDING_ASSISTANT_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    MAX_REPLICA_COUNT_FIELD_NUMBER: _ClassVar[int]
    ACCELERATOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCELERATOR_COUNT_FIELD_NUMBER: _ClassVar[int]
    PRECISION_FIELD_NUMBER: _ClassVar[int]
    REINFORCEMENT_FINE_TUNING_EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
    SKIP_DATASET_VALIDATION_FIELD_NUMBER: _ClassVar[int]
    JOB_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    TOLERATION_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_EXTRA_ARGS_FIELD_NUMBER: _ClassVar[int]
    MCP_SERVER_FIELD_NUMBER: _ClassVar[int]
    CONTINUED_FROM_JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    create_time: _timestamp_pb2.Timestamp
    expire_time: _timestamp_pb2.Timestamp
    created_by: str
    state: _status_pb2.JobState
    status: _status_pb2.Status
    model: str
    input_dataset_id: str
    output_dataset_id: str
    append_to_messages: AppendToMessages
    inference_parameters: InferenceParameters
    update_time: _timestamp_pb2.Timestamp
    ending_assistant_messages: str
    region: _deployment_pb2.Region
    max_replica_count: int
    accelerator_type: _deployment_pb2.AcceleratorType
    accelerator_count: int
    precision: _deployment_pb2.Deployment.Precision
    reinforcement_fine_tuning_epoch_id: str
    skip_dataset_validation: bool
    job_progress: _job_progress_pb2.JobProgress
    priority: int
    toleration: str
    deployment_extra_args: _containers.RepeatedScalarFieldContainer[str]
    mcp_server: str
    continued_from_job_name: str
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[str] = ..., state: _Optional[_Union[_status_pb2.JobState, str]] = ..., status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., model: _Optional[str] = ..., input_dataset_id: _Optional[str] = ..., output_dataset_id: _Optional[str] = ..., append_to_messages: _Optional[_Union[AppendToMessages, _Mapping]] = ..., inference_parameters: _Optional[_Union[InferenceParameters, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ending_assistant_messages: _Optional[str] = ..., region: _Optional[_Union[_deployment_pb2.Region, str]] = ..., max_replica_count: _Optional[int] = ..., accelerator_type: _Optional[_Union[_deployment_pb2.AcceleratorType, str]] = ..., accelerator_count: _Optional[int] = ..., precision: _Optional[_Union[_deployment_pb2.Deployment.Precision, str]] = ..., reinforcement_fine_tuning_epoch_id: _Optional[str] = ..., skip_dataset_validation: bool = ..., job_progress: _Optional[_Union[_job_progress_pb2.JobProgress, _Mapping]] = ..., priority: _Optional[int] = ..., toleration: _Optional[str] = ..., deployment_extra_args: _Optional[_Iterable[str]] = ..., mcp_server: _Optional[str] = ..., continued_from_job_name: _Optional[str] = ...) -> None: ...

class InferenceParameters(_message.Message):
    __slots__ = ("max_tokens", "temperature", "top_p", "n", "extra_body", "top_k")
    MAX_TOKENS_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    TOP_P_FIELD_NUMBER: _ClassVar[int]
    N_FIELD_NUMBER: _ClassVar[int]
    EXTRA_BODY_FIELD_NUMBER: _ClassVar[int]
    TOP_K_FIELD_NUMBER: _ClassVar[int]
    max_tokens: int
    temperature: float
    top_p: float
    n: int
    extra_body: str
    top_k: int
    def __init__(self, max_tokens: _Optional[int] = ..., temperature: _Optional[float] = ..., top_p: _Optional[float] = ..., n: _Optional[int] = ..., extra_body: _Optional[str] = ..., top_k: _Optional[int] = ...) -> None: ...

class AppendToMessages(_message.Message):
    __slots__ = ("unroll_multiple_responses",)
    UNROLL_MULTIPLE_RESPONSES_FIELD_NUMBER: _ClassVar[int]
    unroll_multiple_responses: bool
    def __init__(self, unroll_multiple_responses: bool = ...) -> None: ...

class GetBatchInferenceJobRequest(_message.Message):
    __slots__ = ("name", "read_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class CreateBatchInferenceJobRequest(_message.Message):
    __slots__ = ("parent", "batch_inference_job", "batch_inference_job_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BATCH_INFERENCE_JOB_FIELD_NUMBER: _ClassVar[int]
    BATCH_INFERENCE_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    batch_inference_job: BatchInferenceJob
    batch_inference_job_id: str
    def __init__(self, parent: _Optional[str] = ..., batch_inference_job: _Optional[_Union[BatchInferenceJob, _Mapping]] = ..., batch_inference_job_id: _Optional[str] = ...) -> None: ...

class ListBatchInferenceJobsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by", "show_internal", "read_mask")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    SHOW_INTERNAL_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    show_internal: bool
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ..., show_internal: bool = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListBatchInferenceJobsResponse(_message.Message):
    __slots__ = ("batch_inference_jobs", "next_page_token", "total_size")
    BATCH_INFERENCE_JOBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    batch_inference_jobs: _containers.RepeatedCompositeFieldContainer[BatchInferenceJob]
    next_page_token: str
    total_size: int
    def __init__(self, batch_inference_jobs: _Optional[_Iterable[_Union[BatchInferenceJob, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class UpdateBatchInferenceJobRequest(_message.Message):
    __slots__ = ("batch_inference_job", "update_mask")
    BATCH_INFERENCE_JOB_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    batch_inference_job: BatchInferenceJob
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, batch_inference_job: _Optional[_Union[BatchInferenceJob, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteBatchInferenceJobRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetBatchInferenceJobInputUploadEndpointRequest(_message.Message):
    __slots__ = ("name", "filename_to_size")
    class FilenameToSizeEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    FILENAME_TO_SIZE_FIELD_NUMBER: _ClassVar[int]
    name: str
    filename_to_size: _containers.ScalarMap[str, int]
    def __init__(self, name: _Optional[str] = ..., filename_to_size: _Optional[_Mapping[str, int]] = ...) -> None: ...

class GetBatchInferenceJobInputUploadEndpointResponse(_message.Message):
    __slots__ = ("filename_to_signed_urls",)
    class FilenameToSignedUrlsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    FILENAME_TO_SIGNED_URLS_FIELD_NUMBER: _ClassVar[int]
    filename_to_signed_urls: _containers.ScalarMap[str, str]
    def __init__(self, filename_to_signed_urls: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ValidateBatchInferenceJobInputUploadRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetBatchInferenceJobOutputDownloadEndpointRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetBatchInferenceJobOutputDownloadEndpointResponse(_message.Message):
    __slots__ = ("filename_to_signed_urls",)
    class FilenameToSignedUrlsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    FILENAME_TO_SIGNED_URLS_FIELD_NUMBER: _ClassVar[int]
    filename_to_signed_urls: _containers.ScalarMap[str, str]
    def __init__(self, filename_to_signed_urls: _Optional[_Mapping[str, str]] = ...) -> None: ...
