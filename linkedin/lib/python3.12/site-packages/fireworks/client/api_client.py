import asyncio
import atexit
import json
import aiohttp
import httpx
from typing import Callable, Dict, Any, Optional, Generator, Union, AsyncGenerator
import httpx_sse
from .._util import is_running_in_async_context
from .error import (
    AuthenticationError,
    APITimeoutError,
    BadGatewayError,
    InternalServerError,
    InvalidRequestError,
    PermissionError,
    RateLimitError,
    ServiceUnavailableError,
)


# Helper functions for api key and base url prevent cyclic dependencies
def default_api_key() -> str:
    from fireworks.client import api_key

    if api_key is not None:
        return api_key
    else:
        raise ValueError(
            "No API key provided. You can set your API key in code using 'fireworks.client.api_key = <API-KEY>', or you can set the environment variable FIREWORKS_API_KEY=<API-KEY>)."
        )


def default_base_url() -> str:
    from fireworks.client import base_url

    return base_url


# Based on benchmark results, 1000 connections is a good balance between
# performance and not overloading the server.
DEFAULT_AIOHTTP_CONNECTOR_LIMIT = 1_000


class FireworksClient:
    """
    Fireworks client class for handling HTTP requests to the Fireworks API.

    Supports both synchronous and asynchronous operations with streaming and
    non-streaming responses. Uses httpx for primary HTTP operations and aiohttp
    as an alternative for specific async use cases since aiohttp is better in
    highly concurrent workloads, which is important when maximizing performance
    for dedicated deployments on Fireworks.
    """

    def __init__(
        self,
        request_timeout=600,
        *,
        api_key: Union[str, None] = None,
        base_url: Union[str, httpx.URL, None] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        max_connections: Optional[int] = None,
        **kwargs,
    ) -> None:
        """Initialize the Fireworks client.

        Args:
            request_timeout: Request timeout in seconds. Defaults to 600.
            api_key: Fireworks API key. If not provided, will use the global api_key.
            base_url: Base URL for API requests. If not provided, will use the global base_url.
            extra_headers: Additional headers to include in all requests.
            **kwargs: Additional arguments passed to the underlying HTTP clients.
        """
        if "request_timeout" in kwargs:
            request_timeout = kwargs["request_timeout"]
        self.api_key = api_key or default_api_key()
        if not self.api_key:
            raise AuthenticationError(
                "No API key provided. You can set your API key in code using 'fireworks.client.api_key = <API-KEY>', or you can set the environment variable FIREWORKS_API_KEY=<API-KEY>)."
            )
        self.base_url = base_url or default_base_url()
        self.request_timeout = request_timeout
        self.max_connections = max_connections
        self.client_kwargs = kwargs
        self.extra_headers = extra_headers or {}
        self._client: httpx.Client = self.create_client(extra_headers=self.extra_headers)
        self._async_client: httpx.AsyncClient = self.create_async_client(extra_headers=self.extra_headers)
        self._aiohttp_session: Optional[aiohttp.ClientSession] = self.create_aiohttp_client_session(
            extra_headers=self.extra_headers
        )

    def _raise_for(self, status_code: int, error_message: Callable[[], str]):
        if status_code == 400:
            raise InvalidRequestError(error_message())
        elif status_code == 401:
            raise AuthenticationError(error_message())
        elif status_code == 403:
            raise PermissionError(error_message())
        elif status_code == 404:
            raise InvalidRequestError(error_message())
        elif status_code == 408:
            raise APITimeoutError(error_message())
        elif status_code == 429:
            raise RateLimitError(error_message())
        elif status_code == 500:
            raise InternalServerError(error_message())
        elif status_code == 502:
            raise BadGatewayError(error_message())
        elif status_code == 503:
            raise ServiceUnavailableError(error_message())

    def _raise_for_status(self, response: Union[httpx.Response, aiohttp.ClientResponse], response_text: str = ""):
        """
        Raises an error if the response status code is not 200. Handles both
        httpx and aiohttp responses.

        Args:
            response: The response object from the HTTP client.
            response_text: The text of the response.
        """

        # Function to get error message or default to response code name
        def get_error_message() -> str:
            # Try to get error message from response_text first (for aiohttp)
            if response_text:
                try:
                    # Validate it's valid JSON
                    json.loads(response_text)
                    return response_text
                except (json.JSONDecodeError, ValueError):
                    pass

            # Try to get error message from response.json() (for httpx)
            try:
                if isinstance(response, httpx.Response):
                    return json.dumps(response.json())
                else:
                    # since we can't call "await" on response.json() for aiohttp, return response_text if non-empty
                    if response_text:
                        return response_text
            except (json.JSONDecodeError, AttributeError):
                pass

            # If JSON parsing fails, return the HTTP status code name
            if isinstance(response, httpx.Response):
                status_code = response.status_code
                reason = response.reason_phrase
            else:
                status_code = response.status
                reason = response.reason

            if 400 <= status_code < 500:
                error_type = "invalid_request_error"
            elif 500 <= status_code < 600:
                error_type = "internal_server_error"
            else:
                error_type = "unknown_error"
            return json.dumps(
                {
                    "error": {
                        "object": "error",
                        "type": error_type,
                        "message": reason,
                    }
                }
            )

        status_code = response.status_code if isinstance(response, httpx.Response) else response.status
        self._raise_for(status_code, get_error_message)

        # if our implementation did not catch the error, let aiohttp or httpx handle it
        response.raise_for_status()

    async def _async_error_handling(
        self, resp: Union[httpx.Response, aiohttp.ClientResponse], response_text: str = ""
    ):
        # Handle httpx async responses
        if isinstance(resp, httpx.Response) and resp.is_error:
            await resp.aread()
        # Handle aiohttp responses
        elif isinstance(resp, aiohttp.ClientResponse) and resp.status >= 400:
            response_text = await resp.text()
        self._raise_for_status(resp, response_text)

    def _error_handling(self, resp):
        if resp.is_error:
            resp.read()
        self._raise_for_status(resp)

    def _get_request(self, url: str, extra_headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        resp = self._client.get(url, headers=self._build_headers(extra_headers))
        self._error_handling(resp)
        return resp.json()

    def _build_headers(self, extra_headers: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        """Build headers with authorization and any extra headers.

        Args:
            extra_headers: Additional headers to merge with the authorization header and
                          instance extra_headers.

        Returns:
            Dictionary containing the Authorization header and any extra headers.
        """
        headers = {"Authorization": f"Bearer {self.api_key}"}
        # Start with instance extra_headers
        headers.update(self.extra_headers)
        # Then add any additional headers passed to this method
        if extra_headers:
            headers.update(extra_headers)
        return headers

    def post_request_streaming(
        self,
        url: str,
        data: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
    ) -> Generator[str, None, None]:
        """Make a streaming POST request.

        Args:
            url: The endpoint URL to send the request to.
            data: JSON data to send in the request body.
            extra_headers: Additional headers to include in the request.

        Yields:
            Server-sent event data as strings.
        """
        with httpx_sse.connect_sse(
            self._client,
            url=url,
            method="POST",
            json=data,
            headers=self._build_headers(extra_headers),
        ) as event_source:
            self._error_handling(event_source.response)
            for sse in event_source.iter_sse():
                yield sse.data

    def post_request_non_streaming(
        self,
        url: str,
        data: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """Make a non-streaming POST request.

        Args:
            url: The endpoint URL to send the request to.
            data: JSON data to send in the request body.
            extra_headers: Additional headers to include in the request.

        Returns:
            JSON response data as a dictionary.
        """
        response = self._client.post(url, json=data, headers=self._build_headers(extra_headers))
        self._error_handling(response)
        return response.json()

    async def post_request_async_streaming(
        self,
        url: str,
        data: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
    ) -> AsyncGenerator[str, None]:
        """Make an async streaming POST request.

        Args:
            url: The endpoint URL to send the request to.
            data: JSON data to send in the request body.
            extra_headers: Additional headers to include in the request.

        Yields:
            Server-sent event data as strings.
        """
        async with httpx_sse.aconnect_sse(
            self._async_client,
            url=url,
            method="POST",
            json=data,
            headers=self._build_headers(extra_headers),
        ) as event_source:
            await self._async_error_handling(event_source.response)
            async for sse in event_source.aiter_sse():
                yield sse.data

    async def post_request_async_non_streaming(
        self,
        url: str,
        data: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """Make an async non-streaming POST request using httpx.

        Args:
            url: The endpoint URL to send the request to.
            data: JSON data to send in the request body.
            extra_headers: Additional headers to include in the request.

        Returns:
            JSON response data as a dictionary.
        """
        # Check if we're in an async context with a running event loop
        if is_running_in_async_context() and self._aiohttp_session is None:
            self._aiohttp_session = self.create_aiohttp_client_session(extra_headers)
        if self._aiohttp_session is None:
            raise ValueError("Aiohttp client session is not initialized, likely due to a non-async context")
        async with self._aiohttp_session.post(url, json=data, headers=self._build_headers(extra_headers)) as resp:
            await self._async_error_handling(resp)
            return await resp.json()

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.close()

    def close(self):
        self._client.close()

    async def __aenter__(self):
        return self

    async def __aexit__(self, *exc):
        await self.aclose()

    async def aclose(self):
        await self._async_client.aclose()
        if self._aiohttp_session is not None:
            await self._aiohttp_session.close()

    def create_client(self, extra_headers: Optional[Dict[str, str]] = None) -> httpx.Client:
        return httpx.Client(
            headers=self._build_headers(extra_headers),
            timeout=self.request_timeout,
            **self.client_kwargs,
        )

    def create_async_client(self, extra_headers: Optional[Dict[str, str]] = None) -> httpx.AsyncClient:
        return httpx.AsyncClient(
            headers=self._build_headers(extra_headers),
            timeout=self.request_timeout,
            **self.client_kwargs,
        )

    def create_aiohttp_client_session(
        self, extra_headers: Optional[Dict[str, str]] = None
    ) -> Optional[aiohttp.ClientSession]:
        # Check if we're in an async context with a running event loop
        if not is_running_in_async_context():
            return None

        max_connections = self.max_connections or DEFAULT_AIOHTTP_CONNECTOR_LIMIT
        connector = aiohttp.TCPConnector(limit=max_connections)
        timeout = aiohttp.ClientTimeout(total=self.request_timeout)
        return aiohttp.ClientSession(
            connector=connector,
            headers=self._build_headers(extra_headers),
            timeout=timeout,
            **self.client_kwargs,
        )
