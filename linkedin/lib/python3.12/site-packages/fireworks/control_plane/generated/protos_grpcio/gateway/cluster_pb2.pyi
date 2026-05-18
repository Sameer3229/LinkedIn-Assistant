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

class Cluster(_message.Message):
    __slots__ = ("name", "display_name", "create_time", "eks_cluster", "fake_cluster", "annotations", "state", "status", "is_dlde", "metering_key", "update_time")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Cluster.State]
        CREATING: _ClassVar[Cluster.State]
        READY: _ClassVar[Cluster.State]
        DELETING: _ClassVar[Cluster.State]
        FAILED: _ClassVar[Cluster.State]
    STATE_UNSPECIFIED: Cluster.State
    CREATING: Cluster.State
    READY: Cluster.State
    DELETING: Cluster.State
    FAILED: Cluster.State
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
    EKS_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    FAKE_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    IS_DLDE_FIELD_NUMBER: _ClassVar[int]
    METERING_KEY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    create_time: _timestamp_pb2.Timestamp
    eks_cluster: EksCluster
    fake_cluster: FakeCluster
    annotations: _containers.ScalarMap[str, str]
    state: Cluster.State
    status: _status_pb2.Status
    is_dlde: bool
    metering_key: str
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., eks_cluster: _Optional[_Union[EksCluster, _Mapping]] = ..., fake_cluster: _Optional[_Union[FakeCluster, _Mapping]] = ..., annotations: _Optional[_Mapping[str, str]] = ..., state: _Optional[_Union[Cluster.State, str]] = ..., status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., is_dlde: bool = ..., metering_key: _Optional[str] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class EksCluster(_message.Message):
    __slots__ = ("aws_account_id", "fireworks_manager_role", "region", "cluster_role", "cluster_autoscaler_role", "system_node_role", "subnet_ids", "cluster_name", "repository_name", "storage_bucket_name", "node_security_group", "metric_writer_role", "load_balancer_controller_role", "workload_identity_pool_provider_id", "inference_role")
    AWS_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    FIREWORKS_MANAGER_ROLE_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ROLE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_AUTOSCALER_ROLE_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_NODE_ROLE_FIELD_NUMBER: _ClassVar[int]
    SUBNET_IDS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    REPOSITORY_NAME_FIELD_NUMBER: _ClassVar[int]
    STORAGE_BUCKET_NAME_FIELD_NUMBER: _ClassVar[int]
    NODE_SECURITY_GROUP_FIELD_NUMBER: _ClassVar[int]
    METRIC_WRITER_ROLE_FIELD_NUMBER: _ClassVar[int]
    LOAD_BALANCER_CONTROLLER_ROLE_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_IDENTITY_POOL_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    INFERENCE_ROLE_FIELD_NUMBER: _ClassVar[int]
    aws_account_id: str
    fireworks_manager_role: str
    region: str
    cluster_role: str
    cluster_autoscaler_role: str
    system_node_role: str
    subnet_ids: _containers.RepeatedScalarFieldContainer[str]
    cluster_name: str
    repository_name: str
    storage_bucket_name: str
    node_security_group: str
    metric_writer_role: str
    load_balancer_controller_role: str
    workload_identity_pool_provider_id: str
    inference_role: str
    def __init__(self, aws_account_id: _Optional[str] = ..., fireworks_manager_role: _Optional[str] = ..., region: _Optional[str] = ..., cluster_role: _Optional[str] = ..., cluster_autoscaler_role: _Optional[str] = ..., system_node_role: _Optional[str] = ..., subnet_ids: _Optional[_Iterable[str]] = ..., cluster_name: _Optional[str] = ..., repository_name: _Optional[str] = ..., storage_bucket_name: _Optional[str] = ..., node_security_group: _Optional[str] = ..., metric_writer_role: _Optional[str] = ..., load_balancer_controller_role: _Optional[str] = ..., workload_identity_pool_provider_id: _Optional[str] = ..., inference_role: _Optional[str] = ...) -> None: ...

class FakeCluster(_message.Message):
    __slots__ = ("project_id", "location", "cluster_name")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    location: str
    cluster_name: str
    def __init__(self, project_id: _Optional[str] = ..., location: _Optional[str] = ..., cluster_name: _Optional[str] = ...) -> None: ...

class CreateClusterRequest(_message.Message):
    __slots__ = ("parent", "cluster", "cluster_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    cluster: Cluster
    cluster_id: str
    def __init__(self, parent: _Optional[str] = ..., cluster: _Optional[_Union[Cluster, _Mapping]] = ..., cluster_id: _Optional[str] = ...) -> None: ...

class GetClusterRequest(_message.Message):
    __slots__ = ("name", "read_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListClustersRequest(_message.Message):
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

class ListClustersResponse(_message.Message):
    __slots__ = ("clusters", "next_page_token", "total_size")
    CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    clusters: _containers.RepeatedCompositeFieldContainer[Cluster]
    next_page_token: str
    total_size: int
    def __init__(self, clusters: _Optional[_Iterable[_Union[Cluster, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class UpdateClusterRequest(_message.Message):
    __slots__ = ("cluster", "update_mask")
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    cluster: Cluster
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, cluster: _Optional[_Union[Cluster, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteClusterRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetClusterConnectionInfoRequest(_message.Message):
    __slots__ = ("name", "read_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ClusterConnectionInfo(_message.Message):
    __slots__ = ("endpoint", "ca_data")
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    CA_DATA_FIELD_NUMBER: _ClassVar[int]
    endpoint: str
    ca_data: str
    def __init__(self, endpoint: _Optional[str] = ..., ca_data: _Optional[str] = ...) -> None: ...
