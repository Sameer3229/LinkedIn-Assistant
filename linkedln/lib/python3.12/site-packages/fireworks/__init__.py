from .llm import LLM
from .dataset import Dataset
from .evaluator import Evaluator
from .supervised_fine_tuning_job import SupervisedFineTuningJob
from .batch_inference_job import BatchInferenceJob
import importlib.metadata
from typing import Callable, NoReturn, Protocol, TypeVar, cast

F = TypeVar("F", bound=Callable[..., object])

class _RewardFunctionDecorator(Protocol):
    def __call__(
        self,
        _func: F | None = None,
        *,
        mode: str = "pointwise",
        id: str | None = None,
        requirements: list[str] | None = None,
    ) -> F | Callable[[F], F]:
        ...

try:
    from reward_kit import reward_function as _reward_function  # type: ignore
    reward_function: _RewardFunctionDecorator = cast(_RewardFunctionDecorator, _reward_function)
except Exception:  # pragma: no cover
    def _reward_function_stub(*args: object, **kwargs: object) -> NoReturn:
        raise ImportError(
            "reward_kit is not installed. Install the extra: `pip install 'fireworks-ai[reward-kit]'` or with uv: `uv pip install 'fireworks-ai[reward-kit]'`."
        )

    reward_function: _RewardFunctionDecorator = cast(_RewardFunctionDecorator, _reward_function_stub)
from openai.types.chat.chat_completion import ChatCompletion
from openai.types.chat.chat_completion_chunk import ChatCompletionChunk
from openai.types.chat.chat_completion_message_param import ChatCompletionMessageParam
from openai.types.chat.chat_completion_tool_param import ChatCompletionToolParam
from .platform import FireworksPlatform
import fireworks.control_plane.generated.protos.gateway as fw
from fireworks._literals import (
    DeploymentTypeLiteral,
    RegionLiteral,
    MultiRegionLiteral,
    AcceleratorTypeLiteral,
    PrecisionLiteral,
    DirectRouteTypeLiteral,
    ReasoningEffort,
)

try:
    __version__ = importlib.metadata.version("fireworks-ai")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.0.0"  # Fallback for development mode

__all__ = [
    "LLM",
    "Dataset",
    "Evaluator",
    "SupervisedFineTuningJob",
    "BatchInferenceJob",
    "FireworksPlatform",
    "fw",
    "__version__",
    "reward_function",
    "ChatCompletion",
    "ChatCompletionChunk",
    "ChatCompletionMessageParam",
    "ChatCompletionToolParam",
    "DeploymentTypeLiteral",
    "RegionLiteral",
    "MultiRegionLiteral",
    "AcceleratorTypeLiteral",
    "PrecisionLiteral",
    "DirectRouteTypeLiteral",
    "ReasoningEffort",
]
