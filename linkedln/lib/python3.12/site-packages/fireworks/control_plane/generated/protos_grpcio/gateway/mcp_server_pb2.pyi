from ..buf.validate import validate_pb2 as _validate_pb2
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

class McpServer(_message.Message):
    __slots__ = ("name", "display_name", "description", "create_time", "update_time", "endpoint_url", "api_key_secret", "simulated", "state", "status", "remote_hosted", "annotations", "public", "authentication_type", "featured")
    class AuthenticationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AUTHENTICATION_TYPE_UNSPECIFIED: _ClassVar[McpServer.AuthenticationType]
        OPEN: _ClassVar[McpServer.AuthenticationType]
        API_KEY: _ClassVar[McpServer.AuthenticationType]
        OAUTH2: _ClassVar[McpServer.AuthenticationType]
        BEARER_TOKEN: _ClassVar[McpServer.AuthenticationType]
    AUTHENTICATION_TYPE_UNSPECIFIED: McpServer.AuthenticationType
    OPEN: McpServer.AuthenticationType
    API_KEY: McpServer.AuthenticationType
    OAUTH2: McpServer.AuthenticationType
    BEARER_TOKEN: McpServer.AuthenticationType
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[McpServer.State]
        CREATING: _ClassVar[McpServer.State]
        ACTIVE: _ClassVar[McpServer.State]
        FAILED: _ClassVar[McpServer.State]
        DELETING: _ClassVar[McpServer.State]
    STATE_UNSPECIFIED: McpServer.State
    CREATING: McpServer.State
    ACTIVE: McpServer.State
    FAILED: McpServer.State
    DELETING: McpServer.State
    class AnnotationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_URL_FIELD_NUMBER: _ClassVar[int]
    API_KEY_SECRET_FIELD_NUMBER: _ClassVar[int]
    SIMULATED_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REMOTE_HOSTED_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    FEATURED_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    endpoint_url: str
    api_key_secret: str
    simulated: bool
    state: McpServer.State
    status: _status_pb2.Status
    remote_hosted: bool
    annotations: _containers.ScalarMap[str, str]
    public: bool
    authentication_type: McpServer.AuthenticationType
    featured: bool
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., endpoint_url: _Optional[str] = ..., api_key_secret: _Optional[str] = ..., simulated: bool = ..., state: _Optional[_Union[McpServer.State, str]] = ..., status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., remote_hosted: bool = ..., annotations: _Optional[_Mapping[str, str]] = ..., public: bool = ..., authentication_type: _Optional[_Union[McpServer.AuthenticationType, str]] = ..., featured: bool = ...) -> None: ...

class CreateMcpServerRequest(_message.Message):
    __slots__ = ("parent", "mcp_server", "mcp_server_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MCP_SERVER_FIELD_NUMBER: _ClassVar[int]
    MCP_SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    mcp_server: McpServer
    mcp_server_id: str
    def __init__(self, parent: _Optional[str] = ..., mcp_server: _Optional[_Union[McpServer, _Mapping]] = ..., mcp_server_id: _Optional[str] = ...) -> None: ...

class GetMcpServerRequest(_message.Message):
    __slots__ = ("name", "read_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListMcpServersRequest(_message.Message):
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

class ListMcpServersResponse(_message.Message):
    __slots__ = ("mcp_servers", "next_page_token", "total_size")
    MCP_SERVERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    mcp_servers: _containers.RepeatedCompositeFieldContainer[McpServer]
    next_page_token: str
    total_size: int
    def __init__(self, mcp_servers: _Optional[_Iterable[_Union[McpServer, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class UpdateMcpServerRequest(_message.Message):
    __slots__ = ("mcp_server", "update_mask")
    MCP_SERVER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    mcp_server: McpServer
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, mcp_server: _Optional[_Union[McpServer, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteMcpServerRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
