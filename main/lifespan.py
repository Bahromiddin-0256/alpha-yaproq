import contextlib

from bot.misc import on_shutdown as bot_on_shutdown
from bot.misc import on_startup as bot_on_startup


@contextlib.asynccontextmanager
async def lifespan_context():
    try:
        await bot_on_startup()
        yield
    finally:
        await bot_on_shutdown()
