from . import options_pb2 as _options_pb2
from . import status_pb2 as _status_pb2
from . import user_pb2 as _user_pb2
from . import wandb_pb2 as _wandb_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.api import visibility_pb2 as _visibility_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Account(_message.Message):
    __slots__ = ("name", "display_name", "create_time", "intended_use", "prometheus_endpoint", "athena_cost_usage_report_bucket", "account_type", "email", "state", "status", "suspend_state", "stripe_customer_id", "oidc_issuer_url", "oidc_client_id", "cognito_domain", "wandb_config", "update_time")
    class AccountType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACCOUNT_TYPE_UNSPECIFIED: _ClassVar[Account.AccountType]
        DEVELOPER: _ClassVar[Account.AccountType]
        ENTERPRISE: _ClassVar[Account.AccountType]
        BUSINESS: _ClassVar[Account.AccountType]
    ACCOUNT_TYPE_UNSPECIFIED: Account.AccountType
    DEVELOPER: Account.AccountType
    ENTERPRISE: Account.AccountType
    BUSINESS: Account.AccountType
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Account.State]
        CREATING: _ClassVar[Account.State]
        READY: _ClassVar[Account.State]
        UPDATING: _ClassVar[Account.State]
        DELETING: _ClassVar[Account.State]
    STATE_UNSPECIFIED: Account.State
    CREATING: Account.State
    READY: Account.State
    UPDATING: Account.State
    DELETING: Account.State
    class SuspendState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSUSPENDED: _ClassVar[Account.SuspendState]
        FAILED_PAYMENTS: _ClassVar[Account.SuspendState]
        CREDIT_DEPLETED: _ClassVar[Account.SuspendState]
        MONTHLY_SPEND_LIMIT_EXCEEDED: _ClassVar[Account.SuspendState]
    UNSUSPENDED: Account.SuspendState
    FAILED_PAYMENTS: Account.SuspendState
    CREDIT_DEPLETED: Account.SuspendState
    MONTHLY_SPEND_LIMIT_EXCEEDED: Account.SuspendState
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    INTENDED_USE_FIELD_NUMBER: _ClassVar[int]
    PROMETHEUS_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    ATHENA_COST_USAGE_REPORT_BUCKET_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_TYPE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SUSPEND_STATE_FIELD_NUMBER: _ClassVar[int]
    STRIPE_CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    OIDC_ISSUER_URL_FIELD_NUMBER: _ClassVar[int]
    OIDC_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    COGNITO_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    WANDB_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    create_time: _timestamp_pb2.Timestamp
    intended_use: str
    prometheus_endpoint: str
    athena_cost_usage_report_bucket: str
    account_type: Account.AccountType
    email: str
    state: Account.State
    status: _status_pb2.Status
    suspend_state: Account.SuspendState
    stripe_customer_id: str
    oidc_issuer_url: str
    oidc_client_id: str
    cognito_domain: str
    wandb_config: _wandb_pb2.WandbConfig
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., intended_use: _Optional[str] = ..., prometheus_endpoint: _Optional[str] = ..., athena_cost_usage_report_bucket: _Optional[str] = ..., account_type: _Optional[_Union[Account.AccountType, str]] = ..., email: _Optional[str] = ..., state: _Optional[_Union[Account.State, str]] = ..., status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., suspend_state: _Optional[_Union[Account.SuspendState, str]] = ..., stripe_customer_id: _Optional[str] = ..., oidc_issuer_url: _Optional[str] = ..., oidc_client_id: _Optional[str] = ..., cognito_domain: _Optional[str] = ..., wandb_config: _Optional[_Union[_wandb_pb2.WandbConfig, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateAccountRequest(_message.Message):
    __slots__ = ("account", "account_id", "wait", "user")
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    WAIT_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    account: Account
    account_id: str
    wait: bool
    user: _user_pb2.User
    def __init__(self, account: _Optional[_Union[Account, _Mapping]] = ..., account_id: _Optional[str] = ..., wait: bool = ..., user: _Optional[_Union[_user_pb2.User, _Mapping]] = ...) -> None: ...

class GetAccountRequest(_message.Message):
    __slots__ = ("name", "read_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListAccountsRequest(_message.Message):
    __slots__ = ("page_size", "page_token", "filter", "order_by", "show_all", "read_mask")
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    SHOW_ALL_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    filter: str
    order_by: str
    show_all: bool
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ..., show_all: bool = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListAccountsResponse(_message.Message):
    __slots__ = ("accounts", "next_page_token", "total_size")
    ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    accounts: _containers.RepeatedCompositeFieldContainer[Account]
    next_page_token: str
    total_size: int
    def __init__(self, accounts: _Optional[_Iterable[_Union[Account, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class UpdateAccountRequest(_message.Message):
    __slots__ = ("account", "update_mask")
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    account: Account
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, account: _Optional[_Union[Account, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteAccountRequest(_message.Message):
    __slots__ = ("name", "force")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool
    def __init__(self, name: _Optional[str] = ..., force: bool = ...) -> None: ...
