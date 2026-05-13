from . import options_pb2 as _options_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AlertRule(_message.Message):
    __slots__ = ("name", "alert_rule_configuration", "threshold", "duration", "enabled", "filters", "notification_channels", "create_time", "update_time")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ALERT_RULE_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    alert_rule_configuration: str
    threshold: float
    duration: str
    enabled: bool
    filters: _containers.RepeatedCompositeFieldContainer[Filter]
    notification_channels: _containers.RepeatedScalarFieldContainer[str]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., alert_rule_configuration: _Optional[str] = ..., threshold: _Optional[float] = ..., duration: _Optional[str] = ..., enabled: bool = ..., filters: _Optional[_Iterable[_Union[Filter, _Mapping]]] = ..., notification_channels: _Optional[_Iterable[str]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Filter(_message.Message):
    __slots__ = ("key", "value", "operator", "value_template")
    class Operator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPERATOR_UNSPECIFIED: _ClassVar[Filter.Operator]
        EQUAL: _ClassVar[Filter.Operator]
        NOT_EQUAL: _ClassVar[Filter.Operator]
        EQUAL_REGEX: _ClassVar[Filter.Operator]
        NOT_EQUAL_REGEX: _ClassVar[Filter.Operator]
        CONTAINS: _ClassVar[Filter.Operator]
        NOT_CONTAINS: _ClassVar[Filter.Operator]
    OPERATOR_UNSPECIFIED: Filter.Operator
    EQUAL: Filter.Operator
    NOT_EQUAL: Filter.Operator
    EQUAL_REGEX: Filter.Operator
    NOT_EQUAL_REGEX: Filter.Operator
    CONTAINS: Filter.Operator
    NOT_CONTAINS: Filter.Operator
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    VALUE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    operator: Filter.Operator
    value_template: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ..., operator: _Optional[_Union[Filter.Operator, str]] = ..., value_template: _Optional[str] = ...) -> None: ...

class AlertRuleConfiguration(_message.Message):
    __slots__ = ("name", "kind", "monitoring_policy_configuration", "create_time", "update_time")
    class Kind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        KIND_UNSPECIFIED: _ClassVar[AlertRuleConfiguration.Kind]
        MISSING_REPLICAS: _ClassVar[AlertRuleConfiguration.Kind]
        HIGH_ERROR_COUNT: _ClassVar[AlertRuleConfiguration.Kind]
        HIGH_PERPLEXITY_OUTPUT: _ClassVar[AlertRuleConfiguration.Kind]
        HIGH_TIME_TO_FIRST_TOKEN: _ClassVar[AlertRuleConfiguration.Kind]
        HIGH_PER_TOKEN_LATENCY: _ClassVar[AlertRuleConfiguration.Kind]
    KIND_UNSPECIFIED: AlertRuleConfiguration.Kind
    MISSING_REPLICAS: AlertRuleConfiguration.Kind
    HIGH_ERROR_COUNT: AlertRuleConfiguration.Kind
    HIGH_PERPLEXITY_OUTPUT: AlertRuleConfiguration.Kind
    HIGH_TIME_TO_FIRST_TOKEN: AlertRuleConfiguration.Kind
    HIGH_PER_TOKEN_LATENCY: AlertRuleConfiguration.Kind
    class MonitoringPolicyConfiguration(_message.Message):
        __slots__ = ("documentation", "display_name", "combiner", "comparison", "expression", "severity", "notification_channels", "deployment_label_key", "aggregations", "default_filters")
        class Aggregation(_message.Message):
            __slots__ = ("alignment_period", "aligner", "cross_series_reducer", "group_by_fields")
            ALIGNMENT_PERIOD_FIELD_NUMBER: _ClassVar[int]
            ALIGNER_FIELD_NUMBER: _ClassVar[int]
            CROSS_SERIES_REDUCER_FIELD_NUMBER: _ClassVar[int]
            GROUP_BY_FIELDS_FIELD_NUMBER: _ClassVar[int]
            alignment_period: str
            aligner: str
            cross_series_reducer: str
            group_by_fields: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, alignment_period: _Optional[str] = ..., aligner: _Optional[str] = ..., cross_series_reducer: _Optional[str] = ..., group_by_fields: _Optional[_Iterable[str]] = ...) -> None: ...
        DOCUMENTATION_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        COMBINER_FIELD_NUMBER: _ClassVar[int]
        COMPARISON_FIELD_NUMBER: _ClassVar[int]
        EXPRESSION_FIELD_NUMBER: _ClassVar[int]
        SEVERITY_FIELD_NUMBER: _ClassVar[int]
        NOTIFICATION_CHANNELS_FIELD_NUMBER: _ClassVar[int]
        DEPLOYMENT_LABEL_KEY_FIELD_NUMBER: _ClassVar[int]
        AGGREGATIONS_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_FILTERS_FIELD_NUMBER: _ClassVar[int]
        documentation: str
        display_name: str
        combiner: str
        comparison: str
        expression: str
        severity: str
        notification_channels: _containers.RepeatedScalarFieldContainer[str]
        deployment_label_key: str
        aggregations: _containers.RepeatedCompositeFieldContainer[AlertRuleConfiguration.MonitoringPolicyConfiguration.Aggregation]
        default_filters: _containers.RepeatedCompositeFieldContainer[Filter]
        def __init__(self, documentation: _Optional[str] = ..., display_name: _Optional[str] = ..., combiner: _Optional[str] = ..., comparison: _Optional[str] = ..., expression: _Optional[str] = ..., severity: _Optional[str] = ..., notification_channels: _Optional[_Iterable[str]] = ..., deployment_label_key: _Optional[str] = ..., aggregations: _Optional[_Iterable[_Union[AlertRuleConfiguration.MonitoringPolicyConfiguration.Aggregation, _Mapping]]] = ..., default_filters: _Optional[_Iterable[_Union[Filter, _Mapping]]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    MONITORING_POLICY_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    kind: AlertRuleConfiguration.Kind
    monitoring_policy_configuration: AlertRuleConfiguration.MonitoringPolicyConfiguration
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., kind: _Optional[_Union[AlertRuleConfiguration.Kind, str]] = ..., monitoring_policy_configuration: _Optional[_Union[AlertRuleConfiguration.MonitoringPolicyConfiguration, _Mapping]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
