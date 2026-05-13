from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetOAuthArgumentsRequest(_message.Message):
    __slots__ = ("account_id",)
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class GetOAuthArgumentsResponse(_message.Message):
    __slots__ = ("issuer_url", "client_id", "cognito_domain")
    ISSUER_URL_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    COGNITO_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    issuer_url: str
    client_id: str
    cognito_domain: str
    def __init__(self, issuer_url: _Optional[str] = ..., client_id: _Optional[str] = ..., cognito_domain: _Optional[str] = ...) -> None: ...
