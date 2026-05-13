from . import options_pb2 as _options_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AbuseRule(_message.Message):
    __slots__ = ("name", "target", "type", "designation", "create_time", "update_time", "reason", "state")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[AbuseRule.Type]
        DOMAIN: _ClassVar[AbuseRule.Type]
        IP: _ClassVar[AbuseRule.Type]
        ACCOUNT: _ClassVar[AbuseRule.Type]
    TYPE_UNSPECIFIED: AbuseRule.Type
    DOMAIN: AbuseRule.Type
    IP: AbuseRule.Type
    ACCOUNT: AbuseRule.Type
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[AbuseRule.State]
        CREATING: _ClassVar[AbuseRule.State]
        READY: _ClassVar[AbuseRule.State]
        UPDATING: _ClassVar[AbuseRule.State]
        DELETING: _ClassVar[AbuseRule.State]
    STATE_UNSPECIFIED: AbuseRule.State
    CREATING: AbuseRule.State
    READY: AbuseRule.State
    UPDATING: AbuseRule.State
    DELETING: AbuseRule.State
    class Designation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DESIGNATION_UNSPECIFIED: _ClassVar[AbuseRule.Designation]
        ALLOWED: _ClassVar[AbuseRule.Designation]
        BLOCKED: _ClassVar[AbuseRule.Designation]
        SUSPICIOUS: _ClassVar[AbuseRule.Designation]
    DESIGNATION_UNSPECIFIED: AbuseRule.Designation
    ALLOWED: AbuseRule.Designation
    BLOCKED: AbuseRule.Designation
    SUSPICIOUS: AbuseRule.Designation
    NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DESIGNATION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    target: str
    type: AbuseRule.Type
    designation: AbuseRule.Designation
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    reason: str
    state: AbuseRule.State
    def __init__(self, name: _Optional[str] = ..., target: _Optional[str] = ..., type: _Optional[_Union[AbuseRule.Type, str]] = ..., designation: _Optional[_Union[AbuseRule.Designation, str]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., reason: _Optional[str] = ..., state: _Optional[_Union[AbuseRule.State, str]] = ...) -> None: ...
