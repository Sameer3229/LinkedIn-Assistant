from . import options_pb2 as _options_pb2
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

class Quota(_message.Message):
    __slots__ = ("name", "value", "max_value", "usage", "update_time", "create_time")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: int
    max_value: int
    usage: float
    update_time: _timestamp_pb2.Timestamp
    create_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., value: _Optional[int] = ..., max_value: _Optional[int] = ..., usage: _Optional[float] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetQuotaRequest(_message.Message):
    __slots__ = ("name", "read_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListQuotasRequest(_message.Message):
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

class UpdateQuotaRequest(_message.Message):
    __slots__ = ("quota", "update_mask", "allow_missing")
    QUOTA_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    quota: Quota
    update_mask: _field_mask_pb2.FieldMask
    allow_missing: bool
    def __init__(self, quota: _Optional[_Union[Quota, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., allow_missing: bool = ...) -> None: ...

class ListQuotasResponse(_message.Message):
    __slots__ = ("quotas", "next_page_token", "total_size")
    QUOTAS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    quotas: _containers.RepeatedCompositeFieldContainer[Quota]
    next_page_token: str
    total_size: int
    def __init__(self, quotas: _Optional[_Iterable[_Union[Quota, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...
