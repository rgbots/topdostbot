from aiogram import Router, F

from config import config
from . import admin_handlers
from . import change_greetings_type
from . import export_by_ref


admin_router = Router()
admin_router.message.filter(F.chat.type == 'private', F.from_user.id.in_(config.bot.admins))
admin_router.callback_query.filter(F.message.chat.type == 'private', F.from_user.id.in_(config.bot.admins))

admin_router.include_routers(
    export_by_ref.router,
    admin_handlers.router,
    change_greetings_type.router,
    
)
