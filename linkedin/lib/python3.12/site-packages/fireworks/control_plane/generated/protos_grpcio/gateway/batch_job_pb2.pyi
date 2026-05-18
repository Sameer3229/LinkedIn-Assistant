from . import options_pb2 as _options_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BatchJob(_message.Message):
    __slots__ = ("name", "display_name", "create_time", "start_time", "end_time", "created_by", "node_pool_id", "environment_id", "snapshot_id", "num_ranks", "env_vars", "role", "python_executor", "notebook_executor", "shell_executor", "image_ref", "annotations", "state", "status", "shared", "update_time")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[BatchJob.State]
        CREATING: _ClassVar[BatchJob.State]
        QUEUED: _ClassVar[BatchJob.State]
        PENDING: _ClassVar[BatchJob.State]
        RUNNING: _ClassVar[BatchJob.State]
        COMPLETED: _ClassVar[BatchJob.State]
        FAILED: _ClassVar[BatchJob.State]
        CANCELLING: _ClassVar[BatchJob.State]
        CANCELLED: _ClassVar[BatchJob.State]
        DELETING: _ClassVar[BatchJob.State]
    STATE_UNSPECIFIED: BatchJob.State
    CREATING: BatchJob.State
    QUEUED: BatchJob.State
    PENDING: BatchJob.State
    RUNNING: BatchJob.State
    COMPLETED: BatchJob.State
    FAILED: BatchJob.State
    CANCELLING: BatchJob.State
    CANCELLED: BatchJob.State
    DELETING: BatchJob.State
    class EnvVarsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class AnnotationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    NODE_POOL_ID_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    NUM_RANKS_FIELD_NUMBER: _ClassVar[int]
    ENV_VARS_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    PYTHON_EXECUTOR_FIELD_NUMBER: _ClassVar[int]
    NOTEBOOK_EXECUTOR_FIELD_NUMBER: _ClassVar[int]
    SHELL_EXECUTOR_FIELD_NUMBER: _ClassVar[int]
    IMAGE_REF_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SHARED_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    create_time: _timestamp_pb2.Timestamp
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    created_by: str
    node_pool_id: str
    environment_id: str
    snapshot_id: str
    num_ranks: int
    env_vars: _containers.ScalarMap[str, str]
    role: str
    python_executor: PythonExecutor
    notebook_executor: NotebookExecutor
    shell_executor: ShellExecutor
    image_ref: str
    annotations: _containers.ScalarMap[str, str]
    state: BatchJob.State
    status: str
    shared: bool
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[str] = ..., node_pool_id: _Optional[str] = ..., environment_id: _Optional[str] = ..., snapshot_id: _Optional[str] = ..., num_ranks: _Optional[int] = ..., env_vars: _Optional[_Mapping[str, str]] = ..., role: _Optional[str] = ..., python_executor: _Optional[_Union[PythonExecutor, _Mapping]] = ..., notebook_executor: _Optional[_Union[NotebookExecutor, _Mapping]] = ..., shell_executor: _Optional[_Union[ShellExecutor, _Mapping]] = ..., image_ref: _Optional[str] = ..., annotations: _Optional[_Mapping[str, str]] = ..., state: _Optional[_Union[BatchJob.State, str]] = ..., status: _Optional[str] = ..., shared: bool = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateBatchJobRequest(_message.Message):
    __slots__ = ("parent", "batch_job")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BATCH_JOB_FIELD_NUMBER: _ClassVar[int]
    parent: str
    batch_job: BatchJob
    def __init__(self, parent: _Optional[str] = ..., batch_job: _Optional[_Union[BatchJob, _Mapping]] = ...) -> None: ...

class GetBatchJobRequest(_message.Message):
    __slots__ = ("name", "read_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListBatchJobsRequest(_message.Message):
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

class ListBatchJobsResponse(_message.Message):
    __slots__ = ("batch_jobs", "next_page_token", "total_size")
    BATCH_JOBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    batch_jobs: _containers.RepeatedCompositeFieldContainer[BatchJob]
    next_page_token: str
    total_size: int
    def __init__(self, batch_jobs: _Optional[_Iterable[_Union[BatchJob, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class UpdateBatchJobRequest(_message.Message):
    __slots__ = ("batch_job", "update_mask")
    BATCH_JOB_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    batch_job: BatchJob
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, batch_job: _Optional[_Union[BatchJob, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteBatchJobRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class BatchDeleteBatchJobsRequest(_message.Message):
    __slots__ = ("parent", "names")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAMES_FIELD_NUMBER: _ClassVar[int]
    parent: str
    names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, parent: _Optional[str] = ..., names: _Optional[_Iterable[str]] = ...) -> None: ...

class CancelBatchJobRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetBatchJobLogsRequest(_message.Message):
    __slots__ = ("name", "ranks", "page_size", "page_token", "start_time", "filter", "start_from_head", "read_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    RANKS_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    START_FROM_HEAD_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    ranks: _containers.RepeatedScalarFieldContainer[int]
    page_size: int
    page_token: str
    start_time: _timestamp_pb2.Timestamp
    filter: str
    start_from_head: bool
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., ranks: _Optional[_Iterable[int]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., filter: _Optional[str] = ..., start_from_head: bool = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetBatchJobLogsResponse(_message.Message):
    __slots__ = ("entries", "next_page_token")
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[LogEntry]
    next_page_token: str
    def __init__(self, entries: _Optional[_Iterable[_Union[LogEntry, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class PythonExecutor(_message.Message):
    __slots__ = ("target_type", "target", "args")
    class TargetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TARGET_TYPE_UNSPECIFIED: _ClassVar[PythonExecutor.TargetType]
        MODULE: _ClassVar[PythonExecutor.TargetType]
        FILENAME: _ClassVar[PythonExecutor.TargetType]
    TARGET_TYPE_UNSPECIFIED: PythonExecutor.TargetType
    MODULE: PythonExecutor.TargetType
    FILENAME: PythonExecutor.TargetType
    TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    target_type: PythonExecutor.TargetType
    target: str
    args: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, target_type: _Optional[_Union[PythonExecutor.TargetType, str]] = ..., target: _Optional[str] = ..., args: _Optional[_Iterable[str]] = ...) -> None: ...

class ShellExecutor(_message.Message):
    __slots__ = ("command",)
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    command: str
    def __init__(self, command: _Optional[str] = ...) -> None: ...

class NotebookExecutor(_message.Message):
    __slots__ = ("notebook_filename",)
    NOTEBOOK_FILENAME_FIELD_NUMBER: _ClassVar[int]
    notebook_filename: str
    def __init__(self, notebook_filename: _Optional[str] = ...) -> None: ...

class LogEntry(_message.Message):
    __slots__ = ("log_time", "rank", "message")
    LOG_TIME_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    log_time: _timestamp_pb2.Timestamp
    rank: int
    message: str
    def __init__(self, log_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., rank: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...
