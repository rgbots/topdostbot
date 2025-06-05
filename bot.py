import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.aiohttp import AiohttpSession

from handlers import user_router, admin_router

from config import config
from database.crud import create_admin_settings
from database import init_database
from utils.telegram import set_commands


async def main():
    await init_database(config.db.url)
    await create_admin_settings()

    dp = Dispatcher()
    dp.include_routers(
        admin_router,
        user_router,
    )

    bot = Bot(
        token=config.bot.token, default=DefaultBotProperties(parse_mode="HTML"),
        session=AiohttpSession(timeout=3)
    )
    await set_commands(bot)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s'
    )
    asyncio.run(main())
