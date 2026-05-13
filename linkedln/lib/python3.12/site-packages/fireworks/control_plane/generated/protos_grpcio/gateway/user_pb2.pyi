from . import options_pb2 as _options_pb2
from . import status_pb2 as _status_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.api import visibility_pb2 as _visibility_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = ("name", "display_name", "first_name", "last_name", "stated_role", "service_account", "create_time", "role", "email", "state", "status", "update_time")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[User.State]
        CREATING: _ClassVar[User.State]
        READY: _ClassVar[User.State]
        UPDATING: _ClassVar[User.State]
        DELETING: _ClassVar[User.State]
    STATE_UNSPECIFIED: User.State
    CREATING: User.State
    READY: User.State
    UPDATING: User.State
    DELETING: User.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    STATED_ROLE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    first_name: str
    last_name: str
    stated_role: str
    service_account: bool
    create_time: _timestamp_pb2.Timestamp
    role: str
    email: str
    state: User.State
    status: _status_pb2.Status
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., stated_role: _Optional[str] = ..., service_account: bool = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., role: _Optional[str] = ..., email: _Optional[str] = ..., state: _Optional[_Union[User.State, str]] = ..., status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateUserRequest(_message.Message):
    __slots__ = ("parent", "user", "user_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    user: User
    user_id: str
    def __init__(self, parent: _Optional[str] = ..., user: _Optional[_Union[User, _Mapping]] = ..., user_id: _Optional[str] = ...) -> None: ...

class GetUserRequest(_message.Message):
    __slots__ = ("name", "read_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListUsersRequest(_message.Message):
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

class ListUsersResponse(_message.Message):
    __slots__ = ("users", "next_page_token", "total_size")
    USERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[User]
    next_page_token: str
    total_size: int
    def __init__(self, users: _Optional[_Iterable[_Union[User, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class UpdateUserRequest(_message.Message):
    __slots__ = ("user", "update_mask")
    USER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    user: User
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteUserRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
