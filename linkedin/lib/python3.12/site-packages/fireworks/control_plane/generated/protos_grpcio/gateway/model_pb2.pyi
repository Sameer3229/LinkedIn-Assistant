from . import billing_pb2 as _billing_pb2
from . import deployed_model_pb2 as _deployed_model_pb2
from . import deployment_pb2 as _deployment_pb2
from . import options_pb2 as _options_pb2
from . import status_pb2 as _status_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.api import visibility_pb2 as _visibility_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import date_pb2 as _date_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Model(_message.Message):
    __slots__ = ("name", "display_name", "description", "create_time", "created_by", "state", "status", "kind", "github_url", "hugging_face_url", "base_model_details", "peft_details", "teft_details", "public", "conversation_config", "context_length", "supports_image_input", "supports_tools", "imported_from", "tokens_per_second", "featured_priority", "fine_tuning_job", "sku_infos", "default_draft_model", "default_draft_token_count", "deployed_model_refs", "cluster", "deprecation_date", "calibrated", "tunable", "supports_lora", "use_hf_apply_chat_template", "extra_deployment_args", "update_time", "default_sampling_params", "gcs_uri", "rl_tunable", "supported_precisions", "supported_precisions_with_calibration", "training_context_length", "image_tag", "annotations")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Model.State]
        UPLOADING: _ClassVar[Model.State]
        READY: _ClassVar[Model.State]
    STATE_UNSPECIFIED: Model.State
    UPLOADING: Model.State
    READY: Model.State
    class Kind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        KIND_UNSPECIFIED: _ClassVar[Model.Kind]
        HF_BASE_MODEL: _ClassVar[Model.Kind]
        HF_PEFT_ADDON: _ClassVar[Model.Kind]
        HF_TEFT_ADDON: _ClassVar[Model.Kind]
        FLUMINA_BASE_MODEL: _ClassVar[Model.Kind]
        FLUMINA_ADDON: _ClassVar[Model.Kind]
        DRAFT_ADDON: _ClassVar[Model.Kind]
        FIRE_AGENT: _ClassVar[Model.Kind]
        LIVE_MERGE: _ClassVar[Model.Kind]
        CUSTOM_MODEL: _ClassVar[Model.Kind]
    KIND_UNSPECIFIED: Model.Kind
    HF_BASE_MODEL: Model.Kind
    HF_PEFT_ADDON: Model.Kind
    HF_TEFT_ADDON: Model.Kind
    FLUMINA_BASE_MODEL: Model.Kind
    FLUMINA_ADDON: Model.Kind
    DRAFT_ADDON: Model.Kind
    FIRE_AGENT: Model.Kind
    LIVE_MERGE: Model.Kind
    CUSTOM_MODEL: Model.Kind
    class DefaultSamplingParamsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float
        def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
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
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    GITHUB_URL_FIELD_NUMBER: _ClassVar[int]
    HUGGING_FACE_URL_FIELD_NUMBER: _ClassVar[int]
    BASE_MODEL_DETAILS_FIELD_NUMBER: _ClassVar[int]
    PEFT_DETAILS_FIELD_NUMBER: _ClassVar[int]
    TEFT_DETAILS_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_LENGTH_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_IMAGE_INPUT_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_TOOLS_FIELD_NUMBER: _ClassVar[int]
    IMPORTED_FROM_FIELD_NUMBER: _ClassVar[int]
    TOKENS_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    FEATURED_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    FINE_TUNING_JOB_FIELD_NUMBER: _ClassVar[int]
    SKU_INFOS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_DRAFT_MODEL_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_DRAFT_TOKEN_COUNT_FIELD_NUMBER: _ClassVar[int]
    DEPLOYED_MODEL_REFS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    DEPRECATION_DATE_FIELD_NUMBER: _ClassVar[int]
    CALIBRATED_FIELD_NUMBER: _ClassVar[int]
    TUNABLE_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_LORA_FIELD_NUMBER: _ClassVar[int]
    USE_HF_APPLY_CHAT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    EXTRA_DEPLOYMENT_ARGS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SAMPLING_PARAMS_FIELD_NUMBER: _ClassVar[int]
    GCS_URI_FIELD_NUMBER: _ClassVar[int]
    RL_TUNABLE_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_PRECISIONS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_PRECISIONS_WITH_CALIBRATION_FIELD_NUMBER: _ClassVar[int]
    TRAINING_CONTEXT_LENGTH_FIELD_NUMBER: _ClassVar[int]
    IMAGE_TAG_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    created_by: str
    state: Model.State
    status: _status_pb2.Status
    kind: Model.Kind
    github_url: str
    hugging_face_url: str
    base_model_details: BaseModelDetails
    peft_details: PEFTDetails
    teft_details: TEFTDetails
    public: bool
    conversation_config: ConversationConfig
    context_length: int
    supports_image_input: bool
    supports_tools: bool
    imported_from: str
    tokens_per_second: int
    featured_priority: int
    fine_tuning_job: str
    sku_infos: _containers.RepeatedCompositeFieldContainer[_billing_pb2.SKUInfo]
    default_draft_model: str
    default_draft_token_count: int
    deployed_model_refs: _containers.RepeatedCompositeFieldContainer[_deployed_model_pb2.DeployedModelRef]
    cluster: str
    deprecation_date: _date_pb2.Date
    calibrated: bool
    tunable: bool
    supports_lora: bool
    use_hf_apply_chat_template: bool
    extra_deployment_args: _containers.RepeatedScalarFieldContainer[str]
    update_time: _timestamp_pb2.Timestamp
    default_sampling_params: _containers.ScalarMap[str, float]
    gcs_uri: str
    rl_tunable: bool
    supported_precisions: _containers.RepeatedScalarFieldContainer[_deployment_pb2.Deployment.Precision]
    supported_precisions_with_calibration: _containers.RepeatedScalarFieldContainer[_deployment_pb2.Deployment.Precision]
    training_context_length: int
    image_tag: str
    annotations: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[str] = ..., state: _Optional[_Union[Model.State, str]] = ..., status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., kind: _Optional[_Union[Model.Kind, str]] = ..., github_url: _Optional[str] = ..., hugging_face_url: _Optional[str] = ..., base_model_details: _Optional[_Union[BaseModelDetails, _Mapping]] = ..., peft_details: _Optional[_Union[PEFTDetails, _Mapping]] = ..., teft_details: _Optional[_Union[TEFTDetails, _Mapping]] = ..., public: bool = ..., conversation_config: _Optional[_Union[ConversationConfig, _Mapping]] = ..., context_length: _Optional[int] = ..., supports_image_input: bool = ..., supports_tools: bool = ..., imported_from: _Optional[str] = ..., tokens_per_second: _Optional[int] = ..., featured_priority: _Optional[int] = ..., fine_tuning_job: _Optional[str] = ..., sku_infos: _Optional[_Iterable[_Union[_billing_pb2.SKUInfo, _Mapping]]] = ..., default_draft_model: _Optional[str] = ..., default_draft_token_count: _Optional[int] = ..., deployed_model_refs: _Optional[_Iterable[_Union[_deployed_model_pb2.DeployedModelRef, _Mapping]]] = ..., cluster: _Optional[str] = ..., deprecation_date: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., calibrated: bool = ..., tunable: bool = ..., supports_lora: bool = ..., use_hf_apply_chat_template: bool = ..., extra_deployment_args: _Optional[_Iterable[str]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., default_sampling_params: _Optional[_Mapping[str, float]] = ..., gcs_uri: _Optional[str] = ..., rl_tunable: bool = ..., supported_precisions: _Optional[_Iterable[_Union[_deployment_pb2.Deployment.Precision, str]]] = ..., supported_precisions_with_calibration: _Optional[_Iterable[_Union[_deployment_pb2.Deployment.Precision, str]]] = ..., training_context_length: _Optional[int] = ..., image_tag: _Optional[str] = ..., annotations: _Optional[_Mapping[str, str]] = ...) -> None: ...

class BaseModelDetails(_message.Message):
    __slots__ = ("world_size", "checkpoint_format", "huggingface_files", "parameter_count", "moe", "tunable", "model_type", "supports_fireattention", "default_precision")
    class CheckpointFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CHECKPOINT_FORMAT_UNSPECIFIED: _ClassVar[BaseModelDetails.CheckpointFormat]
        NATIVE: _ClassVar[BaseModelDetails.CheckpointFormat]
        HUGGINGFACE: _ClassVar[BaseModelDetails.CheckpointFormat]
    CHECKPOINT_FORMAT_UNSPECIFIED: BaseModelDetails.CheckpointFormat
    NATIVE: BaseModelDetails.CheckpointFormat
    HUGGINGFACE: BaseModelDetails.CheckpointFormat
    WORLD_SIZE_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_FORMAT_FIELD_NUMBER: _ClassVar[int]
    HUGGINGFACE_FILES_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_COUNT_FIELD_NUMBER: _ClassVar[int]
    MOE_FIELD_NUMBER: _ClassVar[int]
    TUNABLE_FIELD_NUMBER: _ClassVar[int]
    MODEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_FIREATTENTION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_PRECISION_FIELD_NUMBER: _ClassVar[int]
    world_size: int
    checkpoint_format: BaseModelDetails.CheckpointFormat
    huggingface_files: _containers.RepeatedScalarFieldContainer[str]
    parameter_count: int
    moe: bool
    tunable: bool
    model_type: str
    supports_fireattention: bool
    default_precision: _deployment_pb2.Deployment.Precision
    def __init__(self, world_size: _Optional[int] = ..., checkpoint_format: _Optional[_Union[BaseModelDetails.CheckpointFormat, str]] = ..., huggingface_files: _Optional[_Iterable[str]] = ..., parameter_count: _Optional[int] = ..., moe: bool = ..., tunable: bool = ..., model_type: _Optional[str] = ..., supports_fireattention: bool = ..., default_precision: _Optional[_Union[_deployment_pb2.Deployment.Precision, str]] = ...) -> None: ...

class PEFTDetails(_message.Message):
    __slots__ = ("base_model", "r", "target_modules", "base_model_type", "merge_addon_model_name")
    BASE_MODEL_FIELD_NUMBER: _ClassVar[int]
    R_FIELD_NUMBER: _ClassVar[int]
    TARGET_MODULES_FIELD_NUMBER: _ClassVar[int]
    BASE_MODEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    MERGE_ADDON_MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    base_model: str
    r: int
    target_modules: _containers.RepeatedScalarFieldContainer[str]
    base_model_type: str
    merge_addon_model_name: str
    def __init__(self, base_model: _Optional[str] = ..., r: _Optional[int] = ..., target_modules: _Optional[_Iterable[str]] = ..., base_model_type: _Optional[str] = ..., merge_addon_model_name: _Optional[str] = ...) -> None: ...

class TEFTDetails(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ConversationConfig(_message.Message):
    __slots__ = ("style", "system", "template")
    STYLE_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    style: str
    system: str
    template: str
    def __init__(self, style: _Optional[str] = ..., system: _Optional[str] = ..., template: _Optional[str] = ...) -> None: ...

class CreateModelRequest(_message.Message):
    __slots__ = ("parent", "model", "model_id", "cluster")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    model: Model
    model_id: str
    cluster: str
    def __init__(self, parent: _Optional[str] = ..., model: _Optional[_Union[Model, _Mapping]] = ..., model_id: _Optional[str] = ..., cluster: _Optional[str] = ...) -> None: ...

class GetModelRequest(_message.Message):
    __slots__ = ("name", "read_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class PrepareModelRequest(_message.Message):
    __slots__ = ("name", "precision", "read_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRECISION_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    precision: _deployment_pb2.Deployment.Precision
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., precision: _Optional[_Union[_deployment_pb2.Deployment.Precision, str]] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetModelUploadEndpointRequest(_message.Message):
    __slots__ = ("name", "filename_to_size", "enable_resumable_upload", "read_mask")
    class FilenameToSizeEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    FILENAME_TO_SIZE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_RESUMABLE_UPLOAD_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    filename_to_size: _containers.ScalarMap[str, int]
    enable_resumable_upload: bool
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., filename_to_size: _Optional[_Mapping[str, int]] = ..., enable_resumable_upload: bool = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetModelUploadEndpointResponse(_message.Message):
    __slots__ = ("filename_to_signed_urls", "filename_to_unsigned_uris")
    class FilenameToSignedUrlsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class FilenameToUnsignedUrisEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    FILENAME_TO_SIGNED_URLS_FIELD_NUMBER: _ClassVar[int]
    FILENAME_TO_UNSIGNED_URIS_FIELD_NUMBER: _ClassVar[int]
    filename_to_signed_urls: _containers.ScalarMap[str, str]
    filename_to_unsigned_uris: _containers.ScalarMap[str, str]
    def __init__(self, filename_to_signed_urls: _Optional[_Mapping[str, str]] = ..., filename_to_unsigned_uris: _Optional[_Mapping[str, str]] = ...) -> None: ...

class GetModelDownloadEndpointRequest(_message.Message):
    __slots__ = ("name", "read_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetModelDownloadEndpointResponse(_message.Message):
    __slots__ = ("filename_to_signed_urls",)
    class FilenameToSignedUrlsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    FILENAME_TO_SIGNED_URLS_FIELD_NUMBER: _ClassVar[int]
    filename_to_signed_urls: _containers.ScalarMap[str, str]
    def __init__(self, filename_to_signed_urls: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ValidateModelUploadRequest(_message.Message):
    __slots__ = ("name", "skip_hf_config_validation", "trust_remote_code", "config_only")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SKIP_HF_CONFIG_VALIDATION_FIELD_NUMBER: _ClassVar[int]
    TRUST_REMOTE_CODE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_ONLY_FIELD_NUMBER: _ClassVar[int]
    name: str
    skip_hf_config_validation: bool
    trust_remote_code: bool
    config_only: bool
    def __init__(self, name: _Optional[str] = ..., skip_hf_config_validation: bool = ..., trust_remote_code: bool = ..., config_only: bool = ...) -> None: ...

class ListModelsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by", "include_deployed_model_refs", "read_mask", "show_internal")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_DEPLOYED_MODEL_REFS_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    SHOW_INTERNAL_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    include_deployed_model_refs: bool
    read_mask: _field_mask_pb2.FieldMask
    show_internal: bool
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ..., include_deployed_model_refs: bool = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., show_internal: bool = ...) -> None: ...

class ListModelsResponse(_message.Message):
    __slots__ = ("models", "next_page_token", "total_size")
    MODELS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    models: _containers.RepeatedCompositeFieldContainer[Model]
    next_page_token: str
    total_size: int
    def __init__(self, models: _Optional[_Iterable[_Union[Model, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class ListServerlessLoraModelsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListServerlessLoraModelsResponse(_message.Message):
    __slots__ = ("models",)
    MODELS_FIELD_NUMBER: _ClassVar[int]
    models: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, models: _Optional[_Iterable[str]] = ...) -> None: ...

class ValidateModelConfigRequest(_message.Message):
    __slots__ = ("config_json", "tokenizer_config_json")
    CONFIG_JSON_FIELD_NUMBER: _ClassVar[int]
    TOKENIZER_CONFIG_JSON_FIELD_NUMBER: _ClassVar[int]
    config_json: str
    tokenizer_config_json: str
    def __init__(self, config_json: _Optional[str] = ..., tokenizer_config_json: _Optional[str] = ...) -> None: ...

class UpdateModelRequest(_message.Message):
    __slots__ = ("model", "update_mask")
    MODEL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    model: Model
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, model: _Optional[_Union[Model, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteModelRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class AwsS3ModelSource(_message.Message):
    __slots__ = ("s3_bucket", "s3_path", "role_arn", "access_key_id", "access_secret")
    S3_BUCKET_FIELD_NUMBER: _ClassVar[int]
    S3_PATH_FIELD_NUMBER: _ClassVar[int]
    ROLE_ARN_FIELD_NUMBER: _ClassVar[int]
    ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_SECRET_FIELD_NUMBER: _ClassVar[int]
    s3_bucket: str
    s3_path: str
    role_arn: str
    access_key_id: str
    access_secret: str
    def __init__(self, s3_bucket: _Optional[str] = ..., s3_path: _Optional[str] = ..., role_arn: _Optional[str] = ..., access_key_id: _Optional[str] = ..., access_secret: _Optional[str] = ...) -> None: ...

class ImportModelRequest(_message.Message):
    __slots__ = ("name", "aws_s3_source")
    NAME_FIELD_NUMBER: _ClassVar[int]
    AWS_S3_SOURCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    aws_s3_source: AwsS3ModelSource
    def __init__(self, name: _Optional[str] = ..., aws_s3_source: _Optional[_Union[AwsS3ModelSource, _Mapping]] = ...) -> None: ...
