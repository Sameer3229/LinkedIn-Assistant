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

class DeploymentTemplate(_message.Message):
    __slots__ = ("name", "display_name", "description", "create_time", "created_by", "min_replica_count", "max_replica_count", "autoscaling_policy", "base_model", "accelerator_count", "accelerator_type", "world_size", "generator_count", "disaggregated_prefill_count", "disaggregated_prefill_world_size", "max_batch_size", "max_peft_batch_size", "kv_cache_memory_pct", "enable_addons", "draft_model", "ngram_speculation_length", "draft_token_count", "enable_session_affinity", "image_tag", "region", "direct_route_api_keys", "direct_route_type", "precision", "extra_args", "extra_values", "update_time", "max_context_length", "annotations", "disable_deployment_size_validation")
    class ExtraValuesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
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
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    MIN_REPLICA_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_REPLICA_COUNT_FIELD_NUMBER: _ClassVar[int]
    AUTOSCALING_POLICY_FIELD_NUMBER: _ClassVar[int]
    BASE_MODEL_FIELD_NUMBER: _ClassVar[int]
    ACCELERATOR_COUNT_FIELD_NUMBER: _ClassVar[int]
    ACCELERATOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    WORLD_SIZE_FIELD_NUMBER: _ClassVar[int]
    GENERATOR_COUNT_FIELD_NUMBER: _ClassVar[int]
    DISAGGREGATED_PREFILL_COUNT_FIELD_NUMBER: _ClassVar[int]
    DISAGGREGATED_PREFILL_WORLD_SIZE_FIELD_NUMBER: _ClassVar[int]
    MAX_BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    MAX_PEFT_BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    KV_CACHE_MEMORY_PCT_FIELD_NUMBER: _ClassVar[int]
    ENABLE_ADDONS_FIELD_NUMBER: _ClassVar[int]
    DRAFT_MODEL_FIELD_NUMBER: _ClassVar[int]
    NGRAM_SPECULATION_LENGTH_FIELD_NUMBER: _ClassVar[int]
    DRAFT_TOKEN_COUNT_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SESSION_AFFINITY_FIELD_NUMBER: _ClassVar[int]
    IMAGE_TAG_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    DIRECT_ROUTE_API_KEYS_FIELD_NUMBER: _ClassVar[int]
    DIRECT_ROUTE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRECISION_FIELD_NUMBER: _ClassVar[int]
    EXTRA_ARGS_FIELD_NUMBER: _ClassVar[int]
    EXTRA_VALUES_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    MAX_CONTEXT_LENGTH_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    DISABLE_DEPLOYMENT_SIZE_VALIDATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    created_by: str
    min_replica_count: int
    max_replica_count: int
    autoscaling_policy: _deployment_pb2.AutoscalingPolicy
    base_model: str
    accelerator_count: int
    accelerator_type: _deployment_pb2.AcceleratorType
    world_size: int
    generator_count: int
    disaggregated_prefill_count: int
    disaggregated_prefill_world_size: int
    max_batch_size: int
    max_peft_batch_size: int
    kv_cache_memory_pct: int
    enable_addons: bool
    draft_model: str
    ngram_speculation_length: int
    draft_token_count: int
    enable_session_affinity: bool
    image_tag: str
    region: _deployment_pb2.Region
    direct_route_api_keys: _containers.RepeatedScalarFieldContainer[str]
    direct_route_type: _deployment_pb2.DirectRouteType
    precision: _deployment_pb2.Deployment.Precision
    extra_args: _containers.RepeatedScalarFieldContainer[str]
    extra_values: _containers.ScalarMap[str, str]
    update_time: _timestamp_pb2.Timestamp
    max_context_length: int
    annotations: _containers.ScalarMap[str, str]
    disable_deployment_size_validation: bool
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[str] = ..., min_replica_count: _Optional[int] = ..., max_replica_count: _Optional[int] = ..., autoscaling_policy: _Optional[_Union[_deployment_pb2.AutoscalingPolicy, _Mapping]] = ..., base_model: _Optional[str] = ..., accelerator_count: _Optional[int] = ..., accelerator_type: _Optional[_Union[_deployment_pb2.AcceleratorType, str]] = ..., world_size: _Optional[int] = ..., generator_count: _Optional[int] = ..., disaggregated_prefill_count: _Optional[int] = ..., disaggregated_prefill_world_size: _Optional[int] = ..., max_batch_size: _Optional[int] = ..., max_peft_batch_size: _Optional[int] = ..., kv_cache_memory_pct: _Optional[int] = ..., enable_addons: bool = ..., draft_model: _Optional[str] = ..., ngram_speculation_length: _Optional[int] = ..., draft_token_count: _Optional[int] = ..., enable_session_affinity: bool = ..., image_tag: _Optional[str] = ..., region: _Optional[_Union[_deployment_pb2.Region, str]] = ..., direct_route_api_keys: _Optional[_Iterable[str]] = ..., direct_route_type: _Optional[_Union[_deployment_pb2.DirectRouteType, str]] = ..., precision: _Optional[_Union[_deployment_pb2.Deployment.Precision, str]] = ..., extra_args: _Optional[_Iterable[str]] = ..., extra_values: _Optional[_Mapping[str, str]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., max_context_length: _Optional[int] = ..., annotations: _Optional[_Mapping[str, str]] = ..., disable_deployment_size_validation: bool = ...) -> None: ...

class CreateDeploymentTemplateRequest(_message.Message):
    __slots__ = ("parent", "deployment_template", "deployment_template_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    deployment_template: DeploymentTemplate
    deployment_template_id: str
    def __init__(self, parent: _Optional[str] = ..., deployment_template: _Optional[_Union[DeploymentTemplate, _Mapping]] = ..., deployment_template_id: _Optional[str] = ...) -> None: ...

class GetDeploymentTemplateRequest(_message.Message):
    __slots__ = ("name", "read_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListDeploymentTemplatesRequest(_message.Message):
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

class ListDeploymentTemplatesResponse(_message.Message):
    __slots__ = ("deployment_templates", "next_page_token", "total_size")
    DEPLOYMENT_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    deployment_templates: _containers.RepeatedCompositeFieldContainer[DeploymentTemplate]
    next_page_token: str
    total_size: int
    def __init__(self, deployment_templates: _Optional[_Iterable[_Union[DeploymentTemplate, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class UpdateDeploymentTemplateRequest(_message.Message):
    __slots__ = ("deployment_template", "update_mask")
    DEPLOYMENT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    deployment_template: DeploymentTemplate
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, deployment_template: _Optional[_Union[DeploymentTemplate, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteDeploymentTemplateRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
