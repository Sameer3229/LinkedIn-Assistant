from . import options_pb2 as _options_pb2
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

class EvaluatorState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STATE_UNSPECIFIED: _ClassVar[EvaluatorState]
    ACTIVE: _ClassVar[EvaluatorState]
STATE_UNSPECIFIED: EvaluatorState
ACTIVE: EvaluatorState

class Evaluator(_message.Message):
    __slots__ = ("name", "display_name", "description", "create_time", "created_by", "update_time", "state", "multi_metrics", "criteria", "requirements", "rollup_settings")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    MULTI_METRICS_FIELD_NUMBER: _ClassVar[int]
    CRITERIA_FIELD_NUMBER: _ClassVar[int]
    REQUIREMENTS_FIELD_NUMBER: _ClassVar[int]
    ROLLUP_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    created_by: str
    update_time: _timestamp_pb2.Timestamp
    state: EvaluatorState
    multi_metrics: bool
    criteria: _containers.RepeatedCompositeFieldContainer[Criterion]
    requirements: str
    rollup_settings: RollupSettings
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[str] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., state: _Optional[_Union[EvaluatorState, str]] = ..., multi_metrics: bool = ..., criteria: _Optional[_Iterable[_Union[Criterion, _Mapping]]] = ..., requirements: _Optional[str] = ..., rollup_settings: _Optional[_Union[RollupSettings, _Mapping]] = ...) -> None: ...

class Criterion(_message.Message):
    __slots__ = ("type", "name", "description", "code_snippets")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[Criterion.Type]
        CODE_SNIPPETS: _ClassVar[Criterion.Type]
    TYPE_UNSPECIFIED: Criterion.Type
    CODE_SNIPPETS: Criterion.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CODE_SNIPPETS_FIELD_NUMBER: _ClassVar[int]
    type: Criterion.Type
    name: str
    description: str
    code_snippets: CodeSnippets
    def __init__(self, type: _Optional[_Union[Criterion.Type, str]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., code_snippets: _Optional[_Union[CodeSnippets, _Mapping]] = ...) -> None: ...

class CodeSnippets(_message.Message):
    __slots__ = ("language", "file_contents", "entry_file", "entry_func")
    class FileContentsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    FILE_CONTENTS_FIELD_NUMBER: _ClassVar[int]
    ENTRY_FILE_FIELD_NUMBER: _ClassVar[int]
    ENTRY_FUNC_FIELD_NUMBER: _ClassVar[int]
    language: str
    file_contents: _containers.ScalarMap[str, str]
    entry_file: str
    entry_func: str
    def __init__(self, language: _Optional[str] = ..., file_contents: _Optional[_Mapping[str, str]] = ..., entry_file: _Optional[str] = ..., entry_func: _Optional[str] = ...) -> None: ...

class RollupSettings(_message.Message):
    __slots__ = ("criteria_weights", "python_code", "success_threshold", "skip_rollup")
    class CriteriaWeightsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float
        def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
    CRITERIA_WEIGHTS_FIELD_NUMBER: _ClassVar[int]
    PYTHON_CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    SKIP_ROLLUP_FIELD_NUMBER: _ClassVar[int]
    criteria_weights: _containers.ScalarMap[str, float]
    python_code: str
    success_threshold: float
    skip_rollup: bool
    def __init__(self, criteria_weights: _Optional[_Mapping[str, float]] = ..., python_code: _Optional[str] = ..., success_threshold: _Optional[float] = ..., skip_rollup: bool = ...) -> None: ...

class GetEvaluatorRequest(_message.Message):
    __slots__ = ("name", "read_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListEvaluatorsRequest(_message.Message):
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

class ListEvaluatorsResponse(_message.Message):
    __slots__ = ("evaluators", "next_page_token", "total_size")
    EVALUATORS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    evaluators: _containers.RepeatedCompositeFieldContainer[Evaluator]
    next_page_token: str
    total_size: int
    def __init__(self, evaluators: _Optional[_Iterable[_Union[Evaluator, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class CreateEvaluatorRequest(_message.Message):
    __slots__ = ("parent", "evaluator", "evaluator_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_FIELD_NUMBER: _ClassVar[int]
    EVALUATOR_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    evaluator: Evaluator
    evaluator_id: str
    def __init__(self, parent: _Optional[str] = ..., evaluator: _Optional[_Union[Evaluator, _Mapping]] = ..., evaluator_id: _Optional[str] = ...) -> None: ...

class DeleteEvaluatorRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class PreviewEvaluatorRequest(_message.Message):
    __slots__ = ("evaluator", "sample_data", "max_samples", "parent")
    EVALUATOR_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_DATA_FIELD_NUMBER: _ClassVar[int]
    MAX_SAMPLES_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    evaluator: Evaluator
    sample_data: _containers.RepeatedScalarFieldContainer[str]
    max_samples: int
    parent: str
    def __init__(self, evaluator: _Optional[_Union[Evaluator, _Mapping]] = ..., sample_data: _Optional[_Iterable[str]] = ..., max_samples: _Optional[int] = ..., parent: _Optional[str] = ...) -> None: ...

class PreviewEvaluatorSampleResult(_message.Message):
    __slots__ = ("success", "score", "per_metric_evals", "reason")
    class PerMetricEvalsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Struct
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    PER_METRIC_EVALS_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    success: str
    score: float
    per_metric_evals: _containers.MessageMap[str, _struct_pb2.Struct]
    reason: str
    def __init__(self, success: _Optional[str] = ..., score: _Optional[float] = ..., per_metric_evals: _Optional[_Mapping[str, _struct_pb2.Struct]] = ..., reason: _Optional[str] = ...) -> None: ...

class PreviewEvaluatorResponse(_message.Message):
    __slots__ = ("results", "total_samples", "total_runtime_ms", "stdout", "stderr")
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SAMPLES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_RUNTIME_MS_FIELD_NUMBER: _ClassVar[int]
    STDOUT_FIELD_NUMBER: _ClassVar[int]
    STDERR_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[PreviewEvaluatorSampleResult]
    total_samples: int
    total_runtime_ms: int
    stdout: _containers.RepeatedScalarFieldContainer[str]
    stderr: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, results: _Optional[_Iterable[_Union[PreviewEvaluatorSampleResult, _Mapping]]] = ..., total_samples: _Optional[int] = ..., total_runtime_ms: _Optional[int] = ..., stdout: _Optional[_Iterable[str]] = ..., stderr: _Optional[_Iterable[str]] = ...) -> None: ...
