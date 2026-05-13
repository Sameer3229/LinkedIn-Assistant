from . import options_pb2 as _options_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FeatureFlag(_message.Message):
    __slots__ = ("name", "value", "create_time")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    create_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateFeatureFlagRequest(_message.Message):
    __slots__ = ("parent", "feature_flag", "feature_flag_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FEATURE_FLAG_FIELD_NUMBER: _ClassVar[int]
    FEATURE_FLAG_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    feature_flag: FeatureFlag
    feature_flag_id: str
    def __init__(self, parent: _Optional[str] = ..., feature_flag: _Optional[_Union[FeatureFlag, _Mapping]] = ..., feature_flag_id: _Optional[str] = ...) -> None: ...

class GetFeatureFlagRequest(_message.Message):
    __slots__ = ("name", "read_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListFeatureFlagsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "order_by", "filter", "read_mask")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    order_by: str
    filter: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., order_by: _Optional[str] = ..., filter: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListFeatureFlagsResponse(_message.Message):
    __slots__ = ("feature_flags", "next_page_token", "total_size")
    FEATURE_FLAGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    feature_flags: _containers.RepeatedCompositeFieldContainer[FeatureFlag]
    next_page_token: str
    total_size: int
    def __init__(self, feature_flags: _Optional[_Iterable[_Union[FeatureFlag, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class UpdateFeatureFlagRequest(_message.Message):
    __slots__ = ("feature_flag", "update_mask")
    FEATURE_FLAG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    feature_flag: FeatureFlag
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, feature_flag: _Optional[_Union[FeatureFlag, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteFeatureFlagRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
