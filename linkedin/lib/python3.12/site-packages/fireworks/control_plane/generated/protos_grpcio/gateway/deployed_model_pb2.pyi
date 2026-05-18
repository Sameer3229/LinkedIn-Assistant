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

class DeployedModel(_message.Message):
    __slots__ = ("name", "display_name", "description", "create_time", "created_by", "model", "deployment", "default", "state", "serverless", "status", "public", "update_time", "load_balancer_name", "load_balancer_replica_capacity", "is_load_balancer_sticky_session")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[DeployedModel.State]
        UNDEPLOYING: _ClassVar[DeployedModel.State]
        DEPLOYING: _ClassVar[DeployedModel.State]
        DEPLOYED: _ClassVar[DeployedModel.State]
        UPDATING: _ClassVar[DeployedModel.State]
    STATE_UNSPECIFIED: DeployedModel.State
    UNDEPLOYING: DeployedModel.State
    DEPLOYING: DeployedModel.State
    DEPLOYED: DeployedModel.State
    UPDATING: DeployedModel.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SERVERLESS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LOAD_BALANCER_NAME_FIELD_NUMBER: _ClassVar[int]
    LOAD_BALANCER_REPLICA_CAPACITY_FIELD_NUMBER: _ClassVar[int]
    IS_LOAD_BALANCER_STICKY_SESSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    created_by: str
    model: str
    deployment: str
    default: bool
    state: DeployedModel.State
    serverless: bool
    status: _status_pb2.Status
    public: bool
    update_time: _timestamp_pb2.Timestamp
    load_balancer_name: str
    load_balancer_replica_capacity: float
    is_load_balancer_sticky_session: bool
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[str] = ..., model: _Optional[str] = ..., deployment: _Optional[str] = ..., default: bool = ..., state: _Optional[_Union[DeployedModel.State, str]] = ..., serverless: bool = ..., status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., public: bool = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., load_balancer_name: _Optional[str] = ..., load_balancer_replica_capacity: _Optional[float] = ..., is_load_balancer_sticky_session: bool = ...) -> None: ...

class DeployedModelRef(_message.Message):
    __slots__ = ("name", "deployment", "state", "default", "public")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FIELD_NUMBER: _ClassVar[int]
    name: str
    deployment: str
    state: DeployedModel.State
    default: bool
    public: bool
    def __init__(self, name: _Optional[str] = ..., deployment: _Optional[str] = ..., state: _Optional[_Union[DeployedModel.State, str]] = ..., default: bool = ..., public: bool = ...) -> None: ...

class CreateDeployedModelRequest(_message.Message):
    __slots__ = ("parent", "deployed_model")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DEPLOYED_MODEL_FIELD_NUMBER: _ClassVar[int]
    parent: str
    deployed_model: DeployedModel
    def __init__(self, parent: _Optional[str] = ..., deployed_model: _Optional[_Union[DeployedModel, _Mapping]] = ...) -> None: ...

class DeleteDeployedModelRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetDeployedModelRequest(_message.Message):
    __slots__ = ("name", "read_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListDeployedModelsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by", "read_mask", "show_internal")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    SHOW_INTERNAL_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    read_mask: _field_mask_pb2.FieldMask
    show_internal: bool
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., show_internal: bool = ...) -> None: ...

class ListDeployedModelsResponse(_message.Message):
    __slots__ = ("deployed_models", "next_page_token", "total_size")
    DEPLOYED_MODELS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    deployed_models: _containers.RepeatedCompositeFieldContainer[DeployedModel]
    next_page_token: str
    total_size: int
    def __init__(self, deployed_models: _Optional[_Iterable[_Union[DeployedModel, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class UpdateDeployedModelRequest(_message.Message):
    __slots__ = ("deployed_model", "update_mask")
    DEPLOYED_MODEL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    deployed_model: DeployedModel
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, deployed_model: _Optional[_Union[DeployedModel, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...
