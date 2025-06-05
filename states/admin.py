from aiogram.fsm.state import StatesGroup, State


class Notifs(StatesGroup):
    createref = State()
    createref2 = State()
    sub_get_bot_token = State()
    sub_get_bot_url = State()

    create_sub = State()
    create_sub2 = State()
    choose_audience = State()
    first_step = State()
    second_step = State()
    create_view = State()
    get_type = State()
    create_view2 = State()
    create_view3 = State()


class Stats(StatesGroup):
    get_date = State()
