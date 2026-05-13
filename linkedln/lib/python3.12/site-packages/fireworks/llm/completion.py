from typing import (
    AsyncGenerator,
    Generator,
    List,
    Literal,
    Optional,
    Union,
    overload,
    TYPE_CHECKING,
)

from fireworks.llm._types import ResponseFormat
from openai import NotGiven, NOT_GIVEN
from openai.types.completion import Completion as OpenAICompletion
from openai.types.completion_choice import CompletionChoice

from fireworks.client.completion import CompletionV2 as FireworksCompletion
from fireworks._literals import ReasoningEffort
from fireworks.llm.base_completion import BaseCompletion

# Type checking imports to avoid circular imports
if TYPE_CHECKING:
    from fireworks.llm.llm import LLM


class Completion(BaseCompletion):
    def __init__(self, llm: "LLM"):
        super().__init__(llm)
        self._client = FireworksCompletion(llm._client)

    @overload
    def create(
        self,
        prompt: str,
        stream: Literal[False] = False,
        images: Optional[List[str]] = None,
        max_tokens: Optional[int] = None,
        logprobs: Optional[int] = None,
        echo: Optional[bool] = None,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
        top_k: Optional[int] = None,
        frequency_penalty: Optional[float] = None,
        presence_penalty: Optional[float] = None,
        repetition_penalty: Optional[float] = None,
        reasoning_effort: Optional[ReasoningEffort] = None,
        mirostat_lr: Optional[float] = None,
        mirostat_target: Optional[float] = None,
        n: Optional[int] = None,
        ignore_eos: Optional[bool] = None,
        stop: Optional[Union[str, List[str]]] = None,
        response_format: Optional[ResponseFormat] = None,
        context_length_exceeded_behavior: Optional[str] = None,
        user: Optional[str] = None,
        perf_metrics_in_response: Optional[bool] = None,
        extra_headers=None,
        **kwargs,
    ) -> OpenAICompletion:
        pass

    @overload
    def create(
        self,
        prompt: str,
        stream: Literal[True] = True,
        images: Optional[List[str]] = None,
        max_tokens: Optional[int] = None,
        logprobs: Optional[int] = None,
        echo: Optional[bool] = None,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
        top_k: Optional[int] = None,
        frequency_penalty: Optional[float] = None,
        presence_penalty: Optional[float] = None,
        repetition_penalty: Optional[float] = None,
        reasoning_effort: Optional[ReasoningEffort] = None,
        mirostat_lr: Optional[float] = None,
        mirostat_target: Optional[float] = None,
        n: Optional[int] = None,
        ignore_eos: Optional[bool] = None,
        stop: Optional[Union[str, List[str]]] = None,
        response_format: Optional[ResponseFormat] = None,
        context_length_exceeded_behavior: Optional[str] = None,
        user: Optional[str] = None,
        perf_metrics_in_response: Optional[bool] = None,
        extra_headers=None,
        **kwargs,
    ) -> Generator[OpenAICompletion, None, None]:
        pass

    def _build_request_params(
        self,
        model_id: str,
        prompt: str,
        stream: bool = False,
        images: Optional[List[str]] = None,
        max_tokens: Optional[int] = None,
        logprobs: Optional[int] = None,
        echo: Optional[bool] = None,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
        top_k: Optional[int] = None,
        frequency_penalty: Optional[float] = None,
        presence_penalty: Optional[float] = None,
        repetition_penalty: Optional[float] = None,
        reasoning_effort: Optional[ReasoningEffort] = None,
        mirostat_lr: Optional[float] = None,
        mirostat_target: Optional[float] = None,
        n: Optional[int] = None,
        ignore_eos: Optional[bool] = None,
        stop: Optional[Union[str, List[str]]] = None,
        response_format: Optional[ResponseFormat] = None,
        context_length_exceeded_behavior: Optional[str] = None,
        user: Optional[str] = None,
        perf_metrics_in_response: Optional[bool] = None,
        extra_headers=None,
        **kwargs,
    ) -> dict:
        """Build request parameters for completion calls."""
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

        # Add completion-specific parameters
        params["prompt"] = prompt

        # Add optional completion-specific parameters if not None
        completion_optional_params = {
            "images": images,
            "logprobs": logprobs,
            "echo": echo,
        }

        for key, value in completion_optional_params.items():
            if value is not None:
                params[key] = value

        return params

    def create(
        self,
        prompt: str,
        stream: bool = False,
        images: Optional[List[str]] = None,
        max_tokens: Optional[int] = None,
        logprobs: Optional[int] = None,
        echo: Optional[bool] = None,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
        top_k: Optional[int] = None,
        frequency_penalty: Optional[float] = None,
        presence_penalty: Optional[float] = None,
        repetition_penalty: Optional[float] = None,
        reasoning_effort: Optional[ReasoningEffort] = None,
        mirostat_lr: Optional[float] = None,
        mirostat_target: Optional[float] = None,
        n: Optional[int] = None,
        ignore_eos: Optional[bool] = None,
        stop: Optional[Union[str, List[str]]] = None,
        response_format: Optional[ResponseFormat] = None,
        context_length_exceeded_behavior: Optional[str] = None,
        user: Optional[str] = None,
        perf_metrics_in_response: Optional[bool] = None,
        extra_headers=None,
        **kwargs,
    ) -> Union[OpenAICompletion, Generator[OpenAICompletion, None, None]]:
        if "model" in kwargs:
            raise ValueError(
                "Pass model as a parameter to the constructor of LLM instead of passing it as a parameter to the create method"
            )
        model_id = self._llm.model_id()
        params = self._build_request_params(
            model_id,
            prompt,
            stream,
            images,
            max_tokens,
            logprobs,
            echo,
            temperature,
            top_p,
            top_k,
            frequency_penalty,
            presence_penalty,
            repetition_penalty,
            reasoning_effort,
            mirostat_lr,
            mirostat_target,
            n,
            ignore_eos,
            stop,
            response_format,
            context_length_exceeded_behavior,
            user,
            perf_metrics_in_response,
            extra_headers,
            **kwargs,
        )

        return self._execute_with_retry(params, stream, "completion")

    @overload
    async def acreate(
        self,
        prompt: str,
        stream: Literal[False] = False,
        images: Optional[List[str]] = None,
        max_tokens: Optional[int] = None,
        logprobs: Optional[int] = None,
        echo: Optional[bool] = None,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
        top_k: Optional[int] = None,
        frequency_penalty: Optional[float] = None,
        presence_penalty: Optional[float] = None,
        repetition_penalty: Optional[float] = None,
        reasoning_effort: Optional[ReasoningEffort] = None,
        mirostat_lr: Optional[float] = None,
        mirostat_target: Optional[float] = None,
        n: Optional[int] = None,
        ignore_eos: Optional[bool] = None,
        stop: Optional[Union[str, List[str]]] = None,
        response_format: Optional[ResponseFormat] = None,
        context_length_exceeded_behavior: Optional[str] = None,
        user: Optional[str] = None,
        perf_metrics_in_response: Optional[bool] = None,
        extra_headers=None,
        **kwargs,
    ) -> OpenAICompletion: ...

    @overload
    async def acreate(
        self,
        prompt: str,
        stream: Literal[True] = True,
        images: Optional[List[str]] = None,
        max_tokens: Optional[int] = None,
        logprobs: Optional[int] = None,
        echo: Optional[bool] = None,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
        top_k: Optional[int] = None,
        frequency_penalty: Optional[float] = None,
        presence_penalty: Optional[float] = None,
        repetition_penalty: Optional[float] = None,
        reasoning_effort: Optional[ReasoningEffort] = None,
        mirostat_lr: Optional[float] = None,
        mirostat_target: Optional[float] = None,
        n: Optional[int] = None,
        ignore_eos: Optional[bool] = None,
        stop: Optional[Union[str, List[str]]] = None,
        response_format: Optional[ResponseFormat] = None,
        context_length_exceeded_behavior: Optional[str] = None,
        user: Optional[str] = None,
        perf_metrics_in_response: Optional[bool] = None,
        extra_headers=None,
        **kwargs,
    ) -> AsyncGenerator[OpenAICompletion, None]:
        pass

    async def acreate(
        self,
        prompt: str,
        stream: bool = False,
        images: Optional[List[str]] = None,
        max_tokens: Optional[int] = None,
        logprobs: Optional[int] = None,
        echo: Optional[bool] = None,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
        top_k: Optional[int] = None,
        frequency_penalty: Optional[float] = None,
        presence_penalty: Optional[float] = None,
        repetition_penalty: Optional[float] = None,
        reasoning_effort: Optional[ReasoningEffort] = None,
        mirostat_lr: Optional[float] = None,
        mirostat_target: Optional[float] = None,
        n: Optional[int] = None,
        ignore_eos: Optional[bool] = None,
        stop: Optional[Union[str, List[str]]] = None,
        response_format: Optional[ResponseFormat] = None,
        context_length_exceeded_behavior: Optional[str] = None,
        user: Optional[str] = None,
        perf_metrics_in_response: Optional[bool] = None,
        extra_headers=None,
        **kwargs,
    ) -> Union[OpenAICompletion, AsyncGenerator[OpenAICompletion, None]]:
        model_id = self._llm.model_id()
        params = self._build_request_params(
            model_id,
            prompt,
            stream,
            images,
            max_tokens,
            logprobs,
            echo,
            temperature,
            top_p,
            top_k,
            frequency_penalty,
            presence_penalty,
            repetition_penalty,
            reasoning_effort,
            mirostat_lr,
            mirostat_target,
            n,
            ignore_eos,
            stop,
            response_format,
            context_length_exceeded_behavior,
            user,
            perf_metrics_in_response,
            extra_headers,
            **kwargs,
        )

        return await self._execute_with_retry_async(params, stream, "completion")
