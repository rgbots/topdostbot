from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardRemove
from handlers.user import test

def start_creating():
    builder = InlineKeyboardBuilder()

    builder.button(
        text="Test yarating ✨",
        callback_data="recreate_test"
    )
    return builder.as_markup(resize_keyboard=True)



def created_test_menu(
        user_id,
        bot_user
):
    builder = InlineKeyboardBuilder()

    builder.button(
        text="Baholash 📊",
        callback_data=f"rate_test"
    )
    builder.button(
        text="Testni o'chirish 🗑",
        callback_data=f"delete_test"
    )
    builder.button(
        text="Do'stingizga yuboring ➕",
        url=f'https://t.me/share/url?url=https://t.me/{bot_user}?start=s_{user_id}'
    )
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)


def question_menu(
        action: str,
        options: tuple,
        row_width: int
):
    builder = InlineKeyboardBuilder()

    for index, option in enumerate(options, 0):
        builder.button(
            text=option,
            callback_data=f'{action}_{index}'
        )

    builder.adjust(row_width)
    return builder.as_markup(resize_keyboard=True)



def stats_menu(
    bot_username: str,
    user_id: int
):
    builder = InlineKeyboardBuilder()

    builder.button(
        text="Testni ulashish ➕",
        switch_inline_query=f"Meni qanchalik yaxshi bilasiz?\n\nt.me/{bot_username}?start=s_{user_id}"
    )
    builder.button(
        text="Testni o'chirish 🗑",
        callback_data=f"delete_test"
    )
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)

def stop_creation_test():
    builder = ReplyKeyboardBuilder()

    builder.button(
        text="Test yaratishni to'xtatish ❌"
    )
    
    return builder.as_markup(resize_keyboard=True)


def stop_process_test():
    builder = ReplyKeyboardBuilder()

    builder.button(
        text="Sinovni to'xtating ❌"
    )
    
    return builder.as_markup(resize_keyboard=True)


remove = ReplyKeyboardRemove()


def test_yourself(bot_username, user_id):
    builder = InlineKeyboardBuilder()

    builder.button(
        text="✉️ Havola bilan bo'lishing",
        switch_inline_query=f't.me/{bot_username}?start=s_{user_id}'
    )
    builder.button(
        text="🔙 Orqaga qaytish",
        callback_data=f'back'
    )
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)


def after_creating(bot_user, user_id):
    builder = InlineKeyboardBuilder()
    builder.button(
            text="Do'stingizga yuboring ➕",
            url=f'https://t.me/share/url?url=https://t.me/{bot_user}?start=s_{user_id}'
        )
    builder.button(
        text="Baholash 📊",
        callback_data=f"rate_test"
    )
    
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)