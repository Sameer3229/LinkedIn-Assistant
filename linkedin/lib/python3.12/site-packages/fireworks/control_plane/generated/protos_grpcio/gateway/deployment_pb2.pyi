from ..buf.validate import validate_pb2 as _validate_pb2
from . import options_pb2 as _options_pb2
from . import status_pb2 as _status_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.api import visibility_pb2 as _visibility_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Region(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REGION_UNSPECIFIED: _ClassVar[Region]
    US_IOWA_1: _ClassVar[Region]
    US_VIRGINIA_1: _ClassVar[Region]
    US_VIRGINIA_2: _ClassVar[Region]
    US_ILLINOIS_1: _ClassVar[Region]
    AP_TOKYO_1: _ClassVar[Region]
    EU_LONDON_1: _ClassVar[Region]
    US_ARIZONA_1: _ClassVar[Region]
    US_TEXAS_1: _ClassVar[Region]
    US_ILLINOIS_2: _ClassVar[Region]
    EU_FRANKFURT_1: _ClassVar[Region]
    US_TEXAS_2: _ClassVar[Region]
    EU_PARIS_1: _ClassVar[Region]
    EU_HELSINKI_1: _ClassVar[Region]
    US_NEVADA_1: _ClassVar[Region]
    EU_ICELAND_1: _ClassVar[Region]
    EU_ICELAND_2: _ClassVar[Region]
    US_WASHINGTON_1: _ClassVar[Region]
    US_WASHINGTON_2: _ClassVar[Region]
    EU_ICELAND_DEV_1: _ClassVar[Region]
    US_WASHINGTON_3: _ClassVar[Region]
    US_ARIZONA_2: _ClassVar[Region]
    AP_TOKYO_2: _ClassVar[Region]
    US_CALIFORNIA_1: _ClassVar[Region]
    US_MISSOURI_1: _ClassVar[Region]
    US_UTAH_1: _ClassVar[Region]

class MultiRegion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MULTI_REGION_UNSPECIFIED: _ClassVar[MultiRegion]
    GLOBAL: _ClassVar[MultiRegion]
    US: _ClassVar[MultiRegion]

class AcceleratorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACCELERATOR_TYPE_UNSPECIFIED: _ClassVar[AcceleratorType]
    NVIDIA_A100_80GB: _ClassVar[AcceleratorType]
    NVIDIA_H100_80GB: _ClassVar[AcceleratorType]
    AMD_MI300X_192GB: _ClassVar[AcceleratorType]
    NVIDIA_A10G_24GB: _ClassVar[AcceleratorType]
    NVIDIA_A100_40GB: _ClassVar[AcceleratorType]
    NVIDIA_L4_24GB: _ClassVar[AcceleratorType]
    NVIDIA_H200_141GB: _ClassVar[AcceleratorType]
    NVIDIA_B200_180GB: _ClassVar[AcceleratorType]

class DirectRouteType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DIRECT_ROUTE_TYPE_UNSPECIFIED: _ClassVar[DirectRouteType]
    INTERNET: _ClassVar[DirectRouteType]
    GCP_PRIVATE_SERVICE_CONNECT: _ClassVar[DirectRouteType]
    AWS_PRIVATELINK: _ClassVar[DirectRouteType]

class Metrics(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    METRICS_UNSPECIFIED: _ClassVar[Metrics]
    REPLICA_COUNT: _ClassVar[Metrics]
    LOAD: _ClassVar[Metrics]
    CONCURRENT_REQUESTS: _ClassVar[Metrics]
    PROMPT_CACHE_HIT_RATE: _ClassVar[Metrics]
    REQUESTS_TOTAL: _ClassVar[Metrics]
    REQUESTS_ERROR_RATE: _ClassVar[Metrics]
    TOKENS_PROMPT_PER_REQUEST: _ClassVar[Metrics]
    TOKENS_GENERATED_PER_REQUEST: _ClassVar[Metrics]
    SPECULATIVE_HIT_TOTAL: _ClassVar[Metrics]
    SPECULATIVE_HIT_USER: _ClassVar[Metrics]
    REQUESTS_PER_SECOND: _ClassVar[Metrics]
    TOKENS_PER_SECOND: _ClassVar[Metrics]
    LATENCY: _ClassVar[Metrics]
    GENERATION_QUEUE_LATENCY: _ClassVar[Metrics]
    PREFILL_QUEUE_LATENCY: _ClassVar[Metrics]
    FIRST_TOKEN_LATENCY: _ClassVar[Metrics]
    GENERATION_PER_TOKEN_LATENCY: _ClassVar[Metrics]
    SERVERLESS_REQUESTS_TOTAL: _ClassVar[Metrics]
    SERVERLESS_REQUESTS_RATE_MIRROR_PER_ACCOUNT: _ClassVar[Metrics]
    SERVERLESS_REQUESTS_LIMIT_PER_ACCOUNT: _ClassVar[Metrics]
    SERVERLESS_TOKENS_PROMPT_LIMIT_PER_ACCOUNT: _ClassVar[Metrics]
    SERVERLESS_TOKENS_PROMPT_RATE_MIRROR_PER_ACCOUNT: _ClassVar[Metrics]
    SERVERLESS_TOKENS_GENERATED_LIMIT_PER_ACCOUNT: _ClassVar[Metrics]
    SERVERLESS_TOKENS_GENERATED_RATE_MIRROR_PER_ACCOUNT: _ClassVar[Metrics]
REGION_UNSPECIFIED: Region
US_IOWA_1: Region
US_VIRGINIA_1: Region
US_VIRGINIA_2: Region
US_ILLINOIS_1: Region
AP_TOKYO_1: Region
EU_LONDON_1: Region
US_ARIZONA_1: Region
US_TEXAS_1: Region
US_ILLINOIS_2: Region
EU_FRANKFURT_1: Region
US_TEXAS_2: Region
EU_PARIS_1: Region
EU_HELSINKI_1: Region
US_NEVADA_1: Region
EU_ICELAND_1: Region
EU_ICELAND_2: Region
US_WASHINGTON_1: Region
US_WASHINGTON_2: Region
EU_ICELAND_DEV_1: Region
US_WASHINGTON_3: Region
US_ARIZONA_2: Region
AP_TOKYO_2: Region
US_CALIFORNIA_1: Region
US_MISSOURI_1: Region
US_UTAH_1: Region
MULTI_REGION_UNSPECIFIED: MultiRegion
GLOBAL: MultiRegion
US: MultiRegion
ACCELERATOR_TYPE_UNSPECIFIED: AcceleratorType
NVIDIA_A100_80GB: AcceleratorType
NVIDIA_H100_80GB: AcceleratorType
AMD_MI300X_192GB: AcceleratorType
NVIDIA_A10G_24GB: AcceleratorType
NVIDIA_A100_40GB: AcceleratorType
NVIDIA_L4_24GB: AcceleratorType
NVIDIA_H200_141GB: AcceleratorType
NVIDIA_B200_180GB: AcceleratorType
DIRECT_ROUTE_TYPE_UNSPECIFIED: DirectRouteType
INTERNET: DirectRouteType
GCP_PRIVATE_SERVICE_CONNECT: DirectRouteType
AWS_PRIVATELINK: DirectRouteType
METRICS_UNSPECIFIED: Metrics
REPLICA_COUNT: Metrics
LOAD: Metrics
CONCURRENT_REQUESTS: Metrics
PROMPT_CACHE_HIT_RATE: Metrics
REQUESTS_TOTAL: Metrics
REQUESTS_ERROR_RATE: Metrics
TOKENS_PROMPT_PER_REQUEST: Metrics
TOKENS_GENERATED_PER_REQUEST: Metrics
SPECULATIVE_HIT_TOTAL: Metrics
SPECULATIVE_HIT_USER: Metrics
REQUESTS_PER_SECOND: Metrics
TOKENS_PER_SECOND: Metrics
LATENCY: Metrics
GENERATION_QUEUE_LATENCY: Metrics
PREFILL_QUEUE_LATENCY: Metrics
FIRST_TOKEN_LATENCY: Metrics
GENERATION_PER_TOKEN_LATENCY: Metrics
SERVERLESS_REQUESTS_TOTAL: Metrics
SERVERLESS_REQUESTS_RATE_MIRROR_PER_ACCOUNT: Metrics
SERVERLESS_REQUESTS_LIMIT_PER_ACCOUNT: Metrics
SERVERLESS_TOKENS_PROMPT_LIMIT_PER_ACCOUNT: Metrics
SERVERLESS_TOKENS_PROMPT_RATE_MIRROR_PER_ACCOUNT: Metrics
SERVERLESS_TOKENS_GENERATED_LIMIT_PER_ACCOUNT: Metrics
SERVERLESS_TOKENS_GENERATED_RATE_MIRROR_PER_ACCOUNT: Metrics

class Deployment(_message.Message):
    __slots__ = ("name", "display_name", "description", "create_time", "expire_time", "purge_time", "delete_time", "created_by", "state", "status", "annotations", "min_replica_count", "max_replica_count", "replica_count", "autoscaling_policy", "base_model", "accelerator_count", "accelerator_type", "precision", "world_size", "generator_count", "disaggregated_prefill_count", "disaggregated_prefill_world_size", "max_batch_size", "cluster", "enable_addons", "draft_token_count", "draft_model", "ngram_speculation_length", "max_peft_batch_size", "kv_cache_memory_pct", "enable_session_affinity", "direct_route_api_keys", "image_tag", "num_peft_device_cached", "direct_route_type", "direct_route_handle", "deployment_template", "auto_tune", "placement", "region", "disable_accounting", "extra_args", "max_context_length", "extra_values", "engine", "update_time", "for_training", "disable_deployment_size_validation", "workload", "spot")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Deployment.State]
        CREATING: _ClassVar[Deployment.State]
        READY: _ClassVar[Deployment.State]
        DELETING: _ClassVar[Deployment.State]
        FAILED: _ClassVar[Deployment.State]
        UPDATING: _ClassVar[Deployment.State]
        DELETED: _ClassVar[Deployment.State]
    STATE_UNSPECIFIED: Deployment.State
    CREATING: Deployment.State
    READY: Deployment.State
    DELETING: Deployment.State
    FAILED: Deployment.State
    UPDATING: Deployment.State
    DELETED: Deployment.State
    class Precision(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PRECISION_UNSPECIFIED: _ClassVar[Deployment.Precision]
        FP16: _ClassVar[Deployment.Precision]
        FP8: _ClassVar[Deployment.Precision]
        FP8_MM: _ClassVar[Deployment.Precision]
        FP8_AR: _ClassVar[Deployment.Precision]
        FP8_MM_KV_ATTN: _ClassVar[Deployment.Precision]
        FP8_KV: _ClassVar[Deployment.Precision]
        FP8_MM_V2: _ClassVar[Deployment.Precision]
        FP8_V2: _ClassVar[Deployment.Precision]
        FP8_MM_KV_ATTN_V2: _ClassVar[Deployment.Precision]
        NF4: _ClassVar[Deployment.Precision]
        FP4: _ClassVar[Deployment.Precision]
        BF16: _ClassVar[Deployment.Precision]
    PRECISION_UNSPECIFIED: Deployment.Precision
    FP16: Deployment.Precision
    FP8: Deployment.Precision
    FP8_MM: Deployment.Precision
    FP8_AR: Deployment.Precision
    FP8_MM_KV_ATTN: Deployment.Precision
    FP8_KV: Deployment.Precision
    FP8_MM_V2: Deployment.Precision
    FP8_V2: Deployment.Precision
    FP8_MM_KV_ATTN_V2: Deployment.Precision
    NF4: Deployment.Precision
    FP4: Deployment.Precision
    BF16: Deployment.Precision
    class Engine(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ENGINE_UNSPECIFIED: _ClassVar[Deployment.Engine]
        FIREATTENTION: _ClassVar[Deployment.Engine]
        VLLM: _ClassVar[Deployment.Engine]
        NIM: _ClassVar[Deployment.Engine]
    ENGINE_UNSPECIFIED: Deployment.Engine
    FIREATTENTION: Deployment.Engine
    VLLM: Deployment.Engine
    NIM: Deployment.Engine
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
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    PURGE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    MIN_REPLICA_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_REPLICA_COUNT_FIELD_NUMBER: _ClassVar[int]
    REPLICA_COUNT_FIELD_NUMBER: _ClassVar[int]
    AUTOSCALING_POLICY_FIELD_NUMBER: _ClassVar[int]
    BASE_MODEL_FIELD_NUMBER: _ClassVar[int]
    ACCELERATOR_COUNT_FIELD_NUMBER: _ClassVar[int]
    ACCELERATOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRECISION_FIELD_NUMBER: _ClassVar[int]
    WORLD_SIZE_FIELD_NUMBER: _ClassVar[int]
    GENERATOR_COUNT_FIELD_NUMBER: _ClassVar[int]
    DISAGGREGATED_PREFILL_COUNT_FIELD_NUMBER: _ClassVar[int]
    DISAGGREGATED_PREFILL_WORLD_SIZE_FIELD_NUMBER: _ClassVar[int]
    MAX_BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    ENABLE_ADDONS_FIELD_NUMBER: _ClassVar[int]
    DRAFT_TOKEN_COUNT_FIELD_NUMBER: _ClassVar[int]
    DRAFT_MODEL_FIELD_NUMBER: _ClassVar[int]
    NGRAM_SPECULATION_LENGTH_FIELD_NUMBER: _ClassVar[int]
    MAX_PEFT_BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    KV_CACHE_MEMORY_PCT_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SESSION_AFFINITY_FIELD_NUMBER: _ClassVar[int]
    DIRECT_ROUTE_API_KEYS_FIELD_NUMBER: _ClassVar[int]
    IMAGE_TAG_FIELD_NUMBER: _ClassVar[int]
    NUM_PEFT_DEVICE_CACHED_FIELD_NUMBER: _ClassVar[int]
    DIRECT_ROUTE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DIRECT_ROUTE_HANDLE_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    AUTO_TUNE_FIELD_NUMBER: _ClassVar[int]
    PLACEMENT_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    DISABLE_ACCOUNTING_FIELD_NUMBER: _ClassVar[int]
    EXTRA_ARGS_FIELD_NUMBER: _ClassVar[int]
    MAX_CONTEXT_LENGTH_FIELD_NUMBER: _ClassVar[int]
    EXTRA_VALUES_FIELD_NUMBER: _ClassVar[int]
    ENGINE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    FOR_TRAINING_FIELD_NUMBER: _ClassVar[int]
    DISABLE_DEPLOYMENT_SIZE_VALIDATION_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_FIELD_NUMBER: _ClassVar[int]
    SPOT_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    expire_time: _timestamp_pb2.Timestamp
    purge_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    created_by: str
    state: Deployment.State
    status: _status_pb2.Status
    annotations: _containers.ScalarMap[str, str]
    min_replica_count: int
    max_replica_count: int
    replica_count: int
    autoscaling_policy: AutoscalingPolicy
    base_model: str
    accelerator_count: int
    accelerator_type: AcceleratorType
    precision: Deployment.Precision
    world_size: int
    generator_count: int
    disaggregated_prefill_count: int
    disaggregated_prefill_world_size: int
    max_batch_size: int
    cluster: str
    enable_addons: bool
    draft_token_count: int
    draft_model: str
    ngram_speculation_length: int
    max_peft_batch_size: int
    kv_cache_memory_pct: int
    enable_session_affinity: bool
    direct_route_api_keys: _containers.RepeatedScalarFieldContainer[str]
    image_tag: str
    num_peft_device_cached: int
    direct_route_type: DirectRouteType
    direct_route_handle: str
    deployment_template: str
    auto_tune: AutoTune
    placement: Placement
    region: Region
    disable_accounting: bool
    extra_args: _containers.RepeatedScalarFieldContainer[str]
    max_context_length: int
    extra_values: _containers.ScalarMap[str, str]
    engine: Deployment.Engine
    update_time: _timestamp_pb2.Timestamp
    for_training: bool
    disable_deployment_size_validation: bool
    workload: str
    spot: bool
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., purge_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[str] = ..., state: _Optional[_Union[Deployment.State, str]] = ..., status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., annotations: _Optional[_Mapping[str, str]] = ..., min_replica_count: _Optional[int] = ..., max_replica_count: _Optional[int] = ..., replica_count: _Optional[int] = ..., autoscaling_policy: _Optional[_Union[AutoscalingPolicy, _Mapping]] = ..., base_model: _Optional[str] = ..., accelerator_count: _Optional[int] = ..., accelerator_type: _Optional[_Union[AcceleratorType, str]] = ..., precision: _Optional[_Union[Deployment.Precision, str]] = ..., world_size: _Optional[int] = ..., generator_count: _Optional[int] = ..., disaggregated_prefill_count: _Optional[int] = ..., disaggregated_prefill_world_size: _Optional[int] = ..., max_batch_size: _Optional[int] = ..., cluster: _Optional[str] = ..., enable_addons: bool = ..., draft_token_count: _Optional[int] = ..., draft_model: _Optional[str] = ..., ngram_speculation_length: _Optional[int] = ..., max_peft_batch_size: _Optional[int] = ..., kv_cache_memory_pct: _Optional[int] = ..., enable_session_affinity: bool = ..., direct_route_api_keys: _Optional[_Iterable[str]] = ..., image_tag: _Optional[str] = ..., num_peft_device_cached: _Optional[int] = ..., direct_route_type: _Optional[_Union[DirectRouteType, str]] = ..., direct_route_handle: _Optional[str] = ..., deployment_template: _Optional[str] = ..., auto_tune: _Optional[_Union[AutoTune, _Mapping]] = ..., placement: _Optional[_Union[Placement, _Mapping]] = ..., region: _Optional[_Union[Region, str]] = ..., disable_accounting: bool = ..., extra_args: _Optional[_Iterable[str]] = ..., max_context_length: _Optional[int] = ..., extra_values: _Optional[_Mapping[str, str]] = ..., engine: _Optional[_Union[Deployment.Engine, str]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., for_training: bool = ..., disable_deployment_size_validation: bool = ..., workload: _Optional[str] = ..., spot: bool = ...) -> None: ...

class Placement(_message.Message):
    __slots__ = ("region", "multi_region", "regions")
    REGION_FIELD_NUMBER: _ClassVar[int]
    MULTI_REGION_FIELD_NUMBER: _ClassVar[int]
    REGIONS_FIELD_NUMBER: _ClassVar[int]
    region: Region
    multi_region: MultiRegion
    regions: _containers.RepeatedScalarFieldContainer[Region]
    def __init__(self, region: _Optional[_Union[Region, str]] = ..., multi_region: _Optional[_Union[MultiRegion, str]] = ..., regions: _Optional[_Iterable[_Union[Region, str]]] = ...) -> None: ...

class AutoTune(_message.Message):
    __slots__ = ("long_prompt",)
    LONG_PROMPT_FIELD_NUMBER: _ClassVar[int]
    long_prompt: bool
    def __init__(self, long_prompt: bool = ...) -> None: ...

class AutoscalingPolicy(_message.Message):
    __slots__ = ("scale_up_window", "scale_down_window", "scale_to_zero_window", "load_targets")
    class LoadTargetsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float
        def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
    SCALE_UP_WINDOW_FIELD_NUMBER: _ClassVar[int]
    SCALE_DOWN_WINDOW_FIELD_NUMBER: _ClassVar[int]
    SCALE_TO_ZERO_WINDOW_FIELD_NUMBER: _ClassVar[int]
    LOAD_TARGETS_FIELD_NUMBER: _ClassVar[int]
    scale_up_window: _duration_pb2.Duration
    scale_down_window: _duration_pb2.Duration
    scale_to_zero_window: _duration_pb2.Duration
    load_targets: _containers.ScalarMap[str, float]
    def __init__(self, scale_up_window: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., scale_down_window: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., scale_to_zero_window: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., load_targets: _Optional[_Mapping[str, float]] = ...) -> None: ...

class CreateDeploymentRequest(_message.Message):
    __slots__ = ("parent", "deployment", "disable_auto_deploy", "disable_speculative_decoding", "deployment_id", "dry_run")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    DISABLE_AUTO_DEPLOY_FIELD_NUMBER: _ClassVar[int]
    DISABLE_SPECULATIVE_DECODING_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    deployment: Deployment
    disable_auto_deploy: bool
    disable_speculative_decoding: bool
    deployment_id: str
    dry_run: bool
    def __init__(self, parent: _Optional[str] = ..., deployment: _Optional[_Union[Deployment, _Mapping]] = ..., disable_auto_deploy: bool = ..., disable_speculative_decoding: bool = ..., deployment_id: _Optional[str] = ..., dry_run: bool = ...) -> None: ...

class GetDeploymentRequest(_message.Message):
    __slots__ = ("name", "read_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListDeploymentsRequest(_message.Message):
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

class ListDeploymentsResponse(_message.Message):
    __slots__ = ("deployments", "next_page_token", "total_size")
    DEPLOYMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    deployments: _containers.RepeatedCompositeFieldContainer[Deployment]
    next_page_token: str
    total_size: int
    def __init__(self, deployments: _Optional[_Iterable[_Union[Deployment, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class UpdateDeploymentRequest(_message.Message):
    __slots__ = ("deployment", "update_mask")
    DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    deployment: Deployment
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, deployment: _Optional[_Union[Deployment, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteDeploymentRequest(_message.Message):
    __slots__ = ("name", "hard", "ignore_checks")
    NAME_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    IGNORE_CHECKS_FIELD_NUMBER: _ClassVar[int]
    name: str
    hard: bool
    ignore_checks: bool
    def __init__(self, name: _Optional[str] = ..., hard: bool = ..., ignore_checks: bool = ...) -> None: ...

class UndeleteDeploymentRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ScaleDeploymentRequest(_message.Message):
    __slots__ = ("name", "replica_count")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REPLICA_COUNT_FIELD_NUMBER: _ClassVar[int]
    name: str
    replica_count: int
    def __init__(self, name: _Optional[str] = ..., replica_count: _Optional[int] = ...) -> None: ...

class GetDeploymentMetricsRequest(_message.Message):
    __slots__ = ("name", "time_range", "read_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    time_range: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., time_range: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetDeploymentMetricsResponse(_message.Message):
    __slots__ = ("metrics",)
    class MetricsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float
        def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
    METRICS_FIELD_NUMBER: _ClassVar[int]
    metrics: _containers.ScalarMap[str, float]
    def __init__(self, metrics: _Optional[_Mapping[str, float]] = ...) -> None: ...

class GetDeploymentPrerequisitesRequest(_message.Message):
    __slots__ = ("parent", "name", "read_mask")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    name: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, parent: _Optional[str] = ..., name: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeploymentPrerequisites(_message.Message):
    __slots__ = ("accelerator_configs",)
    ACCELERATOR_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    accelerator_configs: _containers.RepeatedCompositeFieldContainer[DeploymentAcceleratorConfig]
    def __init__(self, accelerator_configs: _Optional[_Iterable[_Union[DeploymentAcceleratorConfig, _Mapping]]] = ...) -> None: ...

class DeploymentAcceleratorConfig(_message.Message):
    __slots__ = ("accelerator_type", "precision", "min_accelerator_count", "regions")
    ACCELERATOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRECISION_FIELD_NUMBER: _ClassVar[int]
    MIN_ACCELERATOR_COUNT_FIELD_NUMBER: _ClassVar[int]
    REGIONS_FIELD_NUMBER: _ClassVar[int]
    accelerator_type: AcceleratorType
    precision: Deployment.Precision
    min_accelerator_count: int
    regions: _containers.RepeatedScalarFieldContainer[Region]
    def __init__(self, accelerator_type: _Optional[_Union[AcceleratorType, str]] = ..., precision: _Optional[_Union[Deployment.Precision, str]] = ..., min_accelerator_count: _Optional[int] = ..., regions: _Optional[_Iterable[_Union[Region, str]]] = ...) -> None: ...

class ListDeploymentMetricsRequest(_message.Message):
    __slots__ = ("parent", "account", "model", "metric", "start", "end", "interval", "group_by", "percentiles")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    METRIC_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_FIELD_NUMBER: _ClassVar[int]
    PERCENTILES_FIELD_NUMBER: _ClassVar[int]
    parent: str
    account: str
    model: str
    metric: Metrics
    start: _timestamp_pb2.Timestamp
    end: _timestamp_pb2.Timestamp
    interval: _duration_pb2.Duration
    group_by: str
    percentiles: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, parent: _Optional[str] = ..., account: _Optional[str] = ..., model: _Optional[str] = ..., metric: _Optional[_Union[Metrics, str]] = ..., start: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., group_by: _Optional[str] = ..., percentiles: _Optional[_Iterable[float]] = ...) -> None: ...

class TimeSeriesPoint(_message.Message):
    __slots__ = ("timestamp", "value")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    value: str
    def __init__(self, timestamp: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...

class TimeSeries(_message.Message):
    __slots__ = ("labels", "values")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    LABELS_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    labels: _containers.ScalarMap[str, str]
    values: _containers.RepeatedCompositeFieldContainer[TimeSeriesPoint]
    def __init__(self, labels: _Optional[_Mapping[str, str]] = ..., values: _Optional[_Iterable[_Union[TimeSeriesPoint, _Mapping]]] = ...) -> None: ...

class ListDeploymentMetricsResponse(_message.Message):
    __slots__ = ("series",)
    SERIES_FIELD_NUMBER: _ClassVar[int]
    series: _containers.RepeatedCompositeFieldContainer[TimeSeries]
    def __init__(self, series: _Optional[_Iterable[_Union[TimeSeries, _Mapping]]] = ...) -> None: ...
