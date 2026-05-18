import asyncio
import time
from typing import TYPE_CHECKING, Optional, Union, List
from openai import NotGiven, NOT_GIVEN
from abc import ABC, abstractmethod

from fireworks._literals import ReasoningEffort
from fireworks.client.error import (
    InvalidRequestError,
    RateLimitError,
    BadGatewayError,
    ServiceUnavailableError,
)
from fireworks._logger import logger
from fireworks.llm._types import ResponseFormat

# Type checking imports to avoid circular imports
if TYPE_CHECKING:
    from fireworks.llm.llm import LLM

DEFAULT_MAX_RETRIES = 10
DEFAULT_DELAY = 0.5


class BaseCompletion(ABC):
    """Base class for completion wrappers that provides common functionality."""

    _client = None  # type: ignore

    def __init__(self, llm: "LLM"):
        self._model_id = None
        self._llm = llm

    def _create_setup(self, skip_setup: bool = False):
        """
        Setup for .create() and .acreate()

        Args:
            skip_setup: If True, skip deployment readiness check and model ID resolution
        """
        if skip_setup:
            # Return cached model_id if available, otherwise get it without setup
            return self._llm.model_id()
        if not self._llm._ran_setup:
            self._llm._ensure_deployment_ready()
            self._llm._ran_setup = True
        return self._llm.model_id()

    def _should_retry_error(self, e: Exception) -> bool:
        """Check if an error should trigger a retry."""
        if isinstance(e, InvalidRequestError):
            error_msg = str(e).lower()
            return any(
                msg in error_msg
                for msg in [
                    "model not found, inaccessible, and/or not deployed",
                    "model does not exist",
                ]
            )
        return isinstance(e, (BadGatewayError, ServiceUnavailableError, RateLimitError))

    @property
    def client(self):  # type: ignore
        return self._client

    def _execute_with_retry(self, params: dict, stream: bool | NotGiven, operation_name: str):
        metric = self._llm.enable_metrics and not stream
        return self._retry_with_backoff(
            self.client.create, **params, operation_name=operation_name, metric=metric
        )  # type: ignore

    async def _execute_with_retry_async(self, params: dict, stream: bool | NotGiven, operation_name: str):
        metric = self._llm.enable_metrics and not stream
        return await self._retry_with_backoff_async(
            self.client.acreate, **params, operation_name=operation_name, metric=metric
        )  # type: ignore

    def _build_common_request_params(
        self,
        model_id: str,
        stream: Optional[bool] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        top_k: Optional[int] | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        repetition_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        reasoning_effort: Optional[ReasoningEffort] | NotGiven = NOT_GIVEN,
        mirostat_lr: Optional[float] | NotGiven = NOT_GIVEN,
        mirostat_target: Optional[float] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        ignore_eos: Optional[bool] | NotGiven = NOT_GIVEN,
        stop: Optional[Union[str, List[str]]] | NotGiven = NOT_GIVEN,
        response_format: Optional[ResponseFormat] | NotGiven = NOT_GIVEN,
        context_length_exceeded_behavior: Optional[str] | NotGiven = NOT_GIVEN,
        user: Optional[str] | NotGiven = NOT_GIVEN,
        perf_metrics_in_response: Optional[bool] | NotGiven = NOT_GIVEN,
        extra_headers=None,
        **kwargs,
    ) -> dict:
        """Build common request parameters shared by both completion types."""
        # Start with required parameters and those that have default handling
        params = {
            "model": model_id,
            **kwargs,
        }

        # Only add optional parameters if they are not NOT_GIVEN
        optional_params = {
            "stream": stream,
            "temperature": temperature,
            "extra_headers": extra_headers,
            "max_tokens": max_tokens,
            "top_p": top_p,
            "top_k": top_k,
            "frequency_penalty": frequency_penalty,
            "presence_penalty": presence_penalty,
            "repetition_penalty": repetition_penalty,
            "reasoning_effort": reasoning_effort,
            "mirostat_lr": mirostat_lr,
            "mirostat_target": mirostat_target,
            "n": n,
            "ignore_eos": ignore_eos,
            "stop": stop,
            "response_format": response_format,
            "context_length_exceeded_behavior": context_length_exceeded_behavior,
            "user": user,
            "perf_metrics_in_response": perf_metrics_in_response,
        }

        # Add only non-NOT_GIVEN optional parameters
        for key, value in optional_params.items():
            if value is not NOT_GIVEN and value is not None:
                params[key] = value

        return params

    @abstractmethod
    def _build_request_params(self, model_id: str, *args, **kwargs) -> dict:
        """Build request parameters - must be implemented by subclasses."""
        pass

    def _retry_with_backoff(
        self,
        func,
        *args,
        operation_name: str = "operation",
        metric: bool = False,
        **kwargs,
    ):
        """DRY helper for retrying sync functions with backoff and optional metrics."""
        retries = 0
        delay = DEFAULT_DELAY
        while retries < self._llm.max_retries:
            try:
                if metric:
                    start_time = time.time()
                result = func(*args, **kwargs)
                if metric:
                    end_time = time.time()
                    self._llm._metrics.add_metric("time_to_last_token", end_time - start_time)
                return result
            except Exception as e:
                if not self._should_retry_error(e):
                    raise e
                logger.debug(f"{type(e).__name__}: {e}. operation: {operation_name}")
                time.sleep(delay)
                retries += 1
                delay *= 2
        raise Exception(f"Failed to create {operation_name} after {self._llm.max_retries} retries")

    async def _retry_with_backoff_async(
        self,
        func,
        *args,
        operation_name: str = "operation",
        metric: bool = False,
        **kwargs,
    ):
        """DRY helper for retrying async functions with backoff and optional metrics."""
        retries = 0
        delay = DEFAULT_DELAY
        while retries <= self._llm.max_retries:
            try:
                if metric:
                    start_time = time.time()
                result = func(*args, **kwargs)
                if kwargs.get("stream", False):
                    if operation_name == "responses":
                        return await result
                    else:
                        return result  # Return generator directly for streaming
                elif metric:
                    result = await result
                    end_time = time.time()
                    self._llm._metrics.add_metric("time_to_last_token", end_time - start_time)
                else:
                    result = await result
                return result
            except Exception as e:
                if not self._should_retry_error(e):
                    raise e
                logger.debug(f"{type(e).__name__}: {e}. operation: {operation_name}")
                await asyncio.sleep(delay)
                retries += 1
                delay *= 2
        raise Exception(f"Failed to create {operation_name} after {self._llm.max_retries} retries")
