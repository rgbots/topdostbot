from aiogram import Router, F, types, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import InputMediaPhoto

from keyboards.test_menu import after_creating, question_menu, stop_creation_test, remove
from utils import texts
from database import crud
from states.user import CreationTest
from .test import *


router = Router()


@router.callback_query(F.data == 'recreate_test_ad')
@router.callback_query(F.data == 'recreate_test')
async def start_creating_handler(call: types.CallbackQuery, state: FSMContext):
    if call.data == 'recreate_test':
        try:
            await call.message.delete()
        except:
            pass

    if await crud.get_test(user_id=call.from_user.id):
        return await call.message.answer(texts.USER_ALREADY_HAS_TEST)

    await call.message.answer(
        text=texts.START_CREATING_TEST,
        reply_markup=stop_creation_test()
    )

    await call.message.answer(
        OneQuestion.text,
        link_preview_options=types.LinkPreviewOptions(
            url=OneQuestion.photo,
            prefer_large_media=True,
            show_above_text=True
        ),
        reply_markup=question_menu(
            action='create',
            options=OneQuestion.ans,
            row_width=OneQuestion.row_width
        )
    )
    await state.set_state(CreationTest.Second_State)


@router.callback_query(F.data.startswith('create'), CreationTest.Second_State)
async def get_first_ans(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.edit_text(
        text=TwoQuestion.text,
        link_preview_options=types.LinkPreviewOptions(
            url=TwoQuestion.photo,
            prefer_large_media=True,
            show_above_text=True
        ),
        reply_markup=question_menu(
            action='create',
            options=TwoQuestion.ans,
            row_width=TwoQuestion.row_width
        )
    )
    await state.update_data(first_answer=call.data.split('_')[1])
    await state.set_state(CreationTest.Third_State)


@router.callback_query(F.data.startswith('create'), CreationTest.Third_State)
async def get_second_ans(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.edit_text(
        text=ThreeQuestion.text,
        link_preview_options=types.LinkPreviewOptions(
            url=ThreeQuestion.photo,
            prefer_large_media=True,
            show_above_text=True
        ),
        reply_markup=question_menu(
            action='create',
            options=ThreeQuestion.ans,
            row_width=ThreeQuestion.row_width
        )
    )
    await state.update_data(second_answer=call.data.split('_')[1])
    await state.set_state(CreationTest.Fourth_State)


@router.callback_query(F.data.startswith('create'), CreationTest.Fourth_State)
async def get_third_ans(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.edit_text(
        text=FourQuestion.text,
        link_preview_options=types.LinkPreviewOptions(
            url=FourQuestion.photo,
            prefer_large_media=True,
            show_above_text=True
        ),
        reply_markup=question_menu(
            action='create',
            options=FourQuestion.ans,
            row_width=FourQuestion.row_width
        )
    )
    await state.update_data(third_answer=call.data.split('_')[1])
    await state.set_state(CreationTest.Fifth_State)


@router.callback_query(F.data.startswith('create'), CreationTest.Fifth_State)
async def get_fourth_ans(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.edit_text(
        text=FiveQuestion.text,
        link_preview_options=types.LinkPreviewOptions(
            url=FiveQuestion.photo,
            prefer_large_media=True,
            show_above_text=True
        ),
        reply_markup=question_menu(
            action='create',
            options=FiveQuestion.ans,
            row_width=FiveQuestion.row_width
        )
    )
    await state.update_data(fourth_answer=call.data.split('_')[1])
    await state.set_state(CreationTest.Sixth_State)


@router.callback_query(F.data.startswith('create'), CreationTest.Sixth_State)
async def get_fifth_ans(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.edit_text(
        text=SixQuestion.text,
        link_preview_options=types.LinkPreviewOptions(
            url=SixQuestion.photo,
            prefer_large_media=True,
            show_above_text=True
        ),
        reply_markup=question_menu(
            action='create',
            options=SixQuestion.ans,
            row_width=SixQuestion.row_width
        )
    )
    await state.update_data(fifth_answer=call.data.split('_')[1])
    await state.set_state(CreationTest.Seventh_State)


@router.callback_query(F.data.startswith('create'), CreationTest.Seventh_State)
async def get_sixth_ans(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.edit_text(
        text=SevenQuestion.text,
        link_preview_options=types.LinkPreviewOptions(
            url=SevenQuestion.photo,
            prefer_large_media=True,
            show_above_text=True
        ),
        reply_markup=question_menu(
            action='create',
            options=SevenQuestion.ans,
            row_width=SevenQuestion.row_width
        )
    )
    await state.update_data(sixth_answer=call.data.split('_')[1])
    await state.set_state(CreationTest.Eighth_State)


@router.callback_query(F.data.startswith('create'), CreationTest.Eighth_State)
async def get_seventh_ans(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.edit_text(
        text=EightQuestion.text,
        link_preview_options=types.LinkPreviewOptions(
            url=EightQuestion.photo,
            prefer_large_media=True,
            show_above_text=True
        ),
        reply_markup=question_menu(
            action='create',
            options=EightQuestion.ans,
            row_width=EightQuestion.row_width
        )
    )
    await state.update_data(seventh_answer=call.data.split('_')[1])
    await state.set_state(CreationTest.Nineth_State)


@router.callback_query(F.data.startswith('create'), CreationTest.Nineth_State)
async def get_nineth_ans(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.edit_text(
        text=NineQuestion.text,
        link_preview_options=types.LinkPreviewOptions(
            url=NineQuestion.photo,
            prefer_large_media=True,
            show_above_text=True
        ),
        reply_markup=question_menu(
            action='create',
            options=NineQuestion.ans,
            row_width=NineQuestion.row_width
        )
    )
    await state.update_data(eighth_answer=call.data.split('_')[1])
    await state.set_state(CreationTest.Tenth_State)


@router.callback_query(F.data.startswith('create'), CreationTest.Tenth_State)
async def get_tenth_ans(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.edit_text(
        text=TenQuestion.text,
        link_preview_options=types.LinkPreviewOptions(
            url=TenQuestion.photo,
            prefer_large_media=True,
            show_above_text=True
        ),
        reply_markup=question_menu(
            action='create',
            options=TenQuestion.ans,
            row_width=TenQuestion.row_width
        )
    )
    await state.update_data(ninth_answer=call.data.split('_')[1])
    await state.set_state(CreationTest.Finish_State)


@router.callback_query(F.data.startswith('create'), CreationTest.Finish_State)
async def get_eleventh_ans(call: types.CallbackQuery, state: FSMContext, bot: Bot):
    await call.answer()
    info = await state.get_data()
    bot = await bot.me()

    # НЕ забыть поменять при изменениии
    answers = [
        info['first_answer'], info['second_answer'], info['third_answer'],
        info['fourth_answer'], info['fifth_answer'], info['sixth_answer'],
        info['seventh_answer'], info['eighth_answer'], info['ninth_answer'],
        call.data.split('_')[1]
    ]

    user_id = call.from_user.id
    try:
        await call.message.delete()
    except:
        pass

    if await crud.get_test(user_id=user_id):
        await state.clear()
        return await call.message.answer(
            text=texts.USER_HAS_TEST_CREATED
        )

    await crud.create_test(
        user_id=user_id,
        answers=answers,
        name_user=call.from_user.first_name
    )

    await call.message.answer('⏳', reply_markup=remove)
    await call.message.answer(
        text=texts.TEST_CREATED.format(
            bot_username=bot.username,
            id=call.from_user.id
        ),
        reply_markup=after_creating(bot_user=bot.username, user_id=call.from_user.id),
        disable_web_page_preview=True
    )

    await state.clear()


@router.message(F.text == "Test yaratishni to'xtatish ❌")
async def stop(message: types.Message, state: FSMContext):
    await state.clear()

    await message.answer(
        text=texts.CREATION_TEST_STOP,
        reply_markup=remove
    )
