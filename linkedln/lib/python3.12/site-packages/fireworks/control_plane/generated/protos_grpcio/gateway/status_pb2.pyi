from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Code(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OK: _ClassVar[Code]
    CANCELLED: _ClassVar[Code]
    UNKNOWN: _ClassVar[Code]
    INVALID_ARGUMENT: _ClassVar[Code]
    DEADLINE_EXCEEDED: _ClassVar[Code]
    NOT_FOUND: _ClassVar[Code]
    ALREADY_EXISTS: _ClassVar[Code]
    PERMISSION_DENIED: _ClassVar[Code]
    UNAUTHENTICATED: _ClassVar[Code]
    RESOURCE_EXHAUSTED: _ClassVar[Code]
    FAILED_PRECONDITION: _ClassVar[Code]
    ABORTED: _ClassVar[Code]
    OUT_OF_RANGE: _ClassVar[Code]
    UNIMPLEMENTED: _ClassVar[Code]
    INTERNAL: _ClassVar[Code]
    UNAVAILABLE: _ClassVar[Code]
    DATA_LOSS: _ClassVar[Code]

class JobState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    JOB_STATE_UNSPECIFIED: _ClassVar[JobState]
    JOB_STATE_CREATING: _ClassVar[JobState]
    JOB_STATE_RUNNING: _ClassVar[JobState]
    JOB_STATE_COMPLETED: _ClassVar[JobState]
    JOB_STATE_FAILED: _ClassVar[JobState]
    JOB_STATE_CANCELLED: _ClassVar[JobState]
    JOB_STATE_DELETING: _ClassVar[JobState]
    JOB_STATE_WRITING_RESULTS: _ClassVar[JobState]
    JOB_STATE_VALIDATING: _ClassVar[JobState]
    JOB_STATE_ROLLOUT: _ClassVar[JobState]
    JOB_STATE_EVALUATION: _ClassVar[JobState]
    JOB_STATE_FAILED_CLEANING_UP: _ClassVar[JobState]
    JOB_STATE_DELETING_CLEANING_UP: _ClassVar[JobState]
    JOB_STATE_POLICY_UPDATE: _ClassVar[JobState]
    JOB_STATE_PENDING: _ClassVar[JobState]
    JOB_STATE_EXPIRED_CLEANING_UP: _ClassVar[JobState]
    JOB_STATE_EXPIRED: _ClassVar[JobState]
    JOB_STATE_CREATING_DEPENDENCIES: _ClassVar[JobState]
    JOB_STATE_RE_QUEUEING: _ClassVar[JobState]
    JOB_STATE_CREATING_INPUT_DATASET: _ClassVar[JobState]
OK: Code
CANCELLED: Code
UNKNOWN: Code
INVALID_ARGUMENT: Code
DEADLINE_EXCEEDED: Code
NOT_FOUND: Code
ALREADY_EXISTS: Code
PERMISSION_DENIED: Code
UNAUTHENTICATED: Code
RESOURCE_EXHAUSTED: Code
FAILED_PRECONDITION: Code
ABORTED: Code
OUT_OF_RANGE: Code
UNIMPLEMENTED: Code
INTERNAL: Code
UNAVAILABLE: Code
DATA_LOSS: Code
JOB_STATE_UNSPECIFIED: JobState
JOB_STATE_CREATING: JobState
JOB_STATE_RUNNING: JobState
JOB_STATE_COMPLETED: JobState
JOB_STATE_FAILED: JobState
JOB_STATE_CANCELLED: JobState
JOB_STATE_DELETING: JobState
JOB_STATE_WRITING_RESULTS: JobState
JOB_STATE_VALIDATING: JobState
JOB_STATE_ROLLOUT: JobState
JOB_STATE_EVALUATION: JobState
JOB_STATE_FAILED_CLEANING_UP: JobState
JOB_STATE_DELETING_CLEANING_UP: JobState
JOB_STATE_POLICY_UPDATE: JobState
JOB_STATE_PENDING: JobState
JOB_STATE_EXPIRED_CLEANING_UP: JobState
JOB_STATE_EXPIRED: JobState
JOB_STATE_CREATING_DEPENDENCIES: JobState
JOB_STATE_RE_QUEUEING: JobState
JOB_STATE_CREATING_INPUT_DATASET: JobState

class Status(_message.Message):
    __slots__ = ("code", "message")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: Code
    message: str
    def __init__(self, code: _Optional[_Union[Code, str]] = ..., message: _Optional[str] = ...) -> None: ...
