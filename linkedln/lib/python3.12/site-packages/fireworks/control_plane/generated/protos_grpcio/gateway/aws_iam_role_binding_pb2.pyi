from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AwsIamRoleBinding(_message.Message):
    __slots__ = ("account_id", "create_time", "principal", "role")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    create_time: _timestamp_pb2.Timestamp
    principal: str
    role: str
    def __init__(self, account_id: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., principal: _Optional[str] = ..., role: _Optional[str] = ...) -> None: ...

class CreateAwsIamRoleBindingRequest(_message.Message):
    __slots__ = ("parent", "aws_iam_role_binding")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    AWS_IAM_ROLE_BINDING_FIELD_NUMBER: _ClassVar[int]
    parent: str
    aws_iam_role_binding: AwsIamRoleBinding
    def __init__(self, parent: _Optional[str] = ..., aws_iam_role_binding: _Optional[_Union[AwsIamRoleBinding, _Mapping]] = ...) -> None: ...

class ListAwsIamRoleBindingsRequest(_message.Message):
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

class ListAwsIamRoleBindingsResponse(_message.Message):
    __slots__ = ("aws_iam_role_bindings", "next_page_token", "total_size")
    AWS_IAM_ROLE_BINDINGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    aws_iam_role_bindings: _containers.RepeatedCompositeFieldContainer[AwsIamRoleBinding]
    next_page_token: str
    total_size: int
    def __init__(self, aws_iam_role_bindings: _Optional[_Iterable[_Union[AwsIamRoleBinding, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class DeleteAwsIamRoleBindingRequest(_message.Message):
    __slots__ = ("aws_iam_role_binding",)
    AWS_IAM_ROLE_BINDING_FIELD_NUMBER: _ClassVar[int]
    aws_iam_role_binding: AwsIamRoleBinding
    def __init__(self, aws_iam_role_binding: _Optional[_Union[AwsIamRoleBinding, _Mapping]] = ...) -> None: ...
