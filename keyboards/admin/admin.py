from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, ReplyKeyboardBuilder


CANCEL_BTN = InlineKeyboardButton(text='🚫 Отмена', callback_data="cancel_admin")


def main_menu() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.row(
        InlineKeyboardButton(text='📥 Рассылка', callback_data="users_notifications"),
        InlineKeyboardButton(text='✏️ Подписки', callback_data="subs")
    )
    builder.row(
        InlineKeyboardButton(text='👁 Показы', callback_data="views"),
        InlineKeyboardButton(text='♿️ Удалить неактивных', callback_data="deleteInactive")
    )
    builder.row(
        InlineKeyboardButton(text='⛓ Ссылки', callback_data="refs"),
        InlineKeyboardButton(text="👥 Все юзеры", callback_data='CSV')
    )
    builder.row(
        InlineKeyboardButton(text='👥 Живые юзеры', callback_data="csv"),
        InlineKeyboardButton(text='🔄 Обновить файл валида', callback_data="updateCsv")
    )
    builder.row(
        InlineKeyboardButton(text='📊 Статистика', callback_data="stats")
    )
    builder.row(
        CANCEL_BTN
    )

    return builder.as_markup()

def generate_or_cancel_ref():
    builder = InlineKeyboardBuilder()
    builder.button(
        text='🌀 Сгенерировать',
        callback_data='gen_ref'
    )
    builder.button(
        text='🚫 Отмена',
        callback_data='refs'
    )
    builder.adjust(1)
    return builder.as_markup()


def cancel_action(return_to: str):
    builder = InlineKeyboardBuilder()
    builder.button(
        text='🚫 Отмена',
        callback_data=return_to
    )
    return builder.as_markup()


def user_stats_menu() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text='🐵 Сводка по пользователям', callback_data='stats'),
        width=1
    )
    builder.row(
        InlineKeyboardButton(text='🔙 Назад', callback_data="admin"),
        CANCEL_BTN
    )

    return builder.as_markup()


def download_stats_menu() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text='Скачивания', callback_data='download_stats'),
        InlineKeyboardButton(text='🔙 Назад', callback_data="admin"),
        width=1
    )

    return builder.as_markup()


def users_stats_menu() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text='Пользователи', callback_data='stats'),
        InlineKeyboardButton(text='🔙 Назад', callback_data="admin"),
        width=1
    )

    return builder.as_markup()


def back_to_menu(with_cancel: bool = True) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text='🔙 Назад', callback_data="admin"),
        width=2
    )
    if with_cancel:
        builder.add(CANCEL_BTN)

    return builder.as_markup()


def mandatory_subs_list(subs_list: list):
    builder = InlineKeyboardBuilder()

    for num, sub in enumerate(subs_list, start=1):
        builder.row(InlineKeyboardButton(text=f'{sub.channel_name}', callback_data="manageSub_{}".format(sub.id)))

    builder.row(InlineKeyboardButton(text='🆕 Добавить новый', callback_data="createSub"))
    builder.row(InlineKeyboardButton(text='🤖 Добавить нового бота', callback_data="createSubBot"))
    builder.row(
        InlineKeyboardButton(text='🔙 Назад', callback_data="admin"),
        CANCEL_BTN
    )

    return builder.as_markup()


def delete_sub(sub_id: int):
    builder = InlineKeyboardBuilder()

    builder.row(InlineKeyboardButton(text='❌ Удалить ОП', callback_data="deleteSub_{}".format(sub_id)))
    builder.row(
        InlineKeyboardButton(text='🔙 Назад', callback_data="admin"),
        CANCEL_BTN
    )

    return builder.as_markup()


def current_views_list(views_list: list):
    builder = InlineKeyboardBuilder()

    for view in views_list:
        builder.row(InlineKeyboardButton(text='{}'.format(view.name), callback_data="manageView_{}".format(view.id)))

    builder.row(InlineKeyboardButton(text='🆕 Создать новый', callback_data="CreateView"))
    builder.row(
        InlineKeyboardButton(
            text='⚙️ Тип приветствий', callback_data="change_greetings_type"
        )
    )
    builder.row(
        InlineKeyboardButton(text='🔙 Назад', callback_data="admin"),
        CANCEL_BTN
    )

    return builder.as_markup()


def view_options(view_id: int):
    builder = InlineKeyboardBuilder()

    builder.row(InlineKeyboardButton(text='❌ Удалить показ', callback_data="deleteView_{}".format(view_id)))
    builder.row(InlineKeyboardButton(text='👁 Посмотреть показ', callback_data="watchView_{}".format(view_id)))
    builder.row(
        InlineKeyboardButton(text='🔙 Назад', callback_data="views"),
        CANCEL_BTN
    )

    return builder.as_markup()


def refresh_notifications_status():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="Обновить", callback_data='refreshNotify'))

    return builder.as_markup()


def where_to_send_notifications_menu() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="👤 ПОЛЬЗОВАТЕЛИ", callback_data="users_notifications"),
        InlineKeyboardButton(text="👥 ГРУППЫ", callback_data="chats_notifications")
    )
    builder.row(
        InlineKeyboardButton(text="🌐 Везде", callback_data="all_notifications")
    )
    builder.row(
        InlineKeyboardButton(text='🔙Вернуться в меню', callback_data="admin"),
        CANCEL_BTN
    )

    return builder.as_markup()


def refs_menu():
    builder = InlineKeyboardBuilder()

    builder.row(
        InlineKeyboardButton(text='🆕 Добавить', callback_data="createref"),
        InlineKeyboardButton(text="❌ Удалить", callback_data="delrefs")
    )
    builder.row(
        InlineKeyboardButton(text='🔙 Назад', callback_data="admin"),
        CANCEL_BTN
    )

    return builder.as_markup()


def menu_stats():
    builder = InlineKeyboardBuilder()

    builder.button(
        text='За месяц',
        callback_data='month_stats'
    )

    builder.button(
        text='За неделю',
        callback_data='week_stats'
    )

    builder.button(
        text='За сутки',
        callback_data='day_stats'
    )

    builder.button(
        text='По дате',
        callback_data='date_stats'
    )

    builder.adjust(2)

    return builder.as_markup()


def views_types():
    kb = ReplyKeyboardBuilder()
    kb.button(
        text='Обычный'
    )
    kb.button(
        text='Приветствие'
    )
    kb.adjust(1)

    return kb.as_markup(resize_keyboard=True)
