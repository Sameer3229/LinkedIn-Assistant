from . import options_pb2 as _options_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import date_pb2 as _date_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OuterEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OUTER_ENUM_UNSPECIFIED: _ClassVar[OuterEnum]
    ONE: _ClassVar[OuterEnum]
OUTER_ENUM_UNSPECIFIED: OuterEnum
ONE: OuterEnum

class TestResource(_message.Message):
    __slots__ = ("name", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12", "f13", "f14", "f15", "f16", "f18", "f19", "f20", "f21", "f22", "f23", "f24", "f25", "f26", "f27", "f28", "f29", "f30", "f31")
    class InnerEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INNER_ENUM_UNSPECIFIED: _ClassVar[TestResource.InnerEnum]
        ONE: _ClassVar[TestResource.InnerEnum]
    INNER_ENUM_UNSPECIFIED: TestResource.InnerEnum
    ONE: TestResource.InnerEnum
    class InnerMessage(_message.Message):
        __slots__ = ("foo",)
        FOO_FIELD_NUMBER: _ClassVar[int]
        foo: str
        def __init__(self, foo: _Optional[str] = ...) -> None: ...
    class NestedMessage(_message.Message):
        __slots__ = ("baz", "qux", "quux", "quuz", "corge", "grault")
        class InnerNested(_message.Message):
            __slots__ = ("garply", "waldo", "fred")
            GARPLY_FIELD_NUMBER: _ClassVar[int]
            WALDO_FIELD_NUMBER: _ClassVar[int]
            FRED_FIELD_NUMBER: _ClassVar[int]
            garply: str
            waldo: str
            fred: str
            def __init__(self, garply: _Optional[str] = ..., waldo: _Optional[str] = ..., fred: _Optional[str] = ...) -> None: ...
        BAZ_FIELD_NUMBER: _ClassVar[int]
        QUX_FIELD_NUMBER: _ClassVar[int]
        QUUX_FIELD_NUMBER: _ClassVar[int]
        QUUZ_FIELD_NUMBER: _ClassVar[int]
        CORGE_FIELD_NUMBER: _ClassVar[int]
        GRAULT_FIELD_NUMBER: _ClassVar[int]
        baz: str
        qux: str
        quux: str
        quuz: str
        corge: str
        grault: TestResource.NestedMessage.InnerNested
        def __init__(self, baz: _Optional[str] = ..., qux: _Optional[str] = ..., quux: _Optional[str] = ..., quuz: _Optional[str] = ..., corge: _Optional[str] = ..., grault: _Optional[_Union[TestResource.NestedMessage.InnerNested, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    F2_FIELD_NUMBER: _ClassVar[int]
    F3_FIELD_NUMBER: _ClassVar[int]
    F4_FIELD_NUMBER: _ClassVar[int]
    F5_FIELD_NUMBER: _ClassVar[int]
    F6_FIELD_NUMBER: _ClassVar[int]
    F7_FIELD_NUMBER: _ClassVar[int]
    F8_FIELD_NUMBER: _ClassVar[int]
    F9_FIELD_NUMBER: _ClassVar[int]
    F10_FIELD_NUMBER: _ClassVar[int]
    F11_FIELD_NUMBER: _ClassVar[int]
    F12_FIELD_NUMBER: _ClassVar[int]
    F13_FIELD_NUMBER: _ClassVar[int]
    F14_FIELD_NUMBER: _ClassVar[int]
    F15_FIELD_NUMBER: _ClassVar[int]
    F16_FIELD_NUMBER: _ClassVar[int]
    F18_FIELD_NUMBER: _ClassVar[int]
    F19_FIELD_NUMBER: _ClassVar[int]
    F20_FIELD_NUMBER: _ClassVar[int]
    F21_FIELD_NUMBER: _ClassVar[int]
    F22_FIELD_NUMBER: _ClassVar[int]
    F23_FIELD_NUMBER: _ClassVar[int]
    F24_FIELD_NUMBER: _ClassVar[int]
    F25_FIELD_NUMBER: _ClassVar[int]
    F26_FIELD_NUMBER: _ClassVar[int]
    F27_FIELD_NUMBER: _ClassVar[int]
    F28_FIELD_NUMBER: _ClassVar[int]
    F29_FIELD_NUMBER: _ClassVar[int]
    F30_FIELD_NUMBER: _ClassVar[int]
    F31_FIELD_NUMBER: _ClassVar[int]
    name: str
    f2: float
    f3: float
    f4: int
    f5: int
    f6: int
    f7: int
    f8: int
    f9: int
    f10: int
    f11: int
    f12: int
    f13: int
    f14: bool
    f15: str
    f16: _timestamp_pb2.Timestamp
    f18: TestResource.InnerEnum
    f19: OuterEnum
    f20: TestResource.InnerMessage
    f21: OuterMessage
    f22: _date_pb2.Date
    f23: str
    f24: str
    f25: str
    f26: str
    f27: str
    f28: TestResource.NestedMessage
    f29: TestResource.NestedMessage
    f30: TestResource.NestedMessage
    f31: TestResource.NestedMessage
    def __init__(self, name: _Optional[str] = ..., f2: _Optional[float] = ..., f3: _Optional[float] = ..., f4: _Optional[int] = ..., f5: _Optional[int] = ..., f6: _Optional[int] = ..., f7: _Optional[int] = ..., f8: _Optional[int] = ..., f9: _Optional[int] = ..., f10: _Optional[int] = ..., f11: _Optional[int] = ..., f12: _Optional[int] = ..., f13: _Optional[int] = ..., f14: bool = ..., f15: _Optional[str] = ..., f16: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., f18: _Optional[_Union[TestResource.InnerEnum, str]] = ..., f19: _Optional[_Union[OuterEnum, str]] = ..., f20: _Optional[_Union[TestResource.InnerMessage, _Mapping]] = ..., f21: _Optional[_Union[OuterMessage, _Mapping]] = ..., f22: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., f23: _Optional[str] = ..., f24: _Optional[str] = ..., f25: _Optional[str] = ..., f26: _Optional[str] = ..., f27: _Optional[str] = ..., f28: _Optional[_Union[TestResource.NestedMessage, _Mapping]] = ..., f29: _Optional[_Union[TestResource.NestedMessage, _Mapping]] = ..., f30: _Optional[_Union[TestResource.NestedMessage, _Mapping]] = ..., f31: _Optional[_Union[TestResource.NestedMessage, _Mapping]] = ...) -> None: ...

class OuterMessage(_message.Message):
    __slots__ = ("bar",)
    BAR_FIELD_NUMBER: _ClassVar[int]
    bar: str
    def __init__(self, bar: _Optional[str] = ...) -> None: ...
