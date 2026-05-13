from . import deployment_pb2 as _deployment_pb2
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

class DatasetValidationFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATASET_VALIDATION_FORMAT_UNSPECIFIED: _ClassVar[DatasetValidationFormat]
    DATASET_VALIDATION_FORMAT_CHAT: _ClassVar[DatasetValidationFormat]
    DATASET_VALIDATION_FORMAT_CHAT_RELAXED: _ClassVar[DatasetValidationFormat]
    DATASET_VALIDATION_FORMAT_RLOR: _ClassVar[DatasetValidationFormat]
    DATASET_VALIDATION_FORMAT_BATCH_INFERENCE_STRICT: _ClassVar[DatasetValidationFormat]
    DATASET_VALIDATION_FORMAT_BATCH_INFERENCE_ALLOW_TRAILING_ASSISTANT: _ClassVar[DatasetValidationFormat]
    DATASET_VALIDATION_FORMAT_BATCH_INFERENCE: _ClassVar[DatasetValidationFormat]

class DatasetValidationJobResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATASET_VALIDATION_JOB_RESULT_UNSPECIFIED: _ClassVar[DatasetValidationJobResult]
    DATASET_VALIDATION_JOB_RESULT_SUCCESS: _ClassVar[DatasetValidationJobResult]
    DATASET_VALIDATION_JOB_RESULT_FAILURE: _ClassVar[DatasetValidationJobResult]
DATASET_VALIDATION_FORMAT_UNSPECIFIED: DatasetValidationFormat
DATASET_VALIDATION_FORMAT_CHAT: DatasetValidationFormat
DATASET_VALIDATION_FORMAT_CHAT_RELAXED: DatasetValidationFormat
DATASET_VALIDATION_FORMAT_RLOR: DatasetValidationFormat
DATASET_VALIDATION_FORMAT_BATCH_INFERENCE_STRICT: DatasetValidationFormat
DATASET_VALIDATION_FORMAT_BATCH_INFERENCE_ALLOW_TRAILING_ASSISTANT: DatasetValidationFormat
DATASET_VALIDATION_FORMAT_BATCH_INFERENCE: DatasetValidationFormat
DATASET_VALIDATION_JOB_RESULT_UNSPECIFIED: DatasetValidationJobResult
DATASET_VALIDATION_JOB_RESULT_SUCCESS: DatasetValidationJobResult
DATASET_VALIDATION_JOB_RESULT_FAILURE: DatasetValidationJobResult

class DatasetValidationJob(_message.Message):
    __slots__ = ("name", "display_name", "create_time", "created_by", "state", "status", "dataset_name", "format", "result", "validation_error", "dataset_names", "update_time", "rewards", "region", "custom_image_tag")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATASET_NAME_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_ERROR_FIELD_NUMBER: _ClassVar[int]
    DATASET_NAMES_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    REWARDS_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_IMAGE_TAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    create_time: _timestamp_pb2.Timestamp
    created_by: str
    state: _status_pb2.JobState
    status: _status_pb2.Status
    dataset_name: str
    format: DatasetValidationFormat
    result: DatasetValidationJobResult
    validation_error: str
    dataset_names: _containers.RepeatedScalarFieldContainer[str]
    update_time: _timestamp_pb2.Timestamp
    rewards: _containers.RepeatedScalarFieldContainer[str]
    region: _deployment_pb2.Region
    custom_image_tag: str
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[str] = ..., state: _Optional[_Union[_status_pb2.JobState, str]] = ..., status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., dataset_name: _Optional[str] = ..., format: _Optional[_Union[DatasetValidationFormat, str]] = ..., result: _Optional[_Union[DatasetValidationJobResult, str]] = ..., validation_error: _Optional[str] = ..., dataset_names: _Optional[_Iterable[str]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., rewards: _Optional[_Iterable[str]] = ..., region: _Optional[_Union[_deployment_pb2.Region, str]] = ..., custom_image_tag: _Optional[str] = ...) -> None: ...

class GetDatasetValidationJobRequest(_message.Message):
    __slots__ = ("name", "read_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class CreateDatasetValidationJobRequest(_message.Message):
    __slots__ = ("parent", "dataset_validation_job", "dataset_validation_job_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DATASET_VALIDATION_JOB_FIELD_NUMBER: _ClassVar[int]
    DATASET_VALIDATION_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    dataset_validation_job: DatasetValidationJob
    dataset_validation_job_id: str
    def __init__(self, parent: _Optional[str] = ..., dataset_validation_job: _Optional[_Union[DatasetValidationJob, _Mapping]] = ..., dataset_validation_job_id: _Optional[str] = ...) -> None: ...

class ListDatasetValidationJobsRequest(_message.Message):
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

class ListDatasetValidationJobsResponse(_message.Message):
    __slots__ = ("dataset_validation_jobs", "next_page_token", "total_size")
    DATASET_VALIDATION_JOBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    dataset_validation_jobs: _containers.RepeatedCompositeFieldContainer[DatasetValidationJob]
    next_page_token: str
    total_size: int
    def __init__(self, dataset_validation_jobs: _Optional[_Iterable[_Union[DatasetValidationJob, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class DeleteDatasetValidationJobRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
