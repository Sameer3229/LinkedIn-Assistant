from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WandbConfig(_message.Message):
    __slots__ = ("enabled", "api_key", "project", "entity", "run_id", "url")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    api_key: str
    project: str
    entity: str
    run_id: str
    url: str
    def __init__(self, enabled: bool = ..., api_key: _Optional[str] = ..., project: _Optional[str] = ..., entity: _Optional[str] = ..., run_id: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...
