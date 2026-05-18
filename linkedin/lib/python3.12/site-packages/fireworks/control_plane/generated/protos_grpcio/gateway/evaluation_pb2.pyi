from ..buf.validate import validate_pb2 as _validate_pb2
from . import options_pb2 as _options_pb2
from . import status_pb2 as _status_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Evaluation(_message.Message):
    __slots__ = ("name", "create_time", "created_by", "status", "evaluation_type", "description", "providers", "assertions", "update_time")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PROVIDERS_FIELD_NUMBER: _ClassVar[int]
    ASSERTIONS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    created_by: str
    status: _status_pb2.Status
    evaluation_type: str
    description: str
    providers: _containers.RepeatedCompositeFieldContainer[Provider]
    assertions: _containers.RepeatedCompositeFieldContainer[Assertion]
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[str] = ..., status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., evaluation_type: _Optional[str] = ..., description: _Optional[str] = ..., providers: _Optional[_Iterable[_Union[Provider, _Mapping]]] = ..., assertions: _Optional[_Iterable[_Union[Assertion, _Mapping]]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Assertion(_message.Message):
    __slots__ = ("assertion_type", "llm_assertion", "code_assertion", "metric_name")
    class AssertionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ASSERTION_TYPE_UNSPECIFIED: _ClassVar[Assertion.AssertionType]
        ASSERTION_TYPE_LLM: _ClassVar[Assertion.AssertionType]
        ASSERTION_TYPE_CODE: _ClassVar[Assertion.AssertionType]
    ASSERTION_TYPE_UNSPECIFIED: Assertion.AssertionType
    ASSERTION_TYPE_LLM: Assertion.AssertionType
    ASSERTION_TYPE_CODE: Assertion.AssertionType
    ASSERTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    LLM_ASSERTION_FIELD_NUMBER: _ClassVar[int]
    CODE_ASSERTION_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    assertion_type: Assertion.AssertionType
    llm_assertion: LLMAssertion
    code_assertion: CodeAssertion
    metric_name: str
    def __init__(self, assertion_type: _Optional[_Union[Assertion.AssertionType, str]] = ..., llm_assertion: _Optional[_Union[LLMAssertion, _Mapping]] = ..., code_assertion: _Optional[_Union[CodeAssertion, _Mapping]] = ..., metric_name: _Optional[str] = ...) -> None: ...

class LLMAssertion(_message.Message):
    __slots__ = ("llm_evaluator_prompt", "providers", "prompts", "evaluate_options")
    LLM_EVALUATOR_PROMPT_FIELD_NUMBER: _ClassVar[int]
    PROVIDERS_FIELD_NUMBER: _ClassVar[int]
    PROMPTS_FIELD_NUMBER: _ClassVar[int]
    EVALUATE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    llm_evaluator_prompt: str
    providers: _containers.RepeatedCompositeFieldContainer[Provider]
    prompts: _containers.RepeatedScalarFieldContainer[str]
    evaluate_options: EvaluateOptions
    def __init__(self, llm_evaluator_prompt: _Optional[str] = ..., providers: _Optional[_Iterable[_Union[Provider, _Mapping]]] = ..., prompts: _Optional[_Iterable[str]] = ..., evaluate_options: _Optional[_Union[EvaluateOptions, _Mapping]] = ...) -> None: ...

class CodeAssertion(_message.Message):
    __slots__ = ("language", "code", "expected_output", "options")
    class ExecutionOptions(_message.Message):
        __slots__ = ("timeout_ms", "memory_limit_mb", "env_vars")
        class EnvVarsEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
        MEMORY_LIMIT_MB_FIELD_NUMBER: _ClassVar[int]
        ENV_VARS_FIELD_NUMBER: _ClassVar[int]
        timeout_ms: int
        memory_limit_mb: int
        env_vars: _containers.ScalarMap[str, str]
        def __init__(self, timeout_ms: _Optional[int] = ..., memory_limit_mb: _Optional[int] = ..., env_vars: _Optional[_Mapping[str, str]] = ...) -> None: ...
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    language: str
    code: str
    expected_output: str
    options: CodeAssertion.ExecutionOptions
    def __init__(self, language: _Optional[str] = ..., code: _Optional[str] = ..., expected_output: _Optional[str] = ..., options: _Optional[_Union[CodeAssertion.ExecutionOptions, _Mapping]] = ...) -> None: ...

class Provider(_message.Message):
    __slots__ = ("id", "config", "label")
    class ConfigEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    id: str
    config: _containers.ScalarMap[str, str]
    label: str
    def __init__(self, id: _Optional[str] = ..., config: _Optional[_Mapping[str, str]] = ..., label: _Optional[str] = ...) -> None: ...

class EvaluateOptions(_message.Message):
    __slots__ = ("max_concurrency", "repeat", "delay")
    MAX_CONCURRENCY_FIELD_NUMBER: _ClassVar[int]
    REPEAT_FIELD_NUMBER: _ClassVar[int]
    DELAY_FIELD_NUMBER: _ClassVar[int]
    max_concurrency: int
    repeat: int
    delay: int
    def __init__(self, max_concurrency: _Optional[int] = ..., repeat: _Optional[int] = ..., delay: _Optional[int] = ...) -> None: ...

class GetEvaluationRequest(_message.Message):
    __slots__ = ("name", "read_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class CreateEvaluationRequest(_message.Message):
    __slots__ = ("parent", "evaluation", "evaluation_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    evaluation: Evaluation
    evaluation_id: str
    def __init__(self, parent: _Optional[str] = ..., evaluation: _Optional[_Union[Evaluation, _Mapping]] = ..., evaluation_id: _Optional[str] = ...) -> None: ...

class ListEvaluationsRequest(_message.Message):
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

class ListEvaluationsResponse(_message.Message):
    __slots__ = ("evaluations", "next_page_token", "total_size")
    EVALUATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    evaluations: _containers.RepeatedCompositeFieldContainer[Evaluation]
    next_page_token: str
    total_size: int
    def __init__(self, evaluations: _Optional[_Iterable[_Union[Evaluation, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class UpdateEvaluationRequest(_message.Message):
    __slots__ = ("name", "evaluation", "update_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    evaluation: Evaluation
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., evaluation: _Optional[_Union[Evaluation, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteEvaluationRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class TestEvaluationRequest(_message.Message):
    __slots__ = ("parent", "evaluation", "sample_data")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_DATA_FIELD_NUMBER: _ClassVar[int]
    parent: str
    evaluation: Evaluation
    sample_data: str
    def __init__(self, parent: _Optional[str] = ..., evaluation: _Optional[_Union[Evaluation, _Mapping]] = ..., sample_data: _Optional[str] = ...) -> None: ...

class ValidateAssertionsRequest(_message.Message):
    __slots__ = ("parent", "assertions")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ASSERTIONS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    assertions: _containers.RepeatedCompositeFieldContainer[Assertion]
    def __init__(self, parent: _Optional[str] = ..., assertions: _Optional[_Iterable[_Union[Assertion, _Mapping]]] = ...) -> None: ...

class ValidateAssertionsResponse(_message.Message):
    __slots__ = ("status", "metric_to_errors")
    class MetricToErrorsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ValidateAssertionsResponse.ValidateAssertionError
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ValidateAssertionsResponse.ValidateAssertionError, _Mapping]] = ...) -> None: ...
    class ValidateAssertionError(_message.Message):
        __slots__ = ("error_messages",)
        ERROR_MESSAGES_FIELD_NUMBER: _ClassVar[int]
        error_messages: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, error_messages: _Optional[_Iterable[str]] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    METRIC_TO_ERRORS_FIELD_NUMBER: _ClassVar[int]
    status: str
    metric_to_errors: _containers.MessageMap[str, ValidateAssertionsResponse.ValidateAssertionError]
    def __init__(self, status: _Optional[str] = ..., metric_to_errors: _Optional[_Mapping[str, ValidateAssertionsResponse.ValidateAssertionError]] = ...) -> None: ...

class PreviewEvaluationRequest(_message.Message):
    __slots__ = ("name", "sample_data", "max_samples")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_DATA_FIELD_NUMBER: _ClassVar[int]
    MAX_SAMPLES_FIELD_NUMBER: _ClassVar[int]
    name: str
    sample_data: str
    max_samples: int
    def __init__(self, name: _Optional[str] = ..., sample_data: _Optional[str] = ..., max_samples: _Optional[int] = ...) -> None: ...

class PreviewEvaluationResult(_message.Message):
    __slots__ = ("success", "reason", "score", "messages", "metrics")
    class MetricsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float
        def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    reason: str
    score: float
    messages: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Struct]
    metrics: _containers.ScalarMap[str, float]
    def __init__(self, success: bool = ..., reason: _Optional[str] = ..., score: _Optional[float] = ..., messages: _Optional[_Iterable[_Union[_struct_pb2.Struct, _Mapping]]] = ..., metrics: _Optional[_Mapping[str, float]] = ...) -> None: ...

class PreviewEvaluationResponse(_message.Message):
    __slots__ = ("results", "total_samples", "total_runtime_ms")
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SAMPLES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_RUNTIME_MS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[PreviewEvaluationResult]
    total_samples: int
    total_runtime_ms: int
    def __init__(self, results: _Optional[_Iterable[_Union[PreviewEvaluationResult, _Mapping]]] = ..., total_samples: _Optional[int] = ..., total_runtime_ms: _Optional[int] = ...) -> None: ...
