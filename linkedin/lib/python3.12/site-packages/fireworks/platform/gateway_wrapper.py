import functools
from fireworks.control_plane.generated.protos.gateway import GatewayStub


class GatewayWrapper(GatewayStub):
    def __init__(self, *args, account_id: str, **kwargs):
        super().__init__(*args, **kwargs)

        if not account_id:
            raise ValueError("account_id must be provided and not")

        self.parent = f"accounts/{account_id}"

        # go through every method on self and wrap it
        for method_name in dir(self):
            if method_name.startswith("_"):
                continue
            method = getattr(self, method_name)
            if callable(method):
                setattr(self, method_name, self.wrap_method(method))

    def wrap_method(self, method):
        @functools.wraps(method)
        async def wrapper(*args, **kwargs):
            # if args[0] has attribute "parent"
            if hasattr(args[0], "parent"):
                args[0].parent = self.parent
            return await method(*args, **kwargs)

        return wrapper
