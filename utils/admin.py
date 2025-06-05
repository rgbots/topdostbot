import logging
import asyncio
import random
import string

from datetime import datetime, timedelta
from typing import Optional

from aiogram import Bot
from aiogram.types import Message, InlineKeyboardMarkup
from aiogram.exceptions import TelegramBadRequest, TelegramForbiddenError
from tortoise.expressions import F

from database import crud
from database.models import Users, Subs, Views


async def show_ad_pm(user_id: int, bot: Bot, type: str = 'simple'):
    if type == 'simple':
        await asyncio.sleep(.1)

    views = await Views.filter(max_viewed__gte=F("viewed"), status=1, type=type)

    for view in views:
        if user_id not in view.viewed_users:
            if view:
                try:
                    await bot.send_message(
                        user_id, view.msg,
                        reply_markup=view.markup if view.markup else None,
                        parse_mode='HTML',
                        disable_web_page_preview=True
                    )
                    view.viewed_users.append(user_id)
                    view.viewed += 1
                    await Views.filter(id=view.id).update(viewed_users=view.viewed_users, viewed=F("viewed") + 1)
                    if view.viewed >= view.max_viewed:
                        await Views.filter(id=view.id).update(status=3)

                    if type == 'greeting':
                        await asyncio.sleep(1)
                    return True
                except:
                    pass
    return False


async def show_ad_group(user_id: int, bot: Bot):
    views = await Views.filter(max_viewed__gte=F("viewed"), status=2)
    for view in views:
        if user_id not in view.viewed_users:
            if view:
                try:
                    await bot.send_message(
                        user_id, view.msg,
                        reply_markup=view.markup if view.markup else None,
                        parse_mode='html'
                    )
                    view.viewed_users.append(user_id)
                    view.viewed += 1
                    await Views.filter(id=view.id).update(viewed_users=view.viewed_users, viewed=F("viewed") + 1)
                    if view.viewed >= view.max_viewed:
                        await Views.filter(id=view.id).update(status=3)
                    return
                except:
                    pass


async def check_follow(user: Users, bot: Bot):
    if not user:
        return False

    subs = await Subs.all()
    unfollow = []
    not_mandatory_bots = []
    for sub in subs:
        if sub.type == 'channel':

            try:
                member = await bot.get_chat_member(sub.channel_id, user.id)
            except (TelegramBadRequest, TelegramForbiddenError):  # means bot is not admin in channel
                logging.error(f'BOT IS NOT ADMIN IN CHANNEL {sub.channel_name}!')
                continue

            if member.status == 'left':
                unfollow.append(sub)
        else:
            if sub.token != '0':
                try:
                    msbot = Bot(token=sub.token)
                    await msbot.send_chat_action(user.id, 'typing')
                except:
                    unfollow.append(sub)
            else:
                not_mandatory_bots.append(sub)

    if len(unfollow) > 0:
        unfollow.extend(not_mandatory_bots)

    if unfollow:
        if user.subbed == 1:
            await Users.filter(id=user.id).update(subbed=0, subbed_count=0)
        return {'subs': unfollow}
    else:
        if user.subbed == 0:
            await Users.filter(id=user.id).update(subbed=1)


async def send_formatted_message(
        user_id: int,
        message: Message,
        first_name: str,
        username: Optional[str],
        bot: Bot
):
    if message.text and '$first_name' in message.text:
        text = message.html_text.replace(
            '$first_name',
            f'@{username}' if username else first_name
        )
    elif message.caption and '$first_name' in message.caption:
        text = message.html_text.replace(
            '$first_name',
            f'@{username}' if username else first_name
        )
    else:
        await message.copy_to(user_id, reply_markup=message.reply_markup)
        return

    if message.text:
        await bot.send_message(
            user_id,
            text,
            reply_markup=message.reply_markup
        )
    else:
        method_name = f'send_{message.content_type}'
        method = getattr(bot, method_name)

        if method_name == 'send_photo':
            media_id = message.photo[-1].file_id
        else:
            media_type = getattr(message, message.content_type)
            media_id = media_type.file_id

        await method(
            user_id,
            media_id,
            caption=text,
            reply_markup=message.reply_markup
        )


def gen_random_ref():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))


async def send_greeting(bot: Bot, chat_id: int):
    greeting = await crud.get_greeting()
    if greeting:
        try:
            await bot.send_message(
                chat_id,
                greeting.text,
                reply_markup=greeting.markup if greeting.markup else None,
                disable_web_page_preview=True
            )
        except:
            pass

        await asyncio.sleep(1)
