from ..buf.validate import validate_pb2 as _validate_pb2
from . import deployment_pb2 as _deployment_pb2
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

class Workload(_message.Message):
    __slots__ = ("name", "display_name", "description", "create_time", "update_time", "expire_time", "purge_time", "delete_time", "created_by", "state", "status", "annotations", "placement", "min_replica_count", "max_replica_count", "desired_replica_count", "autoscaling_policy", "workload_shape", "disable_accounting", "for_training")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Workload.State]
        CREATING: _ClassVar[Workload.State]
        READY: _ClassVar[Workload.State]
        DELETING: _ClassVar[Workload.State]
        FAILED: _ClassVar[Workload.State]
        UPDATING: _ClassVar[Workload.State]
        DELETED: _ClassVar[Workload.State]
    STATE_UNSPECIFIED: Workload.State
    CREATING: Workload.State
    READY: Workload.State
    DELETING: Workload.State
    FAILED: Workload.State
    UPDATING: Workload.State
    DELETED: Workload.State
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
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    PURGE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    PLACEMENT_FIELD_NUMBER: _ClassVar[int]
    MIN_REPLICA_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_REPLICA_COUNT_FIELD_NUMBER: _ClassVar[int]
    DESIRED_REPLICA_COUNT_FIELD_NUMBER: _ClassVar[int]
    AUTOSCALING_POLICY_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_SHAPE_FIELD_NUMBER: _ClassVar[int]
    DISABLE_ACCOUNTING_FIELD_NUMBER: _ClassVar[int]
    FOR_TRAINING_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    expire_time: _timestamp_pb2.Timestamp
    purge_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    created_by: str
    state: Workload.State
    status: _status_pb2.Status
    annotations: _containers.ScalarMap[str, str]
    placement: _deployment_pb2.Placement
    min_replica_count: int
    max_replica_count: int
    desired_replica_count: int
    autoscaling_policy: _deployment_pb2.AutoscalingPolicy
    workload_shape: str
    disable_accounting: bool
    for_training: bool
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., purge_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[str] = ..., state: _Optional[_Union[Workload.State, str]] = ..., status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., annotations: _Optional[_Mapping[str, str]] = ..., placement: _Optional[_Union[_deployment_pb2.Placement, _Mapping]] = ..., min_replica_count: _Optional[int] = ..., max_replica_count: _Optional[int] = ..., desired_replica_count: _Optional[int] = ..., autoscaling_policy: _Optional[_Union[_deployment_pb2.AutoscalingPolicy, _Mapping]] = ..., workload_shape: _Optional[str] = ..., disable_accounting: bool = ..., for_training: bool = ...) -> None: ...

class CreateWorkloadRequest(_message.Message):
    __slots__ = ("parent", "workload", "workload_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    workload: Workload
    workload_id: str
    def __init__(self, parent: _Optional[str] = ..., workload: _Optional[_Union[Workload, _Mapping]] = ..., workload_id: _Optional[str] = ...) -> None: ...

class GetWorkloadRequest(_message.Message):
    __slots__ = ("name", "read_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListWorkloadsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by", "show_deleted", "show_internal", "read_mask")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    SHOW_DELETED_FIELD_NUMBER: _ClassVar[int]
    SHOW_INTERNAL_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    show_deleted: bool
    show_internal: bool
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ..., show_deleted: bool = ..., show_internal: bool = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListWorkloadsResponse(_message.Message):
    __slots__ = ("workloads", "next_page_token", "total_size")
    WORKLOADS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    workloads: _containers.RepeatedCompositeFieldContainer[Workload]
    next_page_token: str
    total_size: int
    def __init__(self, workloads: _Optional[_Iterable[_Union[Workload, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class UpdateWorkloadRequest(_message.Message):
    __slots__ = ("workload", "update_mask")
    WORKLOAD_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    workload: Workload
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, workload: _Optional[_Union[Workload, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteWorkloadRequest(_message.Message):
    __slots__ = ("name", "hard", "ignore_checks")
    NAME_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    IGNORE_CHECKS_FIELD_NUMBER: _ClassVar[int]
    name: str
    hard: bool
    ignore_checks: bool
    def __init__(self, name: _Optional[str] = ..., hard: bool = ..., ignore_checks: bool = ...) -> None: ...
