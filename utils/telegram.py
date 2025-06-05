import logging


from aiogram import Bot, exceptions
from aiogram.types import (
    BotCommand,
    BotCommandScopeChat,
)
from aiogram.utils.media_group import MediaGroupBuilder

from config import config


async def set_commands(bot: Bot):
    ru = [

        BotCommand(command='start', description='😎 Botni ishga tushiring'),
        BotCommand(command="mylink", description="🔗 Mening havola"),
        BotCommand(command="results", description="📊 Natijalar"),
    ]
    ru_adm = [
        BotCommand(command='admin', description='Админ панель'),
    ]
    ru_adm.extend(ru)

    await bot.set_my_commands(
        commands=ru,
    )
    for admin in config.bot.admins:
        try:
            await bot.set_my_commands(
                commands=ru_adm,
                scope=BotCommandScopeChat(type='chat', chat_id=admin)
            )
        except exceptions.TelegramAPIError as e:
            logging.error(f'ON SET COMMANDS: {e}')
