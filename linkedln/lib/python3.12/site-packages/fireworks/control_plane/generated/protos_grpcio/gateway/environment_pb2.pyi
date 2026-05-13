from . import options_pb2 as _options_pb2
from . import status_pb2 as _status_pb2
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

class Environment(_message.Message):
    __slots__ = ("name", "display_name", "create_time", "created_by", "state", "status", "connection", "base_image_ref", "image_ref", "snapshot_image_ref", "shared", "annotations", "update_time")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Environment.State]
        CREATING: _ClassVar[Environment.State]
        DISCONNECTED: _ClassVar[Environment.State]
        CONNECTING: _ClassVar[Environment.State]
        CONNECTED: _ClassVar[Environment.State]
        DISCONNECTING: _ClassVar[Environment.State]
        RECONNECTING: _ClassVar[Environment.State]
        DELETING: _ClassVar[Environment.State]
    STATE_UNSPECIFIED: Environment.State
    CREATING: Environment.State
    DISCONNECTED: Environment.State
    CONNECTING: Environment.State
    CONNECTED: Environment.State
    DISCONNECTING: Environment.State
    RECONNECTING: Environment.State
    DELETING: Environment.State
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
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    BASE_IMAGE_REF_FIELD_NUMBER: _ClassVar[int]
    IMAGE_REF_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_IMAGE_REF_FIELD_NUMBER: _ClassVar[int]
    SHARED_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    create_time: _timestamp_pb2.Timestamp
    created_by: str
    state: Environment.State
    status: _status_pb2.Status
    connection: EnvironmentConnection
    base_image_ref: str
    image_ref: str
    snapshot_image_ref: str
    shared: bool
    annotations: _containers.ScalarMap[str, str]
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[str] = ..., state: _Optional[_Union[Environment.State, str]] = ..., status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., connection: _Optional[_Union[EnvironmentConnection, _Mapping]] = ..., base_image_ref: _Optional[str] = ..., image_ref: _Optional[str] = ..., snapshot_image_ref: _Optional[str] = ..., shared: bool = ..., annotations: _Optional[_Mapping[str, str]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class EnvironmentConnection(_message.Message):
    __slots__ = ("node_pool_id", "num_ranks", "role", "zone", "use_local_storage")
    NODE_POOL_ID_FIELD_NUMBER: _ClassVar[int]
    NUM_RANKS_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    USE_LOCAL_STORAGE_FIELD_NUMBER: _ClassVar[int]
    node_pool_id: str
    num_ranks: int
    role: str
    zone: str
    use_local_storage: bool
    def __init__(self, node_pool_id: _Optional[str] = ..., num_ranks: _Optional[int] = ..., role: _Optional[str] = ..., zone: _Optional[str] = ..., use_local_storage: bool = ...) -> None: ...

class CreateEnvironmentRequest(_message.Message):
    __slots__ = ("parent", "environment", "environment_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    environment: Environment
    environment_id: str
    def __init__(self, parent: _Optional[str] = ..., environment: _Optional[_Union[Environment, _Mapping]] = ..., environment_id: _Optional[str] = ...) -> None: ...

class GetEnvironmentRequest(_message.Message):
    __slots__ = ("name", "read_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListEnvironmentsRequest(_message.Message):
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

class ListEnvironmentsResponse(_message.Message):
    __slots__ = ("environments", "next_page_token", "total_size")
    ENVIRONMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    environments: _containers.RepeatedCompositeFieldContainer[Environment]
    next_page_token: str
    total_size: int
    def __init__(self, environments: _Optional[_Iterable[_Union[Environment, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class UpdateEnvironmentRequest(_message.Message):
    __slots__ = ("environment", "update_mask")
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    environment: Environment
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, environment: _Optional[_Union[Environment, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteEnvironmentRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class BatchDeleteEnvironmentsRequest(_message.Message):
    __slots__ = ("parent", "names")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAMES_FIELD_NUMBER: _ClassVar[int]
    parent: str
    names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, parent: _Optional[str] = ..., names: _Optional[_Iterable[str]] = ...) -> None: ...

class ConnectEnvironmentRequest(_message.Message):
    __slots__ = ("name", "connection", "vscode_version")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    VSCODE_VERSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    connection: EnvironmentConnection
    vscode_version: str
    def __init__(self, name: _Optional[str] = ..., connection: _Optional[_Union[EnvironmentConnection, _Mapping]] = ..., vscode_version: _Optional[str] = ...) -> None: ...

class DisconnectEnvironmentRequest(_message.Message):
    __slots__ = ("name", "force", "reset_snapshots")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    RESET_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool
    reset_snapshots: bool
    def __init__(self, name: _Optional[str] = ..., force: bool = ..., reset_snapshots: bool = ...) -> None: ...
