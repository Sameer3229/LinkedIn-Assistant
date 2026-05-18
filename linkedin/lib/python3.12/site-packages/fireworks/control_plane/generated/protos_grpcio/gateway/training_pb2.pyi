from ..buf.validate import validate_pb2 as _validate_pb2
from . import deployment_pb2 as _deployment_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import visibility_pb2 as _visibility_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WeightPrecision(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WEIGHT_PRECISION_UNSPECIFIED: _ClassVar[WeightPrecision]
    BFLOAT16: _ClassVar[WeightPrecision]
    INT8: _ClassVar[WeightPrecision]
    NF4: _ClassVar[WeightPrecision]
WEIGHT_PRECISION_UNSPECIFIED: WeightPrecision
BFLOAT16: WeightPrecision
INT8: WeightPrecision
NF4: WeightPrecision

class EarlyStopConfig(_message.Message):
    __slots__ = ("is_set", "enabled")
    IS_SET_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    is_set: bool
    enabled: bool
    def __init__(self, is_set: bool = ..., enabled: bool = ...) -> None: ...

class BaseTrainingConfig(_message.Message):
    __slots__ = ("output_model", "base_model", "warm_start_from", "jinja_template", "learning_rate", "max_context_length", "lora_rank", "base_model_weight_precision", "accelerator_type", "accelerator_count", "region", "epochs", "batch_size", "is_intermediate", "toleration")
    OUTPUT_MODEL_FIELD_NUMBER: _ClassVar[int]
    BASE_MODEL_FIELD_NUMBER: _ClassVar[int]
    WARM_START_FROM_FIELD_NUMBER: _ClassVar[int]
    JINJA_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    LEARNING_RATE_FIELD_NUMBER: _ClassVar[int]
    MAX_CONTEXT_LENGTH_FIELD_NUMBER: _ClassVar[int]
    LORA_RANK_FIELD_NUMBER: _ClassVar[int]
    BASE_MODEL_WEIGHT_PRECISION_FIELD_NUMBER: _ClassVar[int]
    ACCELERATOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCELERATOR_COUNT_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    EPOCHS_FIELD_NUMBER: _ClassVar[int]
    BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    IS_INTERMEDIATE_FIELD_NUMBER: _ClassVar[int]
    TOLERATION_FIELD_NUMBER: _ClassVar[int]
    output_model: str
    base_model: str
    warm_start_from: str
    jinja_template: str
    learning_rate: float
    max_context_length: int
    lora_rank: int
    base_model_weight_precision: WeightPrecision
    accelerator_type: _deployment_pb2.AcceleratorType
    accelerator_count: int
    region: _deployment_pb2.Region
    epochs: int
    batch_size: int
    is_intermediate: bool
    toleration: str
    def __init__(self, output_model: _Optional[str] = ..., base_model: _Optional[str] = ..., warm_start_from: _Optional[str] = ..., jinja_template: _Optional[str] = ..., learning_rate: _Optional[float] = ..., max_context_length: _Optional[int] = ..., lora_rank: _Optional[int] = ..., base_model_weight_precision: _Optional[_Union[WeightPrecision, str]] = ..., accelerator_type: _Optional[_Union[_deployment_pb2.AcceleratorType, str]] = ..., accelerator_count: _Optional[int] = ..., region: _Optional[_Union[_deployment_pb2.Region, str]] = ..., epochs: _Optional[int] = ..., batch_size: _Optional[int] = ..., is_intermediate: bool = ..., toleration: _Optional[str] = ...) -> None: ...
