import difflib
import time

from aiogram import Router, F, types, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import InputMediaPhoto

from keyboards.test_menu import question_menu, remove
from utils import texts
from database import crud
from states.user import ProccesTest
from .test import *


router = Router()


@router.callback_query(F.data.startswith('process'), ProccesTest.Second_State)
async def get_first_ans(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.edit_text(
        text=TwoQuestion.text1,
        link_preview_options=types.LinkPreviewOptions(
            url=TwoQuestion.photo,
            prefer_large_media=True,
            show_above_text=True
        ),
        reply_markup=question_menu(
            action='process',
            options=TwoQuestion.ans,
            row_width=TwoQuestion.row_width
        )
    )
    await state.update_data(first_answer=call.data.split('_')[1])
    await state.set_state(ProccesTest.Third_State)


@router.callback_query(F.data.startswith('process'), ProccesTest.Third_State)
async def get_second_ans(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.edit_text(
        text=ThreeQuestion.text1,
        link_preview_options=types.LinkPreviewOptions(
            url=ThreeQuestion.photo,
            prefer_large_media=True,
            show_above_text=True
        ),
        reply_markup=question_menu(
            action='process',
            options=ThreeQuestion.ans,
            row_width=ThreeQuestion.row_width
        )
    )
    await state.update_data(second_answer=call.data.split('_')[1])
    await state.set_state(ProccesTest.Fourth_State)


@router.callback_query(F.data.startswith('process'), ProccesTest.Fourth_State)
async def get_third_ans(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.edit_text(
        text=FourQuestion.text1,
        link_preview_options=types.LinkPreviewOptions(
            url=FourQuestion.photo,
            prefer_large_media=True,
            show_above_text=True
        ),
        reply_markup=question_menu(
            action='process',
            options=FourQuestion.ans,
            row_width=FourQuestion.row_width
        )
    )
    await state.update_data(third_answer=call.data.split('_')[1])
    await state.set_state(ProccesTest.Fifth_State)


@router.callback_query(F.data.startswith('process'), ProccesTest.Fifth_State)
async def get_fourth_ans(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.edit_text(
        text=FiveQuestion.text1,
        link_preview_options=types.LinkPreviewOptions(
            url=FiveQuestion.photo,
            prefer_large_media=True,
            show_above_text=True
        ),
        reply_markup=question_menu(
            action='process',
            options=FiveQuestion.ans,
            row_width=FiveQuestion.row_width
        )
    )
    await state.update_data(fourth_answer=call.data.split('_')[1])
    await state.set_state(ProccesTest.Sixth_State)


@router.callback_query(F.data.startswith('process'), ProccesTest.Sixth_State)
async def get_fifth_ans(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.edit_text(
        text=SixQuestion.text1,
        link_preview_options=types.LinkPreviewOptions(
            url=SixQuestion.photo,
            prefer_large_media=True,
            show_above_text=True
        ),
        reply_markup=question_menu(
            action='process',
            options=SixQuestion.ans,
            row_width=SixQuestion.row_width
        )
    )
    await state.update_data(fifth_answer=call.data.split('_')[1])
    await state.set_state(ProccesTest.Seventh_State)


@router.callback_query(F.data.startswith('process'), ProccesTest.Seventh_State)
async def get_sixth_ans(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.edit_text(
        text=SevenQuestion.text1,
        link_preview_options=types.LinkPreviewOptions(
            url=SevenQuestion.photo,
            prefer_large_media=True,
            show_above_text=True
        ),
        reply_markup=question_menu(
            action='process',
            options=SevenQuestion.ans,
            row_width=SevenQuestion.row_width
        )
    )
    await state.update_data(sixth_answer=call.data.split('_')[1])
    await state.set_state(ProccesTest.Eighth_State)


@router.callback_query(F.data.startswith('process'), ProccesTest.Eighth_State)
async def get_seventh_ans(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.edit_text(
        text=EightQuestion.text1,
        link_preview_options=types.LinkPreviewOptions(
            url=EightQuestion.photo,
            prefer_large_media=True,
            show_above_text=True
        ),
        reply_markup=question_menu(
            action='process',
            options=EightQuestion.ans,
            row_width=EightQuestion.row_width
        )
    )
    await state.update_data(seventh_answer=call.data.split('_')[1])
    await state.set_state(ProccesTest.Nineth_State)


@router.callback_query(F.data.startswith('process'), ProccesTest.Nineth_State)
async def get_nineth_ans(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.edit_text(
        text=NineQuestion.text1,
        link_preview_options=types.LinkPreviewOptions(
            url=NineQuestion.photo,
            prefer_large_media=True,
            show_above_text=True
        ),
        reply_markup=question_menu(
            action='process',
            options=NineQuestion.ans,
            row_width=NineQuestion.row_width
        )
    )
    await state.update_data(eighth_answer=call.data.split('_')[1])
    await state.set_state(ProccesTest.Tenth_State)


@router.callback_query(F.data.startswith('process'), ProccesTest.Tenth_State)
async def get_tenth_ans(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.edit_text(
        text=TenQuestion.text1,
        link_preview_options=types.LinkPreviewOptions(
            url=TenQuestion.photo,
            prefer_large_media=True,
            show_above_text=True
        ),
        reply_markup=question_menu(
            action='process',
            options=TenQuestion.ans,
            row_width=TenQuestion.row_width
        )
    )
    await state.update_data(ninth_answer=call.data.split('_')[1])
    await state.set_state(ProccesTest.Finish_State)


@router.callback_query(F.data.startswith('process'), ProccesTest.Finish_State)
async def get_eleventh_ans(call: types.CallbackQuery, state: FSMContext, bot: Bot):
    await call.answer()
    info = await state.get_data()

    test_creator_id = info['test_creator_id']
    # НЕ забыть поменять при изменениии
    answers_of_surveyed = [
        info['first_answer'], info['second_answer'], info['third_answer'],
        info['fourth_answer'], info['fifth_answer'], info['sixth_answer'],
        info['seventh_answer'], info['eighth_answer'], info['ninth_answer'],
        call.data.split('_')[1]
    ]

    answers_of_creator = await crud.creator_answers(
        user_id=test_creator_id
    )

    row_percent = [i for i, j in zip(answers_of_creator[0], answers_of_surveyed) if i == j]
    percentage = int(len(row_percent) / 10 * 100)

    await crud.create_result(
        user_id=call.from_user.id,
        test_creator_id=test_creator_id,
        answers=answers_of_surveyed,
        date=int(time.time()),
        percentage=percentage,
        name_user=call.from_user.first_name
    )

    if 0 <= percentage <= 25:
        friendship_lvl = 'Dushmanlar 😒'
    elif 25 <= percentage <= 50:
        friendship_lvl = 'Do\'stlar 🙃'
    elif 50 <= percentage <= 75:
        friendship_lvl = 'Yaxshi do\'stlar 😏'
    elif 75 <= percentage <= 99:
        friendship_lvl = 'Eng yaxshi do\'stlar 😎'
    elif percentage == 100:
        friendship_lvl = 'Barcha javoblarni bilish 🤓'
    else:
        friendship_lvl = '✨'
    await call.message.delete()
    await call.message.answer(
        text=f"<b>Siz sinovdan o'tdingiz</b> ✅\n\n"
            f"Sizning natijangiz <b>{percentage}%</b>\n"
            f"Do'stlik darajasi: <b>{friendship_lvl}</b>\n\n"
            f"Bundan tashqari, /start yordamida asosiy menyuga o'tish orqali o'z testingizni yaratishingiz mumkin.",
        reply_markup=remove
    )

    try:
        await bot.send_message(
            test_creator_id,
            f"{call.message.chat.first_name} sinovdan o'tdi. "
            f"Uning natijasi <b>{percentage}%</b>\n"
            f"Do'stlik darajasi: <b>{friendship_lvl}</b>"
        )
    except:
        await call.message.answer("*Of. Sinov muallifi botni bloklaganga o'xshaydi :(*", parse_mode="Markdown")

    await state.clear()


@router.message(F.text == "Sinovni to'xtating ❌")
async def stop(message: types.Message, state: FSMContext):
    await state.clear()

    await message.answer(
        text=texts.PROCCESS_TEST_STOP,
        reply_markup=remove
    )
