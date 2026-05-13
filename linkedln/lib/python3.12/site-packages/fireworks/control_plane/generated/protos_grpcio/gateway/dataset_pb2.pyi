from . import options_pb2 as _options_pb2
from . import status_pb2 as _status_pb2
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

class Dataset(_message.Message):
    __slots__ = ("name", "display_name", "create_time", "state", "status", "example_count", "access_policy", "user_uploaded", "evaluation_result", "fireworks_traced", "draft_model_states", "transformed", "splitted", "external_url", "format", "created_by", "update_time", "source_job_name")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Dataset.State]
        UPLOADING: _ClassVar[Dataset.State]
        READY: _ClassVar[Dataset.State]
    STATE_UNSPECIFIED: Dataset.State
    UPLOADING: Dataset.State
    READY: Dataset.State
    class AccessPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PRIVATE: _ClassVar[Dataset.AccessPolicy]
        PUBLIC: _ClassVar[Dataset.AccessPolicy]
    PRIVATE: Dataset.AccessPolicy
    PUBLIC: Dataset.AccessPolicy
    class Format(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FORMAT_UNSPECIFIED: _ClassVar[Dataset.Format]
        CHAT: _ClassVar[Dataset.Format]
        COMPLETION: _ClassVar[Dataset.Format]
        RL: _ClassVar[Dataset.Format]
    FORMAT_UNSPECIFIED: Dataset.Format
    CHAT: Dataset.Format
    COMPLETION: Dataset.Format
    RL: Dataset.Format
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    ACCESS_POLICY_FIELD_NUMBER: _ClassVar[int]
    USER_UPLOADED_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_RESULT_FIELD_NUMBER: _ClassVar[int]
    FIREWORKS_TRACED_FIELD_NUMBER: _ClassVar[int]
    DRAFT_MODEL_STATES_FIELD_NUMBER: _ClassVar[int]
    TRANSFORMED_FIELD_NUMBER: _ClassVar[int]
    SPLITTED_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_URL_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    create_time: _timestamp_pb2.Timestamp
    state: Dataset.State
    status: _status_pb2.Status
    example_count: int
    access_policy: Dataset.AccessPolicy
    user_uploaded: UserUploaded
    evaluation_result: EvaluationResult
    fireworks_traced: FireworksTraced
    draft_model_states: DraftModelStates
    transformed: Transformed
    splitted: Splitted
    external_url: str
    format: Dataset.Format
    created_by: str
    update_time: _timestamp_pb2.Timestamp
    source_job_name: str
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., state: _Optional[_Union[Dataset.State, str]] = ..., status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., example_count: _Optional[int] = ..., access_policy: _Optional[_Union[Dataset.AccessPolicy, str]] = ..., user_uploaded: _Optional[_Union[UserUploaded, _Mapping]] = ..., evaluation_result: _Optional[_Union[EvaluationResult, _Mapping]] = ..., fireworks_traced: _Optional[_Union[FireworksTraced, _Mapping]] = ..., draft_model_states: _Optional[_Union[DraftModelStates, _Mapping]] = ..., transformed: _Optional[_Union[Transformed, _Mapping]] = ..., splitted: _Optional[_Union[Splitted, _Mapping]] = ..., external_url: _Optional[str] = ..., format: _Optional[_Union[Dataset.Format, str]] = ..., created_by: _Optional[str] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., source_job_name: _Optional[str] = ...) -> None: ...

class PreviewDatasetRequest(_message.Message):
    __slots__ = ("name", "page_size", "page_token", "filter", "order_by")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    name: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    def __init__(self, name: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class PreviewDatasetResponse(_message.Message):
    __slots__ = ("examples", "next_page_token", "total_count")
    EXAMPLES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    examples: _containers.RepeatedCompositeFieldContainer[Example]
    next_page_token: str
    total_count: int
    def __init__(self, examples: _Optional[_Iterable[_Union[Example, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_count: _Optional[int] = ...) -> None: ...

class Example(_message.Message):
    __slots__ = ("content",)
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: str
    def __init__(self, content: _Optional[str] = ...) -> None: ...

class UserUploaded(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Transformed(_message.Message):
    __slots__ = ("source_dataset_id", "filter", "original_format")
    SOURCE_DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_FORMAT_FIELD_NUMBER: _ClassVar[int]
    source_dataset_id: str
    filter: str
    original_format: Dataset.Format
    def __init__(self, source_dataset_id: _Optional[str] = ..., filter: _Optional[str] = ..., original_format: _Optional[_Union[Dataset.Format, str]] = ...) -> None: ...

class Splitted(_message.Message):
    __slots__ = ("source_dataset_id",)
    SOURCE_DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    source_dataset_id: str
    def __init__(self, source_dataset_id: _Optional[str] = ...) -> None: ...

class FireworksTraced(_message.Message):
    __slots__ = ("model", "base_model", "start_time", "end_time")
    MODEL_FIELD_NUMBER: _ClassVar[int]
    BASE_MODEL_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    model: str
    base_model: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    def __init__(self, model: _Optional[str] = ..., base_model: _Optional[str] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DraftModelStates(_message.Message):
    __slots__ = ("base_model",)
    BASE_MODEL_FIELD_NUMBER: _ClassVar[int]
    base_model: str
    def __init__(self, base_model: _Optional[str] = ...) -> None: ...

class EvaluationResult(_message.Message):
    __slots__ = ("evaluation_job_id",)
    EVALUATION_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    evaluation_job_id: str
    def __init__(self, evaluation_job_id: _Optional[str] = ...) -> None: ...

class GetDatasetRequest(_message.Message):
    __slots__ = ("name", "read_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class CreateDatasetRequest(_message.Message):
    __slots__ = ("parent", "dataset", "dataset_id", "source_dataset_id", "filter")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DATASET_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    dataset: Dataset
    dataset_id: str
    source_dataset_id: str
    filter: str
    def __init__(self, parent: _Optional[str] = ..., dataset: _Optional[_Union[Dataset, _Mapping]] = ..., dataset_id: _Optional[str] = ..., source_dataset_id: _Optional[str] = ..., filter: _Optional[str] = ...) -> None: ...

class UpdateDatasetRequest(_message.Message):
    __slots__ = ("dataset", "update_mask")
    DATASET_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    dataset: Dataset
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, dataset: _Optional[_Union[Dataset, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UploadDatasetRequest(_message.Message):
    __slots__ = ("name", "filename_to_size")
    class FilenameToSizeEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    FILENAME_TO_SIZE_FIELD_NUMBER: _ClassVar[int]
    name: str
    filename_to_size: _containers.ScalarMap[str, int]
    def __init__(self, name: _Optional[str] = ..., filename_to_size: _Optional[_Mapping[str, int]] = ...) -> None: ...

class UploadDatasetResponse(_message.Message):
    __slots__ = ("filename_to_signed_urls",)
    class FilenameToSignedUrlsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    FILENAME_TO_SIGNED_URLS_FIELD_NUMBER: _ClassVar[int]
    filename_to_signed_urls: _containers.ScalarMap[str, str]
    def __init__(self, filename_to_signed_urls: _Optional[_Mapping[str, str]] = ...) -> None: ...

class GetDatasetUploadEndpointRequest(_message.Message):
    __slots__ = ("name", "filename_to_size", "read_mask")
    class FilenameToSizeEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    FILENAME_TO_SIZE_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    filename_to_size: _containers.ScalarMap[str, int]
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., filename_to_size: _Optional[_Mapping[str, int]] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetDatasetUploadEndpointResponse(_message.Message):
    __slots__ = ("filename_to_signed_urls",)
    class FilenameToSignedUrlsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    FILENAME_TO_SIGNED_URLS_FIELD_NUMBER: _ClassVar[int]
    filename_to_signed_urls: _containers.ScalarMap[str, str]
    def __init__(self, filename_to_signed_urls: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ValidateDatasetUploadRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetDatasetDownloadEndpointRequest(_message.Message):
    __slots__ = ("name", "read_mask", "download_lineage")
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_LINEAGE_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_mask: _field_mask_pb2.FieldMask
    download_lineage: bool
    def __init__(self, name: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., download_lineage: bool = ...) -> None: ...

class GetDatasetDownloadEndpointResponse(_message.Message):
    __slots__ = ("filename_to_signed_urls",)
    class FilenameToSignedUrlsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    FILENAME_TO_SIGNED_URLS_FIELD_NUMBER: _ClassVar[int]
    filename_to_signed_urls: _containers.ScalarMap[str, str]
    def __init__(self, filename_to_signed_urls: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ListDatasetsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by", "read_mask", "show_internal")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    SHOW_INTERNAL_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    read_mask: _field_mask_pb2.FieldMask
    show_internal: bool
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., show_internal: bool = ...) -> None: ...

class ListDatasetsResponse(_message.Message):
    __slots__ = ("datasets", "next_page_token", "total_size")
    DATASETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    datasets: _containers.RepeatedCompositeFieldContainer[Dataset]
    next_page_token: str
    total_size: int
    def __init__(self, datasets: _Optional[_Iterable[_Union[Dataset, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_size: _Optional[int] = ...) -> None: ...

class DeleteDatasetRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class SplitDatasetRequest(_message.Message):
    __slots__ = ("name", "chunk_size", "parent")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    chunk_size: int
    parent: str
    def __init__(self, name: _Optional[str] = ..., chunk_size: _Optional[int] = ..., parent: _Optional[str] = ...) -> None: ...

class SplitDatasetResponse(_message.Message):
    __slots__ = ("chunk_dataset_names", "chunks_created", "total_examples")
    CHUNK_DATASET_NAMES_FIELD_NUMBER: _ClassVar[int]
    CHUNKS_CREATED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_EXAMPLES_FIELD_NUMBER: _ClassVar[int]
    chunk_dataset_names: _containers.RepeatedScalarFieldContainer[str]
    chunks_created: int
    total_examples: int
    def __init__(self, chunk_dataset_names: _Optional[_Iterable[str]] = ..., chunks_created: _Optional[int] = ..., total_examples: _Optional[int] = ...) -> None: ...
