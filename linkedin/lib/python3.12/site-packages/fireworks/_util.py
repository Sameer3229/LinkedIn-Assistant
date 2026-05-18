import asyncio
import os
import re
import textwrap
from typing import List, Optional, TypeVar

import toml

T = TypeVar("T")


def generate_resource_name(resource: str, account: str, id: str):
    return f"accounts/{account}/{resource}/{id}"


def generate_model_resource_name(account: str, id: str):
    return generate_resource_name("models", account, id)


def is_valid_resource_name(name: str):
    """
    Fireworks only allows lowercase alphanumeric characters and hyphens in its resource name
    """
    return re.match(r"^[a-z0-9-]+$", name)


def make_valid_resource_name(name: str):
    """
    Fireworks only allows lowercase alphanumeric characters and hyphens in its resource name
    """
    return re.sub(r"[^a-z0-9-]", "-", name)


def find_requirements_or_pyproject(file_path: Optional[str]):
    """
    Iteratively find the requirements.txt or pyproject.toml file in the directory tree.
    """
    while file_path:
        if os.path.exists(os.path.join(file_path, "requirements.txt")):
            return os.path.join(file_path, "requirements.txt")
        if os.path.exists(os.path.join(file_path, "pyproject.toml")):
            return os.path.join(file_path, "pyproject.toml")
        file_path = os.path.dirname(file_path)
    return None


def get_requirements_from_pyproject_or_requirements_txt(file_path: Optional[str]) -> Optional[str]:
    if file_path is None:
        return None
    if file_path.endswith("pyproject.toml"):
        return convert_pyproject_dependencies_to_requirements_txt(get_requirements_from_pyproject(file_path))
    if file_path.endswith("requirements.txt"):
        return open(file_path).read()


def get_requirements_from_pyproject(pyproject_path: str) -> List[str]:
    with open(pyproject_path, "r") as f:
        pyproject = toml.loads(f.read())
    return pyproject["project"]["dependencies"]


def convert_pyproject_dependencies_to_requirements_txt(dependencies: List[str]):
    return "\n".join(dependencies)


def dedent_code(code: str) -> str:
    """
    Remove leading whitespace from code while preserving relative indentation.

    Args:
        code: The indented code string

    Returns:
        Code string with leading whitespace removed but relative indentation preserved

    Example:
        >>> code = '''
        ...     @reward_function
        ...     def evaluate(messages):
        ...         return {"score": 1.0, "reason": "test"}
        ... '''
        >>> print(dedent_code(code))
        @reward_function
        def evaluate(messages):
            return {"score": 1.0, "reason": "test"}
    """
    return textwrap.dedent(code).strip()


def generate_time_str(minutes: int, seconds: int) -> str:
    if minutes == 0:
        return f"{seconds}s"
    return f"{minutes}m{seconds}s"


def get_api_key_from_env() -> Optional[str]:
    """
    Attempts to obtain API key from the environment variable.

    Returns:
        API key retrieved from env variable or None if missing.
    """
    return os.environ.get("FIREWORKS_API_KEY")


def is_running_in_async_context() -> bool:
    """
    Check if the current code is running in an async context with a running event loop.

    Returns:
        True if running in an async context, False otherwise.

    Example:
        >>> if is_running_in_async_context():
        ...     # We're in an async function or callback
        ...     pass
        ... else:
        ...     # We're in a sync context
        ...     pass
    """
    try:
        asyncio.get_running_loop()
        return True
    except RuntimeError:
        # No running event loop - we're in a sync context
        return False
