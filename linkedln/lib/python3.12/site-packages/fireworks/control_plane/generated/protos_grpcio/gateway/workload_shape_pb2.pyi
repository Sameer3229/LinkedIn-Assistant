from ..buf.validate import validate_pb2 as _validate_pb2
from . import deployment_pb2 as _deployment_pb2
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

class WorkloadShape(_message.Message):
    __slots__ = ("name", "display_name", "description", "create_time", "update_time", "created_by", "annotations", "base_model", "accelerator_count", "accelerator_type", "precision", "world_size", "generator_count", "disaggregated_prefill_count", "disaggregated_prefill_world_size", "max_batch_size", "enable_addons", "draft_token_count", "draft_model", "ngram_speculation_length", "max_lora_batch_size", "kv_cache_memory_pct", "enable_session_affinity", "image_tag", "num_lora_device_cached", "extra_args", "max_context_length", "extra_values", "engine")
    class AnnotationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class ExtraValuesEntry(_message.Message):
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
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    BASE_MODEL_FIELD_NUMBER: _ClassVar[int]
    ACCELERATOR_COUNT_FIELD_NUMBER: _ClassVar[int]
    ACCELERATOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRECISION_FIELD_NUMBER: _ClassVar[int]
    WORLD_SIZE_FIELD_NUMBER: _ClassVar[int]
    GENERATOR_COUNT_FIELD_NUMBER: _ClassVar[int]
    DISAGGREGATED_PREFILL_COUNT_FIELD_NUMBER: _ClassVar[int]
    DISAGGREGATED_PREFILL_WORLD_SIZE_FIELD_NUMBER: _ClassVar[int]
    MAX_BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_ADDONS_FIELD_NUMBER: _ClassVar[int]
    DRAFT_TOKEN_COUNT_FIELD_NUMBER: _ClassVar[int]
    DRAFT_MODEL_FIELD_NUMBER: _ClassVar[int]
    NGRAM_SPECULATION_LENGTH_FIELD_NUMBER: _ClassVar[int]
    MAX_LORA_BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    KV_CACHE_MEMORY_PCT_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SESSION_AFFINITY_FIELD_NUMBER: _ClassVar[int]
    IMAGE_TAG_FIELD_NUMBER: _ClassVar[int]
    NUM_LORA_DEVICE_CACHED_FIELD_NUMBER: _ClassVar[int]
    EXTRA_ARGS_FIELD_NUMBER: _ClassVar[int]
    MAX_CONTEXT_LENGTH_FIELD_NUMBER: _ClassVar[int]
    EXTRA_VALUES_FIELD_NUMBER: _ClassVar[int]
    ENGINE_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    created_by: str
    annotations: _containers.ScalarMap[str, str]
    base_model: str
    accelerator_count: int
    accelerator_type: _deployment_pb2.AcceleratorType
    precision: _deployment_pb2.Deployment.Precision
    world_size: int
    generator_count: int
    disaggregated_prefill_count: int
    disaggregated_prefill_world_size: int
    max_batch_size: int
    enable_addons: bool
    draft_token_count: int
    draft_model: str
    ngram_speculation_length: int
    max_lora_batch_size: int
    kv_cache_memory_pct: int
    enable_session_affinity: bool
    image_tag: str
    num_lora_device_cached: int
    extra_args: _containers.RepeatedScalarFieldContainer[str]
    max_context_length: int
    extra_values: _containers.ScalarMap[str, str]
    engine: _deployment_pb2.Deployment.Engine
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[str] = ..., annotations: _Optional[_Mapping[str, str]] = ..., base_model: _Optional[str] = ..., accelerator_count: _Optional[int] = ..., accelerator_type: _Optional[_Union[_deployment_pb2.AcceleratorType, str]] = ..., precision: _Optional[_Union[_deployment_pb2.Deployment.Precision, str]] = ..., world_size: _Optional[int] = ..., generator_count: _Optional[int] = ..., disaggregated_prefill_count: _Optional[int] = ..., disaggregated_prefill_world_size: _Optional[int] = ..., max_batch_size: _Optional[int] = ..., enable_addons: bool = ..., draft_token_count: _Optional[int] = ..., draft_model: _Optional[str] = ..., ngram_speculation_length: _Optional[int] = ..., max_lora_batch_size: _Optional[int] = ..., kv_cache_memory_pct: _Optional[int] = ..., enable_session_affinity: bool = ..., image_tag: _Optional[str] = ..., num_lora_device_cached: _Optional[int] = ..., extra_args: _Optional[_Iterable[str]] = ..., max_context_length: _Optional[int] = ..., extra_values: _Optional[_Mapping[str, str]] = ..., engine: _Optional[_Union[_deployment_pb2.Deployment.Engine, str]] = ...) -> None: ...

class CreateWorkloadShapeRequest(_message.Message):
    __slots__ = ("parent", "workload_shape", "workload_shape_id", "disable_size_validation")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_SHAPE_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_SHAPE_ID_FIELD_NUMBER: _ClassVar[int]
    DISABLE_SIZE_VALIDATION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    workload_shape: WorkloadShape
    workload_shape_id: str
    disable_size_validation: bool
    def __init__(self, parent: _Optional[str] = ..., workload_shape: _Optional[_Union[WorkloadShape, _Mapping]] = ..., workload_shape_id: _Optional[str] = ..., disable_size_validation: bool = ...) -> None: ...

class GetWorkloadShapeRequest(_message.Message):
    __slots__ = ("name", "read_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListWorkloadShapesRequest(_message.Message):
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

class ListWorkloadShapesResponse(_message.Message):
    __slots__ = ("workload_shapes", "next_page_token", "total_size")
    WORKLOAD_SHAPES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    workload_shapes: _containers.RepeatedCompositeFieldContainer[WorkloadShape]
    next_page_token: str
    total_size: int
    def __init__(self, workload_shapes: _Optional[_Iterable[_Union[WorkloadShape, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class UpdateWorkloadShapeRequest(_message.Message):
    __slots__ = ("workload_shape", "update_mask", "disable_size_validation")
    WORKLOAD_SHAPE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    DISABLE_SIZE_VALIDATION_FIELD_NUMBER: _ClassVar[int]
    workload_shape: WorkloadShape
    update_mask: _field_mask_pb2.FieldMask
    disable_size_validation: bool
    def __init__(self, workload_shape: _Optional[_Union[WorkloadShape, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., disable_size_validation: bool = ...) -> None: ...

class DeleteWorkloadShapeRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
