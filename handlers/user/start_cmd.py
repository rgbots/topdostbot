from aiogram import Router, Bot, types, html, F
from aiogram.filters import CommandObject, Command
from aiogram.fsm.context import FSMContext

from config import config
from database import crud
from database.models import GreetingsType
from handlers.user.test import OneQuestion
from keyboards.test_menu import (
    start_creating, created_test_menu, question_menu,
    stop_process_test, test_yourself
)
from states.user import CreationTest, ProccesTest
from utils.ad import HiViews
from utils.gramads import show_advert
from utils.admin import show_ad_pm
from utils import texts


router = Router()


@router.message(F.text.startswith("/start s_"))
async def start_test(message: types.Message, state: FSMContext, bot: Bot):
    test_creator_id = int(message.text.split('_')[1])
    user, is_created = await crud.create_or_get_user(
        message.from_user.id,
        html.quote(message.from_user.first_name),
        message.from_user.username,
        source=f'friend_{test_creator_id}'
    )

    greetings_type = await crud.get_greetings_type()
    if greetings_type is GreetingsType.hiviews:
        post_sent = await HiViews(
            message.chat.id, message.message_id,
            message.from_user.first_name, message.from_user.language_code
        )
        if not post_sent and message.from_user.id in config.bot.admins:
            await message.answer("Пост HiViews не найден.")
    else:
        await show_ad_pm(user_id=message.from_user.id, bot=bot, type='greeting')

    if test_creator_id == message.from_user.id:
        bot_user = (await bot.me()).username
        user_id = message.from_user.id
        return await message.reply(
            text=texts.TEST_YOURSELF.format(bot_username=bot_user, id=user_id),
            reply_markup=test_yourself(bot_username=bot_user, user_id=user_id)
        )

    test = await crud.get_test(user_id=test_creator_id)
    if not test:
        return await message.answer(
            text='Bu foydalanuvchi hali sinovga ega emas.'
        )
    result = await crud.get_result(
        test_creator_id=test_creator_id,
        user_id=message.from_user.id
    )

    if not result:
        await message.answer(
            text=texts.START_PROCESS_TEST,
            reply_markup=stop_process_test()
        )
        await message.answer(
            OneQuestion.text1,
            link_preview_options=types.LinkPreviewOptions(
                url=OneQuestion.photo,
                prefer_large_media=True,
                show_above_text=True
            ),
            reply_markup=question_menu(
                action='process',
                options=OneQuestion.ans,
                row_width=OneQuestion.row_width
        )
        )
        await state.update_data(test_creator_id=test_creator_id)
        await state.set_state(ProccesTest.Second_State)
    else:
        await message.answer(
            f"Siz allaqachon bu testni topshirdingiz va <b>{result.percentage}% to'pladingiz</b>"
        )


@router.message(Command('start'))
async def start_cmd(message: types.Message, command: CommandObject, bot: Bot, state: FSMContext):
    await state.clear()
    user, is_created = await crud.create_or_get_user(
        message.from_user.id,
        html.quote(message.from_user.first_name),
        message.from_user.username,
        command.args
    )

    greetings_type = await crud.get_greetings_type()
    if greetings_type is GreetingsType.hiviews:
        post_sent = await HiViews(
            message.chat.id, message.message_id,
            message.from_user.first_name, message.from_user.language_code
        )
        if not post_sent and message.from_user.id in config.bot.admins:
            await message.answer("Пост HiViews не найден.")
    else:
        await show_ad_pm(user_id=message.from_user.id, bot=bot, type='greeting')

    is_created = await crud.get_test(
        user_id=message.from_user.id
    )

    bot = await bot.me()
    user_id = message.from_user.id

    if is_created:
        await message.answer(
            text=texts.COMPATIBILITY_TEST_CREATED.format(
                bot_username=bot.username,
                id=user_id
            ),
            reply_markup=created_test_menu(
                user_id=user_id,
                bot_user=bot.username
            ),
            disable_web_page_preview=True
        )
    else:
        await state.set_state(CreationTest.First_State)
        await message.answer(
            text=texts.COMPATIBILITY_TEST_NOT_CREATED,
            reply_markup=start_creating()
        )
    await show_advert(user_id=message.from_user.id)


@router.callback_query(F.data == 'back')
async def back(call: types.CallbackQuery, state: FSMContext, bot: Bot):
    await state.clear()

    await call.message.delete()
    greetings_type = await crud.get_greetings_type()
    if greetings_type is GreetingsType.hiviews:
        post_sent = await HiViews(
            call.message.chat.id, call.message.message_id,
            call.from_user.first_name, call.from_user.language_code
        )
        if not post_sent and call.from_user.id in config.bot.admins:
            await call.message.answer("Пост HiViews не найден.")
    else:
        await show_ad_pm(user_id=call.from_user.id, bot=bot, type='greeting')

    is_created = await crud.get_test(
        user_id=call.from_user.id
    )

    bot = await bot.me()
    user_id = call.from_user.id

    if is_created:
        await call.message.answer(
            text=texts.COMPATIBILITY_TEST_CREATED.format(
                bot_username=bot.username,
                id=user_id
            ),
            reply_markup=created_test_menu(
                user_id=user_id,
                bot_user=bot.username
            ),
            disable_web_page_preview=True
        )
    else:
        await state.set_state(CreationTest.First_State)
        await call.message.answer(
            text=texts.COMPATIBILITY_TEST_NOT_CREATED,
            reply_markup=start_creating()
        )
    await show_advert(user_id=call.from_user.id)