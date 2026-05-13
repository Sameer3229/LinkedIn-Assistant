# Configure logger with a consistent format for better debugging
import logging
import os
import time
import functools
import inspect
import sys

logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger("fireworks-ai")
handler = logging.StreamHandler(sys.stdout)  # Explicitly use stdout instead of stderr
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.propagate = False  # Prevent duplicate logs

if os.environ.get("FIREWORKS_SDK_DEBUG"):
    logger.setLevel(logging.DEBUG)
else:
    # default to warning level so that we don't spam the console
    logger.setLevel(logging.WARNING)


def log_execution_time(func):
    @functools.wraps(func)
    async def async_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = await func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        logger.debug(f"Function {func.__name__} took {execution_time:.4f} seconds to execute")
        return result

    @functools.wraps(func)
    def sync_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        logger.debug(f"Function {func.__name__} took {execution_time:.4f} seconds to execute")
        return result

    if inspect.iscoroutinefunction(func):
        return async_wrapper
    return sync_wrapper
