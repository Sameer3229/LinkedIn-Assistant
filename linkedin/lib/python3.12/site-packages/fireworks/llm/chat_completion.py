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
from openai import NotGiven, NOT_GIVEN
from openai.types.chat.chat_completion import ChatCompletion as OpenAIChatCompletion
from openai.types.chat.chat_completion_chunk import ChatCompletionChunk
from openai.types.chat.chat_completion_message_param import ChatCompletionMessageParam
from openai.types.chat.chat_completion_tool_param import ChatCompletionToolParam

from fireworks.client.chat_completion import ChatCompletionV2 as FireworksChatCompletion
from fireworks._literals import ReasoningEffort
from fireworks.llm.base_completion import BaseCompletion

# Type checking imports to avoid circular imports
if TYPE_CHECKING:
    from fireworks.llm.llm import LLM


class ChatCompletion(BaseCompletion):
    def __init__(self, llm: "LLM"):
        super().__init__(llm)
        self._client = FireworksChatCompletion(llm._client)

    @overload
    def create(
        self,
        messages: Iterable[ChatCompletionMessageParam],
        stream: Literal[False] = False,
        response_format: Optional[ResponseFormat] = None,
        reasoning_effort: Optional[ReasoningEffort] = None,
        max_tokens: Optional[int] = None,
        prompt_truncate_len: Optional[int] = None,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
        top_k: Optional[int] = None,
        frequency_penalty: Optional[float] = None,
        presence_penalty: Optional[float] = None,
        repetition_penalty: Optional[float] = None,
        mirostat_lr: Optional[float] = None,
        mirostat_target: Optional[float] = None,
        n: Optional[int] = None,
        ignore_eos: Optional[bool] = None,
        stop: Optional[Union[str, List[str]]] = None,
        context_length_exceeded_behavior: Optional[str] = None,
        user: Optional[str] = None,
        tools: Union[List[ChatCompletionToolParam], NotGiven] = NOT_GIVEN,
        perf_metrics_in_response: Optional[bool] = None,
        extra_headers=None,
        **kwargs,
    ) -> OpenAIChatCompletion:
        pass

    @overload
    def create(
        self,
        messages: Iterable[ChatCompletionMessageParam],
        stream: Literal[True] = True,
        response_format: Optional[ResponseFormat] = None,
        reasoning_effort: Optional[ReasoningEffort] = None,
        max_tokens: Optional[int] = None,
        prompt_truncate_len: Optional[int] = None,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
        top_k: Optional[int] = None,
        frequency_penalty: Optional[float] = None,
        presence_penalty: Optional[float] = None,
        repetition_penalty: Optional[float] = None,
        mirostat_lr: Optional[float] = None,
        mirostat_target: Optional[float] = None,
        n: Optional[int] = None,
        ignore_eos: Optional[bool] = None,
        stop: Optional[Union[str, List[str]]] = None,
        context_length_exceeded_behavior: Optional[str] = None,
        user: Optional[str] = None,
        tools: Union[List[ChatCompletionToolParam], NotGiven] = NOT_GIVEN,
        perf_metrics_in_response: Optional[bool] = None,
        extra_headers=None,
        **kwargs,
    ) -> Generator[ChatCompletionChunk, None, None]:
        pass

    def _build_request_params(
        self,
        model_id: str,
        messages: Iterable[ChatCompletionMessageParam],
        stream: bool = False,
        response_format: Optional[ResponseFormat] = None,
        reasoning_effort: Optional[ReasoningEffort] = None,
        max_tokens: Optional[int] = None,
        prompt_truncate_len: Optional[int] = None,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
        top_k: Optional[int] = None,
        frequency_penalty: Optional[float] = None,
        presence_penalty: Optional[float] = None,
        repetition_penalty: Optional[float] = None,
        mirostat_lr: Optional[float] = None,
        mirostat_target: Optional[float] = None,
        n: Optional[int] = None,
        ignore_eos: Optional[bool] = None,
        stop: Optional[Union[str, List[str]]] = None,
        context_length_exceeded_behavior: Optional[str] = None,
        user: Optional[str] = None,
        tools: Union[List[ChatCompletionToolParam], NotGiven] = NOT_GIVEN,
        perf_metrics_in_response: Optional[bool] = None,
        extra_headers=None,
        **kwargs,
    ) -> dict:
        """Build request parameters for chat completion calls."""
        # Build common parameters using base class method
        params = self._build_common_request_params(
            model_id=model_id,
            stream=stream,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            top_k=top_k,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            repetition_penalty=repetition_penalty,
            reasoning_effort=reasoning_effort,
            mirostat_lr=mirostat_lr,
            mirostat_target=mirostat_target,
            n=n,
            ignore_eos=ignore_eos,
            stop=stop,
            response_format=response_format,
            context_length_exceeded_behavior=context_length_exceeded_behavior,
            user=user,
            perf_metrics_in_response=perf_metrics_in_response,
            extra_headers=extra_headers,
            **kwargs,
        )

        # Add chat completion-specific parameters
        params["messages"] = messages

        # Add optional chat completion-specific parameters if not None
        if prompt_truncate_len is not None:
            params["prompt_truncate_len"] = prompt_truncate_len

        # Only include tools if it's not NotGiven
        if not isinstance(tools, NotGiven):
            params["tools"] = tools

        return params

    def create(
        self,
        messages: Iterable[ChatCompletionMessageParam],
        stream: bool = False,
        response_format: Optional[ResponseFormat] = None,
        reasoning_effort: Optional[ReasoningEffort] = None,
        max_tokens: Optional[int] = None,
        prompt_truncate_len: Optional[int] = None,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
        top_k: Optional[int] = None,
        frequency_penalty: Optional[float] = None,
        presence_penalty: Optional[float] = None,
        repetition_penalty: Optional[float] = None,
        mirostat_lr: Optional[float] = None,
        mirostat_target: Optional[float] = None,
        n: Optional[int] = None,
        ignore_eos: Optional[bool] = None,
        stop: Optional[Union[str, List[str]]] = None,
        context_length_exceeded_behavior: Optional[str] = None,
        user: Optional[str] = None,
        tools: Union[List[ChatCompletionToolParam], NotGiven] = NOT_GIVEN,
        perf_metrics_in_response: Optional[bool] = None,
        extra_headers=None,
        **kwargs,
    ) -> Union[OpenAIChatCompletion, Generator[ChatCompletionChunk, None, None]]:
        if "model" in kwargs:
            raise ValueError(
                "Pass model as a parameter to the constructor of LLM instead of passing it as a parameter to the create method"
            )
        model_id = self._llm.model_id()
        params = self._build_request_params(
            model_id,
            messages,
            stream,
            response_format,
            reasoning_effort,
            max_tokens,
            prompt_truncate_len,
            temperature,
            top_p,
            top_k,
            frequency_penalty,
            presence_penalty,
            repetition_penalty,
            mirostat_lr,
            mirostat_target,
            n,
            ignore_eos,
            stop,
            context_length_exceeded_behavior,
            user,
            tools,
            perf_metrics_in_response,
            extra_headers,
            **kwargs,
        )

        return self._execute_with_retry(params, stream, "chat completion")

    @overload
    async def acreate(
        self,
        messages: Iterable[ChatCompletionMessageParam],
        stream: Literal[False] = False,
        response_format: Optional[ResponseFormat] = None,
        reasoning_effort: Optional[ReasoningEffort] = None,
        max_tokens: Optional[int] = None,
        prompt_truncate_len: Optional[int] = None,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
        top_k: Optional[int] = None,
        frequency_penalty: Optional[float] = None,
        presence_penalty: Optional[float] = None,
        repetition_penalty: Optional[float] = None,
        mirostat_lr: Optional[float] = None,
        mirostat_target: Optional[float] = None,
        n: Optional[int] = None,
        ignore_eos: Optional[bool] = None,
        stop: Optional[Union[str, List[str]]] = None,
        context_length_exceeded_behavior: Optional[str] = None,
        user: Optional[str] = None,
        tools: Union[List[ChatCompletionToolParam], NotGiven] = NOT_GIVEN,
        perf_metrics_in_response: Optional[bool] = None,
        extra_headers=None,
        **kwargs,
    ) -> OpenAIChatCompletion: ...

    @overload
    async def acreate(
        self,
        messages: Iterable[ChatCompletionMessageParam],
        stream: Literal[True] = True,
        response_format: Optional[ResponseFormat] = None,
        reasoning_effort: Optional[ReasoningEffort] = None,
        max_tokens: Optional[int] = None,
        prompt_truncate_len: Optional[int] = None,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
        top_k: Optional[int] = None,
        frequency_penalty: Optional[float] = None,
        presence_penalty: Optional[float] = None,
        repetition_penalty: Optional[float] = None,
        mirostat_lr: Optional[float] = None,
        mirostat_target: Optional[float] = None,
        n: Optional[int] = None,
        ignore_eos: Optional[bool] = None,
        stop: Optional[Union[str, List[str]]] = None,
        context_length_exceeded_behavior: Optional[str] = None,
        user: Optional[str] = None,
        tools: Union[List[ChatCompletionToolParam], NotGiven] = NOT_GIVEN,
        perf_metrics_in_response: Optional[bool] = None,
        extra_headers=None,
        **kwargs,
    ) -> AsyncGenerator[ChatCompletionChunk, None]:
        pass

    async def acreate(
        self,
        messages: Iterable[ChatCompletionMessageParam],
        stream: bool = False,
        response_format: Optional[ResponseFormat] = None,
        reasoning_effort: Optional[ReasoningEffort] = None,
        max_tokens: Optional[int] = None,
        prompt_truncate_len: Optional[int] = None,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
        top_k: Optional[int] = None,
        frequency_penalty: Optional[float] = None,
        presence_penalty: Optional[float] = None,
        repetition_penalty: Optional[float] = None,
        mirostat_lr: Optional[float] = None,
        mirostat_target: Optional[float] = None,
        n: Optional[int] = None,
        ignore_eos: Optional[bool] = None,
        stop: Optional[Union[str, List[str]]] = None,
        context_length_exceeded_behavior: Optional[str] = None,
        user: Optional[str] = None,
        tools: Union[List[ChatCompletionToolParam], NotGiven] = NOT_GIVEN,
        perf_metrics_in_response: Optional[bool] = None,
        extra_headers=None,
        **kwargs,
    ) -> Union[OpenAIChatCompletion, AsyncGenerator[ChatCompletionChunk, None]]:
        if "model" in kwargs:
            raise ValueError(
                "Pass model as a parameter to the constructor of LLM instead of passing it as a parameter to the create method"
            )
        model_id = self._llm.model_id()
        params = self._build_request_params(
            model_id,
            messages,
            stream,
            response_format,
            reasoning_effort,
            max_tokens,
            prompt_truncate_len,
            temperature,
            top_p,
            top_k,
            frequency_penalty,
            presence_penalty,
            repetition_penalty,
            mirostat_lr,
            mirostat_target,
            n,
            ignore_eos,
            stop,
            context_length_exceeded_behavior,
            user,
            tools,
            perf_metrics_in_response,
            extra_headers,
            **kwargs,
        )

        return await self._execute_with_retry_async(params, stream, "chat completion")


class Chat:
    def __init__(self, llm: "LLM", model):
        self.completions = ChatCompletion(llm)
