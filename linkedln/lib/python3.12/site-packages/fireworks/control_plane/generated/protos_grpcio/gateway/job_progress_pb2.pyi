from google.api import visibility_pb2 as _visibility_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class JobProgress(_message.Message):
    __slots__ = ("percent", "epoch", "chunk", "total_input_requests", "total_processed_requests", "successfully_processed_requests", "failed_requests", "output_rows", "input_tokens", "output_tokens")
    PERCENT_FIELD_NUMBER: _ClassVar[int]
    EPOCH_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    TOTAL_INPUT_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PROCESSED_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    SUCCESSFULLY_PROCESSED_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    FAILED_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_ROWS_FIELD_NUMBER: _ClassVar[int]
    INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    percent: int
    epoch: int
    chunk: int
    total_input_requests: int
    total_processed_requests: int
    successfully_processed_requests: int
    failed_requests: int
    output_rows: int
    input_tokens: int
    output_tokens: int
    def __init__(self, percent: _Optional[int] = ..., epoch: _Optional[int] = ..., chunk: _Optional[int] = ..., total_input_requests: _Optional[int] = ..., total_processed_requests: _Optional[int] = ..., successfully_processed_requests: _Optional[int] = ..., failed_requests: _Optional[int] = ..., output_rows: _Optional[int] = ..., input_tokens: _Optional[int] = ..., output_tokens: _Optional[int] = ...) -> None: ...
