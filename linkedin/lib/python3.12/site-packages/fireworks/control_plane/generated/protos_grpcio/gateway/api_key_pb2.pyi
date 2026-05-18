from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ApiKey(_message.Message):
    __slots__ = ("key_id", "display_name", "key", "create_time", "secure", "email", "prefix")
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SECURE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    key_id: str
    display_name: str
    key: str
    create_time: _timestamp_pb2.Timestamp
    secure: bool
    email: str
    prefix: str
    def __init__(self, key_id: _Optional[str] = ..., display_name: _Optional[str] = ..., key: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., secure: bool = ..., email: _Optional[str] = ..., prefix: _Optional[str] = ...) -> None: ...

class CreateApiKeyRequest(_message.Message):
    __slots__ = ("parent", "api_key")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    api_key: ApiKey
    def __init__(self, parent: _Optional[str] = ..., api_key: _Optional[_Union[ApiKey, _Mapping]] = ...) -> None: ...

class ListApiKeysRequest(_message.Message):
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

class ListApiKeysResponse(_message.Message):
    __slots__ = ("api_keys", "next_page_token", "total_size")
    API_KEYS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    api_keys: _containers.RepeatedCompositeFieldContainer[ApiKey]
    next_page_token: str
    total_size: int
    def __init__(self, api_keys: _Optional[_Iterable[_Union[ApiKey, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class DeleteApiKeyRequest(_message.Message):
    __slots__ = ("parent", "key_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    key_id: str
    def __init__(self, parent: _Optional[str] = ..., key_id: _Optional[str] = ...) -> None: ...

class GetInternalApiKeyRequest(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    def __init__(self, parent: _Optional[str] = ...) -> None: ...

class UpdateApiKeyAccountRequest(_message.Message):
    __slots__ = ("old_account", "new_account")
    OLD_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    NEW_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    old_account: str
    new_account: str
    def __init__(self, old_account: _Optional[str] = ..., new_account: _Optional[str] = ...) -> None: ...
