from aiogram import Router, F, Bot

from filters.mandatory_sub import MandatorySubscriptionFilter

from . import start_cmd
from . import creation_test
from . import procces_test
from . import test_menu

user_router = Router()
user_router.message.filter(F.chat.type == 'private', MandatorySubscriptionFilter())
user_router.callback_query.filter(F.message.chat.type == 'private')


user_router.include_routers(
    start_cmd.router,
    creation_test.router,
    procces_test.router,
    test_menu.router
)
