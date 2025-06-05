from io import BytesIO

from aiogram import Router, F, types
from aiogram.filters import Command

from database import crud


router = Router()


@router.message(Command('ref_export'))
async def export_db_by_ref(message: types.Message):
    ref = message.text.split()[1]
    ids = await crud.get_users_ids_by_ref(ref)

    file = BytesIO()
    file.write(bytes('\n'.join([str(user_id) for user_id in ids]), 'utf-8'))
    file.seek(0)

    await message.answer_document(
        types.BufferedInputFile(file.getvalue(), filename=f"export_{ref}.txt"),
        caption=f"Экспорт <b>{len(ids)}</b> пользователей по реферальной ссылке <b>{ref}</b>"
    )
