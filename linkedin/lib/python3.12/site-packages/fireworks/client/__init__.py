import os
from .completion import Completion
from .chat_completion import ChatCompletion
from .embedding import Embedding
from .rerank import Rerank
from .chat import Chat
from .model import Model
from .api_client_v2 import (
    Fireworks,
    AsyncFireworks,
)
import importlib.metadata

try:
    __version__ = importlib.metadata.version("fireworks-ai")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.0.0"  # Fallback for development mode

api_key = os.environ.get("FIREWORKS_API_KEY")
base_url = os.environ.get("FIREWORKS_API_BASE", "https://api.fireworks.ai/inference/v1")

__all__ = [
    "__version__",
    "AsyncFireworks",
    "Chat",
    "ChatCompletion",
    "Completion",
    "Fireworks",
    "Model",
    "Embedding",
    "Rerank",
]
