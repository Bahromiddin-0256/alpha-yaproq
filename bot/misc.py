import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from django.conf import settings

from bot.helpers import get_webhook_url
from bot.routers import router
from bot.utils.middlewares import authentication, i18n
from bot.utils.storage import DjangoRedisStorage

dp = Dispatcher(storage=DjangoRedisStorage())
bot_session = AiohttpSession()

bot = Bot(settings.BOT_TOKEN, parse_mode="HTML", session=bot_session)

dp.include_router(router)
dp.update.outer_middleware.register(authentication.AuthenticationMiddleware())
dp.update.outer_middleware.register(i18n.I18Middleware())


async def on_startup():
    if settings.SET_WEBHOOK:
        webhook_info = await bot.get_webhook_info()
        webhook_url = get_webhook_url()
        if webhook_url != webhook_info.url:
            await bot.set_webhook(
                url=webhook_url, allowed_updates=dp.resolve_used_update_types(), drop_pending_updates=True
            )


async def on_shutdown():
    await bot_session.close()
