# Copyright (c) Fireworks AI, Inc. and affiliates.
#
# All Rights Reserved.

from typing import Optional

from fireworks._const import FIREWORKS_API_BASE_URL, FIREWORKS_GATEWAY_ADDR
from fireworks._util import get_api_key_from_env
from fireworks.platform.gateway_wrapper import GatewayWrapper
from fireworks.control_plane.generated.protos.gateway import GatewayStub
import grpc
from grpclib.client import Channel
import httpx
from functools import cache as sync_cache


class FireworksPlatform:
    """
    Platform client that exposes all its endpoints.
    """

    def __init__(
        self,
        *,
        server_addr: str = FIREWORKS_GATEWAY_ADDR,
        api_key: Optional[str] = None,
    ) -> None:
        """
        Args:
            server_addr: the network address of the gateway server.
            api_key: the API key to use for authentication.
        """
        self._server_addr = server_addr
        if not api_key:
            api_key = get_api_key_from_env()
            if not api_key:
                raise ValueError(
                    "Fireworks API key not found. Please provide an API key either as a parameter "
                    "or by setting the FIREWORKS_API_KEY environment variable. "
                    "You can create a new API key at https://fireworks.ai/settings/users/api-keys or "
                    "by using `firectl create api-key --key-name <key-name>` command."
                )
        self._api_key = api_key
        self._host = self._server_addr.split(":")[0]
        self._port = int(self._server_addr.split(":")[1])
        self._channel = Channel(host=self._host, port=self._port, ssl=True)
        self.client = GatewayWrapper(self._channel, metadata=[("x-api-key", api_key)], account_id=self.account_id())

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self._channel.close()

    @sync_cache
    def account_id(self) -> str:
        # make curl -v -H "Authorization: Bearer XXX" https://api.fireworks.ai/verifyApiKey
        # and read x-fireworks-account-id from headers of the response
        with httpx.Client() as client:
            response = client.get(
                f"{FIREWORKS_API_BASE_URL}/verifyApiKey",
                headers={
                    "Authorization": f"Bearer {self._api_key}",
                },
            )
            return response.headers["x-fireworks-account-id"]
