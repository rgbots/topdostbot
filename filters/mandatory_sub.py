from aiogram import Bot
from aiogram.filters import BaseFilter
from aiogram.types import Message

from database import crud
from utils import mandatory_texts
from utils.admin import check_follow
from keyboards.mandatory_subscription import unsubbed


class MandatorySubscriptionFilter(BaseFilter):
    async def __call__(self, message: Message, bot: Bot) -> bool:
        user = await crud.get_user(message.from_user.id)
        follows = await check_follow(user, bot)
        if follows and "subs" in follows:
            await message.answer(
                mandatory_texts.SUB_TEXT,
                reply_markup=unsubbed(follows)
            )
            return False
        return True
