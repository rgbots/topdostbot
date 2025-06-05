from aiogram import Router, F, types, Bot
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command

from keyboards.test_menu import start_creating, stats_menu, remove
from utils import texts
from database import crud


router = Router()


@router.callback_query(F.data == 'delete_test')
async def deleting_test(call: types.CallbackQuery):
    await crud.delete_test(
        user_id=call.from_user.id
    )

    await call.message.edit_text(
        text=(
            "<b>Muvaffaqiyatli oʻchirib tashlandi ✅</b>\n\n"
            "Botni davom ettirish uchun /start tugmasini bosing."
        )
    )


@router.callback_query(F.data == 'rate_test')
async def rate_test(call: types.CallbackQuery, bot: Bot):
    bot = await bot.me()
    list_of_results = ''
    tuple_of_results = await crud.top_results(
        user_id=call.from_user.id
    )
    for percentage, name_user in tuple_of_results:
        list_of_results += f'{name_user} - {percentage}%\n'
    count = await crud.results_count(
        user_id=call.from_user.id
    )
    general_percentage = await crud.gen_percentage(
        user_id=call.from_user.id
    )
    if count == 0:
        average_percentage = "0 (chunki hali hech kim testdan o'tmagan)"
    else:
        average_percentage = int(sum(general_percentage) / count)
    await call.message.edit_text(
        text=texts.TEST_STATS.format(
            count=count,
            average_percentage=average_percentage,
            list_of_results=list_of_results
        ),
        reply_markup=stats_menu(
            bot_username=bot.username,
            user_id=call.from_user.id
        ),
        disable_web_page_preview=True
    )


@router.message(Command('mylink'))
async def mylink(message: types.Message, bot: Bot):
    user_id = message.from_user.id
    user_has_test_created = await crud.get_test(user_id=user_id)
    if not user_has_test_created:
        await message.answer(
            texts.USER_HAS_NO_TEST_CREATED,
            reply_markup=start_creating()
        )
        return

    botik = await bot.get_me()
    await message.answer(
        f"<b>Sizning havolangiz:</b> https://t.me/{botik.username}?start=s_{user_id}\n\n"
        f"<b>Uni barcha ijtimoiy tarmoqlarda tarqating va barcha do'stlaringiz va tanishlaringiz bilan baham ko'ring."
        f"Keling, ular sizni qanchalik yaxshi bilishlarini ko'raylik</b> 😉",
        reply_markup=remove, disable_web_page_preview=True)
    
    

@router.message(Command('results'))
async def mylink(message: types.Message, bot: Bot):
    user_has_test_created = await crud.get_test(user_id=message.from_user.id)
    if not user_has_test_created:
        await message.answer(
            texts.USER_HAS_NO_TEST_CREATED,
            reply_markup=start_creating()
        )
        return

    bot = await bot.me()
    list_of_results = ''
    tuple_of_results = await crud.top_results(
        user_id=message.from_user.id
    )
    for percentage, name_user in tuple_of_results:
        list_of_results += f'{name_user} - {percentage}%\n'
    count = await crud.results_count(
        user_id=message.from_user.id
    )
    general_percentage = await crud.gen_percentage(
        user_id=message.from_user.id
    )
    if count == 0:
        average_percentage = "0 (chunki hali hech kim testdan o'tmagan)"
    else:
        average_percentage = int(sum(general_percentage) / count)
    await message.answer(
        text=texts.TEST_STATS.format(
            count=count,
            average_percentage=average_percentage,
            list_of_results=list_of_results
        ),
        reply_markup=stats_menu(
            bot_username=bot.username,
            user_id=message.from_user.id
        ),
        disable_web_page_preview=True
    )
