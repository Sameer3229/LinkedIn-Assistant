from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import visibility_pb2 as _visibility_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import money_pb2 as _money_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetBalanceRequest(_message.Message):
    __slots__ = ("name", "read_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class Balance(_message.Message):
    __slots__ = ("money",)
    MONEY_FIELD_NUMBER: _ClassVar[int]
    money: _money_pb2.Money
    def __init__(self, money: _Optional[_Union[_money_pb2.Money, _Mapping]] = ...) -> None: ...

class ListPaymentMethodsRequest(_message.Message):
    __slots__ = ("parent", "read_mask")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, parent: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class StripeCheckoutSession(_message.Message):
    __slots__ = ("id", "checkout_url", "mode", "amount", "create_time")
    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODE_UNSPECIFIED: _ClassVar[StripeCheckoutSession.Mode]
        PAYMENT: _ClassVar[StripeCheckoutSession.Mode]
        SETUP: _ClassVar[StripeCheckoutSession.Mode]
    MODE_UNSPECIFIED: StripeCheckoutSession.Mode
    PAYMENT: StripeCheckoutSession.Mode
    SETUP: StripeCheckoutSession.Mode
    ID_FIELD_NUMBER: _ClassVar[int]
    CHECKOUT_URL_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    id: str
    checkout_url: str
    mode: StripeCheckoutSession.Mode
    amount: _money_pb2.Money
    create_time: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., checkout_url: _Optional[str] = ..., mode: _Optional[_Union[StripeCheckoutSession.Mode, str]] = ..., amount: _Optional[_Union[_money_pb2.Money, _Mapping]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListPaymentMethodsResponse(_message.Message):
    __slots__ = ("default_payment_method_id", "stripe_payment_methods", "pending_checkout_sessions")
    class Card(_message.Message):
        __slots__ = ("brand", "last4", "exp_month", "exp_year")
        BRAND_FIELD_NUMBER: _ClassVar[int]
        LAST4_FIELD_NUMBER: _ClassVar[int]
        EXP_MONTH_FIELD_NUMBER: _ClassVar[int]
        EXP_YEAR_FIELD_NUMBER: _ClassVar[int]
        brand: str
        last4: str
        exp_month: int
        exp_year: int
        def __init__(self, brand: _Optional[str] = ..., last4: _Optional[str] = ..., exp_month: _Optional[int] = ..., exp_year: _Optional[int] = ...) -> None: ...
    class UsBankAccount(_message.Message):
        __slots__ = ("bank_name", "last4")
        BANK_NAME_FIELD_NUMBER: _ClassVar[int]
        LAST4_FIELD_NUMBER: _ClassVar[int]
        bank_name: str
        last4: str
        def __init__(self, bank_name: _Optional[str] = ..., last4: _Optional[str] = ...) -> None: ...
    class StripePaymentMethod(_message.Message):
        __slots__ = ("id", "card", "us_bank_account")
        ID_FIELD_NUMBER: _ClassVar[int]
        CARD_FIELD_NUMBER: _ClassVar[int]
        US_BANK_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
        id: str
        card: ListPaymentMethodsResponse.Card
        us_bank_account: ListPaymentMethodsResponse.UsBankAccount
        def __init__(self, id: _Optional[str] = ..., card: _Optional[_Union[ListPaymentMethodsResponse.Card, _Mapping]] = ..., us_bank_account: _Optional[_Union[ListPaymentMethodsResponse.UsBankAccount, _Mapping]] = ...) -> None: ...
    DEFAULT_PAYMENT_METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    STRIPE_PAYMENT_METHODS_FIELD_NUMBER: _ClassVar[int]
    PENDING_CHECKOUT_SESSIONS_FIELD_NUMBER: _ClassVar[int]
    default_payment_method_id: str
    stripe_payment_methods: _containers.RepeatedCompositeFieldContainer[ListPaymentMethodsResponse.StripePaymentMethod]
    pending_checkout_sessions: _containers.RepeatedCompositeFieldContainer[StripeCheckoutSession]
    def __init__(self, default_payment_method_id: _Optional[str] = ..., stripe_payment_methods: _Optional[_Iterable[_Union[ListPaymentMethodsResponse.StripePaymentMethod, _Mapping]]] = ..., pending_checkout_sessions: _Optional[_Iterable[_Union[StripeCheckoutSession, _Mapping]]] = ...) -> None: ...

class ListCostsRequest(_message.Message):
    __slots__ = ("parent", "start_time", "end_time", "cumulative")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    CUMULATIVE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    cumulative: bool
    def __init__(self, parent: _Optional[str] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., cumulative: bool = ...) -> None: ...

class ListCostsResponse(_message.Message):
    __slots__ = ("cost_data_items",)
    class CostDataItem(_message.Message):
        __slots__ = ("subtotal", "total", "start_time", "end_time")
        SUBTOTAL_FIELD_NUMBER: _ClassVar[int]
        TOTAL_FIELD_NUMBER: _ClassVar[int]
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        END_TIME_FIELD_NUMBER: _ClassVar[int]
        subtotal: _money_pb2.Money
        total: _money_pb2.Money
        start_time: _timestamp_pb2.Timestamp
        end_time: _timestamp_pb2.Timestamp
        def __init__(self, subtotal: _Optional[_Union[_money_pb2.Money, _Mapping]] = ..., total: _Optional[_Union[_money_pb2.Money, _Mapping]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    COST_DATA_ITEMS_FIELD_NUMBER: _ClassVar[int]
    cost_data_items: _containers.RepeatedCompositeFieldContainer[ListCostsResponse.CostDataItem]
    def __init__(self, cost_data_items: _Optional[_Iterable[_Union[ListCostsResponse.CostDataItem, _Mapping]]] = ...) -> None: ...

class ListInvoicesRequest(_message.Message):
    __slots__ = ("parent", "pending", "page_size", "page_token", "filter", "order_by")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PENDING_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    pending: bool
    page_size: int
    page_token: str
    filter: str
    order_by: str
    def __init__(self, parent: _Optional[str] = ..., pending: bool = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class Invoice(_message.Message):
    __slots__ = ("id", "amount_due", "invoice_url", "state", "target_time", "paid_time")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Invoice.State]
        DRAFT: _ClassVar[Invoice.State]
        ISSUED: _ClassVar[Invoice.State]
        PAID: _ClassVar[Invoice.State]
        VOID: _ClassVar[Invoice.State]
        FAILED: _ClassVar[Invoice.State]
    STATE_UNSPECIFIED: Invoice.State
    DRAFT: Invoice.State
    ISSUED: Invoice.State
    PAID: Invoice.State
    VOID: Invoice.State
    FAILED: Invoice.State
    ID_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_DUE_FIELD_NUMBER: _ClassVar[int]
    INVOICE_URL_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    TARGET_TIME_FIELD_NUMBER: _ClassVar[int]
    PAID_TIME_FIELD_NUMBER: _ClassVar[int]
    id: str
    amount_due: _money_pb2.Money
    invoice_url: str
    state: Invoice.State
    target_time: _timestamp_pb2.Timestamp
    paid_time: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., amount_due: _Optional[_Union[_money_pb2.Money, _Mapping]] = ..., invoice_url: _Optional[str] = ..., state: _Optional[_Union[Invoice.State, str]] = ..., target_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., paid_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListInvoicesResponse(_message.Message):
    __slots__ = ("invoices", "next_page_token", "total_size")
    INVOICES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    invoices: _containers.RepeatedCompositeFieldContainer[Invoice]
    next_page_token: str
    total_size: int
    def __init__(self, invoices: _Optional[_Iterable[_Union[Invoice, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class SKUInfo(_message.Message):
    __slots__ = ("sku", "amount", "unit")
    SKU_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    sku: str
    amount: _money_pb2.Money
    unit: str
    def __init__(self, sku: _Optional[str] = ..., amount: _Optional[_Union[_money_pb2.Money, _Mapping]] = ..., unit: _Optional[str] = ...) -> None: ...

class ExportBillingMetricsRequest(_message.Message):
    __slots__ = ("name", "start_time", "end_time")
    NAME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ExportBillingMetricsResponse(_message.Message):
    __slots__ = ("signed_urls",)
    SIGNED_URLS_FIELD_NUMBER: _ClassVar[int]
    signed_urls: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, signed_urls: _Optional[_Iterable[str]] = ...) -> None: ...

class GetTotalHistoricalSpendRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetTotalHistoricalSpendResponse(_message.Message):
    __slots__ = ("spend",)
    SPEND_FIELD_NUMBER: _ClassVar[int]
    spend: _money_pb2.Money
    def __init__(self, spend: _Optional[_Union[_money_pb2.Money, _Mapping]] = ...) -> None: ...

class ListHuggingFaceBillingCostsRecords(_message.Message):
    __slots__ = ("parent", "request_ids")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_IDS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    request_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, parent: _Optional[str] = ..., request_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class BillingRequestCostRecord(_message.Message):
    __slots__ = ("request_id", "cost_nano_usd")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    COST_NANO_USD_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    cost_nano_usd: float
    def __init__(self, request_id: _Optional[str] = ..., cost_nano_usd: _Optional[float] = ...) -> None: ...

class ListHuggingFaceBillingCostsResponse(_message.Message):
    __slots__ = ("requests",)
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    requests: _containers.RepeatedCompositeFieldContainer[BillingRequestCostRecord]
    def __init__(self, requests: _Optional[_Iterable[_Union[BillingRequestCostRecord, _Mapping]]] = ...) -> None: ...

class GetAccountUsageRequest(_message.Message):
    __slots__ = ("name", "start_time", "end_time")
    NAME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AccountUsage(_message.Message):
    __slots__ = ("serverless_costs", "dedicated_costs")
    class ServerlessUsage(_message.Message):
        __slots__ = ("model_name", "prompt_tokens", "completion_tokens", "start_time", "end_time", "audio_input_seconds", "usage_type")
        MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
        PROMPT_TOKENS_FIELD_NUMBER: _ClassVar[int]
        COMPLETION_TOKENS_FIELD_NUMBER: _ClassVar[int]
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        END_TIME_FIELD_NUMBER: _ClassVar[int]
        AUDIO_INPUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
        USAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
        model_name: str
        prompt_tokens: int
        completion_tokens: int
        start_time: _timestamp_pb2.Timestamp
        end_time: _timestamp_pb2.Timestamp
        audio_input_seconds: float
        usage_type: str
        def __init__(self, model_name: _Optional[str] = ..., prompt_tokens: _Optional[int] = ..., completion_tokens: _Optional[int] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., audio_input_seconds: _Optional[float] = ..., usage_type: _Optional[str] = ...) -> None: ...
    class DedicatedDeploymentUsage(_message.Message):
        __slots__ = ("deployment_id", "accelerator_type", "accelerator_seconds", "start_time", "end_time")
        DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
        ACCELERATOR_TYPE_FIELD_NUMBER: _ClassVar[int]
        ACCELERATOR_SECONDS_FIELD_NUMBER: _ClassVar[int]
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        END_TIME_FIELD_NUMBER: _ClassVar[int]
        deployment_id: str
        accelerator_type: str
        accelerator_seconds: float
        start_time: _timestamp_pb2.Timestamp
        end_time: _timestamp_pb2.Timestamp
        def __init__(self, deployment_id: _Optional[str] = ..., accelerator_type: _Optional[str] = ..., accelerator_seconds: _Optional[float] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    SERVERLESS_COSTS_FIELD_NUMBER: _ClassVar[int]
    DEDICATED_COSTS_FIELD_NUMBER: _ClassVar[int]
    serverless_costs: _containers.RepeatedCompositeFieldContainer[AccountUsage.ServerlessUsage]
    dedicated_costs: _containers.RepeatedCompositeFieldContainer[AccountUsage.DedicatedDeploymentUsage]
    def __init__(self, serverless_costs: _Optional[_Iterable[_Union[AccountUsage.ServerlessUsage, _Mapping]]] = ..., dedicated_costs: _Optional[_Iterable[_Union[AccountUsage.DedicatedDeploymentUsage, _Mapping]]] = ...) -> None: ...
