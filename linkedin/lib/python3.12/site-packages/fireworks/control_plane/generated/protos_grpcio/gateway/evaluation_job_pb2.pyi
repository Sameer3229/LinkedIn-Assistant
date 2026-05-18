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

class EvaluationJob(_message.Message):
    __slots__ = ("name", "display_name", "create_time", "created_by", "state", "status", "evaluator", "input_dataset", "output_dataset", "metrics", "output_stats", "update_time", "reinforcement_fine_tuning_epoch_id", "skip_dataset_validation", "job_progress", "region")
    class MetricsEntry(_message.Message):
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
    EVALUATOR_FIELD_NUMBER: _ClassVar[int]
    INPUT_DATASET_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_DATASET_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_STATS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    REINFORCEMENT_FINE_TUNING_EPOCH_ID_FIELD_NUMBER: _ClassVar[int]
    SKIP_DATASET_VALIDATION_FIELD_NUMBER: _ClassVar[int]
    JOB_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    create_time: _timestamp_pb2.Timestamp
    created_by: str
    state: _status_pb2.JobState
    status: _status_pb2.Status
    evaluator: str
    input_dataset: str
    output_dataset: str
    metrics: _containers.ScalarMap[str, float]
    output_stats: str
    update_time: _timestamp_pb2.Timestamp
    reinforcement_fine_tuning_epoch_id: str
    skip_dataset_validation: bool
    job_progress: _job_progress_pb2.JobProgress
    region: _deployment_pb2.Region
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[str] = ..., state: _Optional[_Union[_status_pb2.JobState, str]] = ..., status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., evaluator: _Optional[str] = ..., input_dataset: _Optional[str] = ..., output_dataset: _Optional[str] = ..., metrics: _Optional[_Mapping[str, float]] = ..., output_stats: _Optional[str] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., reinforcement_fine_tuning_epoch_id: _Optional[str] = ..., skip_dataset_validation: bool = ..., job_progress: _Optional[_Union[_job_progress_pb2.JobProgress, _Mapping]] = ..., region: _Optional[_Union[_deployment_pb2.Region, str]] = ...) -> None: ...

class GetEvaluationJobRequest(_message.Message):
    __slots__ = ("name", "read_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class CreateEvaluationJobRequest(_message.Message):
    __slots__ = ("parent", "evaluation_job", "evaluation_job_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_JOB_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    evaluation_job: EvaluationJob
    evaluation_job_id: str
    def __init__(self, parent: _Optional[str] = ..., evaluation_job: _Optional[_Union[EvaluationJob, _Mapping]] = ..., evaluation_job_id: _Optional[str] = ...) -> None: ...

class ListEvaluationJobsRequest(_message.Message):
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

class ListEvaluationJobsResponse(_message.Message):
    __slots__ = ("evaluation_jobs", "next_page_token", "total_size")
    EVALUATION_JOBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    evaluation_jobs: _containers.RepeatedCompositeFieldContainer[EvaluationJob]
    next_page_token: str
    total_size: int
    def __init__(self, evaluation_jobs: _Optional[_Iterable[_Union[EvaluationJob, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class DeleteEvaluationJobRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
