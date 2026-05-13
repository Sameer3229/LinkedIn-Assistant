from . import options_pb2 as _options_pb2
from . import status_pb2 as _status_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PromptTuningJob(_message.Message):
    __slots__ = ("name", "display_name", "create_time", "created_by", "state", "status", "model_name", "dataset_id", "input_prompt", "output_prompt", "prompt_to_metrics", "update_time")
    class PromptToMetricsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float
        def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    INPUT_PROMPT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_PROMPT_FIELD_NUMBER: _ClassVar[int]
    PROMPT_TO_METRICS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    create_time: _timestamp_pb2.Timestamp
    created_by: str
    state: _status_pb2.JobState
    status: _status_pb2.Status
    model_name: str
    dataset_id: str
    input_prompt: str
    output_prompt: str
    prompt_to_metrics: _containers.ScalarMap[str, float]
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[str] = ..., state: _Optional[_Union[_status_pb2.JobState, str]] = ..., status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., model_name: _Optional[str] = ..., dataset_id: _Optional[str] = ..., input_prompt: _Optional[str] = ..., output_prompt: _Optional[str] = ..., prompt_to_metrics: _Optional[_Mapping[str, float]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetPromptTuningJobRequest(_message.Message):
    __slots__ = ("name", "read_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class CreatePromptTuningJobRequest(_message.Message):
    __slots__ = ("parent", "prompt_tuning_job")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PROMPT_TUNING_JOB_FIELD_NUMBER: _ClassVar[int]
    parent: str
    prompt_tuning_job: PromptTuningJob
    def __init__(self, parent: _Optional[str] = ..., prompt_tuning_job: _Optional[_Union[PromptTuningJob, _Mapping]] = ...) -> None: ...

class ListPromptTuningJobsRequest(_message.Message):
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

class ListPromptTuningJobsResponse(_message.Message):
    __slots__ = ("prompt_tuning_jobs", "next_page_token", "total_size")
    PROMPT_TUNING_JOBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    prompt_tuning_jobs: _containers.RepeatedCompositeFieldContainer[PromptTuningJob]
    next_page_token: str
    total_size: int
    def __init__(self, prompt_tuning_jobs: _Optional[_Iterable[_Union[PromptTuningJob, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class DeletePromptTuningJobRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
