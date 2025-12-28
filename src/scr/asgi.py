import typing


Application_V3 = typing.Callable[
    [
        dict,
        typing.Callable[[], typing.Awaitable[dict]],
        typing.Callable[[dict], typing.Awaitable[None]],
    ],
    typing.Awaitable[None],
]


Application_V2 = typing.Callable[
    [dict],
    typing.Callable[
        [
            typing.Callable[[], typing.Awaitable[dict]],
            typing.Callable[[dict], typing.Awaitable[None]],
        ],
        typing.Awaitable[None],
    ],
]


Application = Application_V3 | Application_V2


async def app(scope: dict, receive: typing.Callable, send: typing.Callable):
    """
    ASGI entrypoint that gets the real app from saucer
    """
    from . import root  # noqa: PLC0415

    real_app = await root.aget(Application)
    # FIXME: Support ASGI2
    return await real_app(scope, receive, send)
