from ..buf.validate import validate_pb2 as _validate_pb2
from . import options_pb2 as _options_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IdentityProvider(_message.Message):
    __slots__ = ("name", "display_name", "create_time", "update_time", "saml_config", "oidc_config")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SAML_CONFIG_FIELD_NUMBER: _ClassVar[int]
    OIDC_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    saml_config: SamlConfig
    oidc_config: OidcConfig
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., saml_config: _Optional[_Union[SamlConfig, _Mapping]] = ..., oidc_config: _Optional[_Union[OidcConfig, _Mapping]] = ...) -> None: ...

class SamlConfig(_message.Message):
    __slots__ = ("metadata_url",)
    METADATA_URL_FIELD_NUMBER: _ClassVar[int]
    metadata_url: str
    def __init__(self, metadata_url: _Optional[str] = ...) -> None: ...

class OidcConfig(_message.Message):
    __slots__ = ("issuer_url", "client_id", "client_secret")
    ISSUER_URL_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    issuer_url: str
    client_id: str
    client_secret: str
    def __init__(self, issuer_url: _Optional[str] = ..., client_id: _Optional[str] = ..., client_secret: _Optional[str] = ...) -> None: ...

class CreateIdentityProviderRequest(_message.Message):
    __slots__ = ("parent", "identity_provider")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    identity_provider: IdentityProvider
    def __init__(self, parent: _Optional[str] = ..., identity_provider: _Optional[_Union[IdentityProvider, _Mapping]] = ...) -> None: ...

class GetIdentityProviderRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListIdentityProvidersRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ...) -> None: ...

class ListIdentityProvidersResponse(_message.Message):
    __slots__ = ("identity_providers", "next_page_token", "total_size")
    IDENTITY_PROVIDERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    identity_providers: _containers.RepeatedCompositeFieldContainer[IdentityProvider]
    next_page_token: str
    total_size: int
    def __init__(self, identity_providers: _Optional[_Iterable[_Union[IdentityProvider, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class UpdateIdentityProviderRequest(_message.Message):
    __slots__ = ("identity_provider", "update_mask")
    IDENTITY_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    identity_provider: IdentityProvider
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, identity_provider: _Optional[_Union[IdentityProvider, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteIdentityProviderRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
