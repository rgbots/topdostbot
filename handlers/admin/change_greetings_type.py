from aiogram import Router, F, types

from database import crud
from keyboards.admin.greetings import GreetingsTypeCD, greetings_type_menu


router = Router()


@router.callback_query(F.data == 'change_greetings_type')
async def change_greetings_type_handler(call: types.CallbackQuery):
    greetings_type = (await crud.get_greetings_type())

    await call.message.edit_text(
        'Выберите тип приветствия:',
        reply_markup=greetings_type_menu(greetings_type)
    )


@router.callback_query(GreetingsTypeCD.filter())
async def select_greetings_type_handler(call: types.CallbackQuery, callback_data: GreetingsTypeCD):
    chosen_greetings_type = callback_data.type

    await crud.update_greetings_type(chosen_greetings_type)
    await call.answer('Тип приветствия изменен!', show_alert=True)
    await call.message.edit_reply_markup(reply_markup=greetings_type_menu(chosen_greetings_type))
