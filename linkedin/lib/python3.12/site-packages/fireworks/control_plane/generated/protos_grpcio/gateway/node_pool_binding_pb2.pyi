from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NodePoolBinding(_message.Message):
    __slots__ = ("account_id", "cluster_id", "node_pool_id", "create_time", "principal")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_POOL_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    cluster_id: str
    node_pool_id: str
    create_time: _timestamp_pb2.Timestamp
    principal: str
    def __init__(self, account_id: _Optional[str] = ..., cluster_id: _Optional[str] = ..., node_pool_id: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., principal: _Optional[str] = ...) -> None: ...

class CreateNodePoolBindingRequest(_message.Message):
    __slots__ = ("parent", "node_pool_binding")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NODE_POOL_BINDING_FIELD_NUMBER: _ClassVar[int]
    parent: str
    node_pool_binding: NodePoolBinding
    def __init__(self, parent: _Optional[str] = ..., node_pool_binding: _Optional[_Union[NodePoolBinding, _Mapping]] = ...) -> None: ...

class ListNodePoolBindingsRequest(_message.Message):
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

class ListNodePoolBindingsResponse(_message.Message):
    __slots__ = ("node_pool_bindings", "next_page_token", "total_size")
    NODE_POOL_BINDINGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    node_pool_bindings: _containers.RepeatedCompositeFieldContainer[NodePoolBinding]
    next_page_token: str
    total_size: int
    def __init__(self, node_pool_bindings: _Optional[_Iterable[_Union[NodePoolBinding, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class DeleteNodePoolBindingRequest(_message.Message):
    __slots__ = ("node_pool_binding",)
    NODE_POOL_BINDING_FIELD_NUMBER: _ClassVar[int]
    node_pool_binding: NodePoolBinding
    def __init__(self, node_pool_binding: _Optional[_Union[NodePoolBinding, _Mapping]] = ...) -> None: ...
