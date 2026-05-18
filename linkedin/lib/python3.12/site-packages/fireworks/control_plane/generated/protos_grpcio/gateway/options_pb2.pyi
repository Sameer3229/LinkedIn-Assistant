from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor
API_RESOURCE_FIELD_NUMBER: _ClassVar[int]
api_resource: _descriptor.FieldDescriptor
API_ONLY_FIELD_NUMBER: _ClassVar[int]
api_only: _descriptor.FieldDescriptor
GORM_JSON_FIELD_NUMBER: _ClassVar[int]
gorm_json: _descriptor.FieldDescriptor
SHOW_IF_ZERO_FIELD_NUMBER: _ClassVar[int]
show_if_zero: _descriptor.FieldDescriptor
GORM_INDEX_FIELD_NUMBER: _ClassVar[int]
gorm_index: _descriptor.FieldDescriptor
GORM_UNIQUE_INDEX_FIELD_NUMBER: _ClassVar[int]
gorm_unique_index: _descriptor.FieldDescriptor
GORM_UNIQUE_NAMED_INDEX_FIELD_NUMBER: _ClassVar[int]
gorm_unique_named_index: _descriptor.FieldDescriptor

class ApiResource(_message.Message):
    __slots__ = ("parent_type", "skip_gorm", "has_db_only_fields")
    PARENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SKIP_GORM_FIELD_NUMBER: _ClassVar[int]
    HAS_DB_ONLY_FIELDS_FIELD_NUMBER: _ClassVar[int]
    parent_type: str
    skip_gorm: bool
    has_db_only_fields: bool
    def __init__(self, parent_type: _Optional[str] = ..., skip_gorm: bool = ..., has_db_only_fields: bool = ...) -> None: ...
