from typing import (
    AsyncGenerator,
    Generator,
    Iterable,
    List,
    Literal,
    Optional,
    Union,
    overload,
    TYPE_CHECKING,
)

from fireworks.llm._types import ResponseFormat
from openai import AsyncOpenAI, NotGiven, NOT_GIVEN
from openai.types.responses import Response as OpenAIResponse
from openai.types.responses import ResponseStreamEvent
from openai.types.responses import ResponseCreateParams
from openai.types.responses import ResponseInputParam
from openai.types.responses import ResponseTextConfigParam
from openai.types.responses import ResponseIncludable
from openai.types.responses import ToolParam
from openai.types.shared_params.metadata import Metadata
from openai.types.shared_params.reasoning import Reasoning
from openai.types.shared_params.responses_model import ResponsesModel
from openai.types.responses.response_create_params import ToolChoice
from openai._streaming import Stream, AsyncStream

from fireworks._literals import ReasoningEffort
from fireworks.llm.base_completion import BaseCompletion

# Type checking imports to avoid circular imports
if TYPE_CHECKING:
    from fireworks.llm.llm import LLM


class Responses(BaseCompletion):
    def __init__(self, llm: "LLM"):
        super().__init__(llm)
        # Import OpenAI client here to avoid circular imports
        from openai import OpenAI

        self._openai_client = OpenAI(
            api_key=llm._client.api_key,
            base_url=str(llm._client.base_url),
            max_retries=llm.max_retries,
        )
        self._openai_client_async = AsyncOpenAI(
            api_key=llm._client.api_key,
            base_url=str(llm._client.base_url),
            max_retries=llm.max_retries,
        )

    @overload
    def create(
        self,
        *,
        input: Union[str, ResponseInputParam],
        include: Optional[List[ResponseIncludable]] | NotGiven = NOT_GIVEN,
        instructions: Optional[str] | NotGiven = NOT_GIVEN,
        max_output_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        metadata: Optional[Metadata] | NotGiven = NOT_GIVEN,
        parallel_tool_calls: Optional[bool] | NotGiven = NOT_GIVEN,
        previous_response_id: Optional[str] | NotGiven = NOT_GIVEN,
        reasoning: Optional[Reasoning] | NotGiven = NOT_GIVEN,
        service_tier: Optional[Literal["auto", "default", "flex"]] | NotGiven = NOT_GIVEN,
        store: Optional[bool] | NotGiven = NOT_GIVEN,
        stream: Optional[Literal[False]] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        text: ResponseTextConfigParam | NotGiven = NOT_GIVEN,
        tool_choice: ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[ToolParam] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        truncation: Optional[Literal["auto", "disabled"]] | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        extra_headers=None,
        **kwargs,
    ) -> OpenAIResponse:
        pass

    @overload
    def create(
        self,
        *,
        input: Union[str, ResponseInputParam],
        stream: Literal[True],
        include: Optional[List[ResponseIncludable]] | NotGiven = NOT_GIVEN,
        instructions: Optional[str] | NotGiven = NOT_GIVEN,
        max_output_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        metadata: Optional[Metadata] | NotGiven = NOT_GIVEN,
        parallel_tool_calls: Optional[bool] | NotGiven = NOT_GIVEN,
        previous_response_id: Optional[str] | NotGiven = NOT_GIVEN,
        reasoning: Optional[Reasoning] | NotGiven = NOT_GIVEN,
        service_tier: Optional[Literal["auto", "default", "flex"]] | NotGiven = NOT_GIVEN,
        store: Optional[bool] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        text: ResponseTextConfigParam | NotGiven = NOT_GIVEN,
        tool_choice: ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[ToolParam] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        truncation: Optional[Literal["auto", "disabled"]] | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        extra_headers=None,
        **kwargs,
    ) -> Stream[ResponseStreamEvent]:
        pass

    def create(
        self,
        *,
        input: Union[str, ResponseInputParam],
        include: Optional[List[ResponseIncludable]] | NotGiven = NOT_GIVEN,
        instructions: Optional[str] | NotGiven = NOT_GIVEN,
        max_output_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        metadata: Optional[Metadata] | NotGiven = NOT_GIVEN,
        parallel_tool_calls: Optional[bool] | NotGiven = NOT_GIVEN,
        previous_response_id: Optional[str] | NotGiven = NOT_GIVEN,
        reasoning: Optional[Reasoning] | NotGiven = NOT_GIVEN,
        service_tier: Optional[Literal["auto", "default", "flex"]] | NotGiven = NOT_GIVEN,
        store: Optional[bool] | NotGiven = NOT_GIVEN,
        stream: Optional[bool] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        text: ResponseTextConfigParam | NotGiven = NOT_GIVEN,
        tool_choice: ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[ToolParam] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        truncation: Optional[Literal["auto", "disabled"]] | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        extra_headers=None,
        **kwargs,
    ) -> Union[OpenAIResponse, Stream[ResponseStreamEvent]]:
        if "model" in kwargs:
            raise ValueError(
                "Pass model as a parameter to the constructor of LLM instead of passing it as a parameter to the create method"
            )
        model_id = self._llm.model_id()
        params = self._build_request_params(
            model_id,
            input,
            stream,
            include,
            instructions,
            max_output_tokens,
            metadata,
            parallel_tool_calls,
            previous_response_id,
            reasoning,
            service_tier,
            store,
            temperature,
            text,
            tool_choice,
            tools,
            top_p,
            truncation,
            user,
            extra_headers,
            **kwargs,
        )

        return self._execute_with_retry(params, "responses")

    @overload
    async def acreate(
        self,
        *,
        input: Union[str, ResponseInputParam],
        include: Optional[List[ResponseIncludable]] | NotGiven = NOT_GIVEN,
        instructions: Optional[str] | NotGiven = NOT_GIVEN,
        max_output_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        metadata: Optional[Metadata] | NotGiven = NOT_GIVEN,
        parallel_tool_calls: Optional[bool] | NotGiven = NOT_GIVEN,
        previous_response_id: Optional[str] | NotGiven = NOT_GIVEN,
        reasoning: Optional[Reasoning] | NotGiven = NOT_GIVEN,
        service_tier: Optional[Literal["auto", "default", "flex"]] | NotGiven = NOT_GIVEN,
        store: Optional[bool] | NotGiven = NOT_GIVEN,
        stream: Optional[Literal[False]] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        text: ResponseTextConfigParam | NotGiven = NOT_GIVEN,
        tool_choice: ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[ToolParam] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        truncation: Optional[Literal["auto", "disabled"]] | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        extra_headers=None,
        **kwargs,
    ) -> OpenAIResponse:
        pass

    @overload
    async def acreate(
        self,
        *,
        input: Union[str, ResponseInputParam],
        stream: Literal[True],
        include: Optional[List[ResponseIncludable]] | NotGiven = NOT_GIVEN,
        instructions: Optional[str] | NotGiven = NOT_GIVEN,
        max_output_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        metadata: Optional[Metadata] | NotGiven = NOT_GIVEN,
        parallel_tool_calls: Optional[bool] | NotGiven = NOT_GIVEN,
        previous_response_id: Optional[str] | NotGiven = NOT_GIVEN,
        reasoning: Optional[Reasoning] | NotGiven = NOT_GIVEN,
        service_tier: Optional[Literal["auto", "default", "flex"]] | NotGiven = NOT_GIVEN,
        store: Optional[bool] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        text: ResponseTextConfigParam | NotGiven = NOT_GIVEN,
        tool_choice: ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[ToolParam] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        truncation: Optional[Literal["auto", "disabled"]] | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        extra_headers=None,
        **kwargs,
    ) -> AsyncStream[ResponseStreamEvent]:
        pass

    async def acreate(
        self,
        *,
        input: Union[str, ResponseInputParam],
        include: Optional[List[ResponseIncludable]] | NotGiven = NOT_GIVEN,
        instructions: Optional[str] | NotGiven = NOT_GIVEN,
        max_output_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        metadata: Optional[Metadata] | NotGiven = NOT_GIVEN,
        parallel_tool_calls: Optional[bool] | NotGiven = NOT_GIVEN,
        previous_response_id: Optional[str] | NotGiven = NOT_GIVEN,
        reasoning: Optional[Reasoning] | NotGiven = NOT_GIVEN,
        service_tier: Optional[Literal["auto", "default", "flex"]] | NotGiven = NOT_GIVEN,
        store: Optional[bool] | NotGiven = NOT_GIVEN,
        stream: Optional[bool] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        text: ResponseTextConfigParam | NotGiven = NOT_GIVEN,
        tool_choice: ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[ToolParam] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        truncation: Optional[Literal["auto", "disabled"]] | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        extra_headers=None,
        **kwargs,
    ) -> Union[OpenAIResponse, AsyncStream[ResponseStreamEvent]]:
        if "model" in kwargs:
            raise ValueError(
                "Pass model as a parameter to the constructor of LLM instead of passing it as a parameter to the create method"
            )
        model_id = self._llm.model_id()
        params = self._build_request_params(
            model_id,
            input,
            stream,
            include,
            instructions,
            max_output_tokens,
            metadata,
            parallel_tool_calls,
            previous_response_id,
            reasoning,
            service_tier,
            store,
            temperature,
            text,
            tool_choice,
            tools,
            top_p,
            truncation,
            user,
            extra_headers,
            **kwargs,
        )

        return await self._execute_with_retry_async(params, "responses")

    def _execute_with_retry(self, params: dict, operation_name: str):
        metric = self._llm.enable_metrics and not params.get("stream", False)
        return self._retry_with_backoff(
            self._openai_client.responses.create,
            **params,
            operation_name=operation_name,
            metric=metric,
        )

    async def _execute_with_retry_async(self, params: dict, operation_name: str):
        metric = self._llm.enable_metrics and not params.get("stream", False)
        return await self._retry_with_backoff_async(
            self._openai_client_async.responses.create,
            **params,
            operation_name=operation_name,
            metric=metric,
        )

    def _build_request_params(
        self,
        model_id: str,
        input: Union[str, ResponseInputParam],
        stream: Optional[bool] | NotGiven = NOT_GIVEN,
        include: Optional[List[ResponseIncludable]] | NotGiven = NOT_GIVEN,
        instructions: Optional[str] | NotGiven = NOT_GIVEN,
        max_output_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        metadata: Optional[Metadata] | NotGiven = NOT_GIVEN,
        parallel_tool_calls: Optional[bool] | NotGiven = NOT_GIVEN,
        previous_response_id: Optional[str] | NotGiven = NOT_GIVEN,
        reasoning: Optional[Reasoning] | NotGiven = NOT_GIVEN,
        service_tier: Optional[Literal["auto", "default", "flex"]] | NotGiven = NOT_GIVEN,
        store: Optional[bool] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        text: ResponseTextConfigParam | NotGiven = NOT_GIVEN,
        tool_choice: ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[ToolParam] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        truncation: Optional[Literal["auto", "disabled"]] | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        extra_headers=None,
        **kwargs,
    ) -> dict:
        """Build request parameters for responses calls."""
        # Build common parameters using base class method
        params = self._build_common_request_params(
            model_id=model_id,
            stream=stream,
            max_tokens=max_output_tokens,
            temperature=temperature,
            top_p=top_p,
            extra_headers=extra_headers,
            **kwargs,
        )

        # Add responses-specific parameters
        params["input"] = input
        params["model"] = model_id

        # Add optional responses-specific parameters if not NOT_GIVEN
        optional_params = {
            "include": include,
            "instructions": instructions,
            "metadata": metadata,
            "parallel_tool_calls": parallel_tool_calls,
            "previous_response_id": previous_response_id,
            "reasoning": reasoning,
            "service_tier": service_tier,
            "store": store,
            "text": text,
            "tool_choice": tool_choice,
            "tools": tools,
            "truncation": truncation,
            "user": user,
        }

        for key, value in optional_params.items():
            if value is not NOT_GIVEN:
                params[key] = value

        return params
