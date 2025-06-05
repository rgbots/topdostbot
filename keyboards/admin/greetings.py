from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, CallbackData

from database.models import GreetingsType


class GreetingsTypeCD(CallbackData, prefix="greetings_type"):
    type: GreetingsType


def greetings_type_menu(current_type: GreetingsType):
    builder = InlineKeyboardBuilder()

    for text in ('Нативные', 'HiViews'):
        if text == 'Нативные':
            if current_type == GreetingsType.native:
                text = f'✅ {text}'

            builder.button(
                text=text,
                callback_data=GreetingsTypeCD(type=GreetingsType.native)
            )
        elif text == 'HiViews':
            if current_type == GreetingsType.hiviews:
                text = f'✅ {text}'

            builder.button(
                text=text,
                callback_data=GreetingsTypeCD(type=GreetingsType.hiviews)
            )

    builder.button(
        text='🔙 Назад',
        callback_data="views"
    )
    builder.adjust(2, 1)

    return builder.as_markup()
