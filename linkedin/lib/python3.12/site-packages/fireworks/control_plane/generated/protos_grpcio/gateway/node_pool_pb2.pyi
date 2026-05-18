from ..buf.validate import validate_pb2 as _validate_pb2
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

class NodePool(_message.Message):
    __slots__ = ("name", "display_name", "create_time", "min_node_count", "max_node_count", "overprovision_node_count", "eks_node_pool", "fake_node_pool", "annotations", "state", "status", "node_pool_stats", "update_time")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[NodePool.State]
        CREATING: _ClassVar[NodePool.State]
        READY: _ClassVar[NodePool.State]
        DELETING: _ClassVar[NodePool.State]
        FAILED: _ClassVar[NodePool.State]
    STATE_UNSPECIFIED: NodePool.State
    CREATING: NodePool.State
    READY: NodePool.State
    DELETING: NodePool.State
    FAILED: NodePool.State
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
    MIN_NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    OVERPROVISION_NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    EKS_NODE_POOL_FIELD_NUMBER: _ClassVar[int]
    FAKE_NODE_POOL_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NODE_POOL_STATS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    create_time: _timestamp_pb2.Timestamp
    min_node_count: int
    max_node_count: int
    overprovision_node_count: int
    eks_node_pool: EksNodePool
    fake_node_pool: FakeNodePool
    annotations: _containers.ScalarMap[str, str]
    state: NodePool.State
    status: _status_pb2.Status
    node_pool_stats: NodePoolStats
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., min_node_count: _Optional[int] = ..., max_node_count: _Optional[int] = ..., overprovision_node_count: _Optional[int] = ..., eks_node_pool: _Optional[_Union[EksNodePool, _Mapping]] = ..., fake_node_pool: _Optional[_Union[FakeNodePool, _Mapping]] = ..., annotations: _Optional[_Mapping[str, str]] = ..., state: _Optional[_Union[NodePool.State, str]] = ..., status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., node_pool_stats: _Optional[_Union[NodePoolStats, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class EksNodePool(_message.Message):
    __slots__ = ("node_role", "instance_type", "spot", "node_group_name", "subnet_ids", "zone", "placement_group", "launch_template")
    NODE_ROLE_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SPOT_FIELD_NUMBER: _ClassVar[int]
    NODE_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    SUBNET_IDS_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    PLACEMENT_GROUP_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    node_role: str
    instance_type: str
    spot: bool
    node_group_name: str
    subnet_ids: _containers.RepeatedScalarFieldContainer[str]
    zone: str
    placement_group: str
    launch_template: str
    def __init__(self, node_role: _Optional[str] = ..., instance_type: _Optional[str] = ..., spot: bool = ..., node_group_name: _Optional[str] = ..., subnet_ids: _Optional[_Iterable[str]] = ..., zone: _Optional[str] = ..., placement_group: _Optional[str] = ..., launch_template: _Optional[str] = ...) -> None: ...

class FakeNodePool(_message.Message):
    __slots__ = ("machine_type", "num_nodes", "service_account")
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    NUM_NODES_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    machine_type: str
    num_nodes: int
    service_account: str
    def __init__(self, machine_type: _Optional[str] = ..., num_nodes: _Optional[int] = ..., service_account: _Optional[str] = ...) -> None: ...

class NodePoolStats(_message.Message):
    __slots__ = ("node_count", "ranks_per_node", "environment_count", "environment_ranks", "batch_job_count", "batch_job_ranks")
    class BatchJobCountEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class BatchJobRanksEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    RANKS_PER_NODE_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_RANKS_FIELD_NUMBER: _ClassVar[int]
    BATCH_JOB_COUNT_FIELD_NUMBER: _ClassVar[int]
    BATCH_JOB_RANKS_FIELD_NUMBER: _ClassVar[int]
    node_count: int
    ranks_per_node: int
    environment_count: int
    environment_ranks: int
    batch_job_count: _containers.ScalarMap[str, int]
    batch_job_ranks: _containers.ScalarMap[str, int]
    def __init__(self, node_count: _Optional[int] = ..., ranks_per_node: _Optional[int] = ..., environment_count: _Optional[int] = ..., environment_ranks: _Optional[int] = ..., batch_job_count: _Optional[_Mapping[str, int]] = ..., batch_job_ranks: _Optional[_Mapping[str, int]] = ...) -> None: ...

class CreateNodePoolRequest(_message.Message):
    __slots__ = ("parent", "node_pool", "node_pool_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NODE_POOL_FIELD_NUMBER: _ClassVar[int]
    NODE_POOL_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    node_pool: NodePool
    node_pool_id: str
    def __init__(self, parent: _Optional[str] = ..., node_pool: _Optional[_Union[NodePool, _Mapping]] = ..., node_pool_id: _Optional[str] = ...) -> None: ...

class GetNodePoolRequest(_message.Message):
    __slots__ = ("name", "read_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListNodePoolsRequest(_message.Message):
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

class ListNodePoolsResponse(_message.Message):
    __slots__ = ("node_pools", "next_page_token", "total_size")
    NODE_POOLS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    node_pools: _containers.RepeatedCompositeFieldContainer[NodePool]
    next_page_token: str
    total_size: int
    def __init__(self, node_pools: _Optional[_Iterable[_Union[NodePool, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class UpdateNodePoolRequest(_message.Message):
    __slots__ = ("node_pool", "update_mask")
    NODE_POOL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    node_pool: NodePool
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, node_pool: _Optional[_Union[NodePool, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteNodePoolRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class BatchDeleteNodePoolsRequest(_message.Message):
    __slots__ = ("parent", "names")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAMES_FIELD_NUMBER: _ClassVar[int]
    parent: str
    names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, parent: _Optional[str] = ..., names: _Optional[_Iterable[str]] = ...) -> None: ...

class GetNodePoolStatsRequest(_message.Message):
    __slots__ = ("name", "read_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...
