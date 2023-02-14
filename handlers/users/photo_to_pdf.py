import os

from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.photo_to_pdf import keyboard_pdf
from loader import dp

from states.photo_to_pdf import PhotoState

from utils.misc.photo_to_pdf import upload_photo, converter


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_document(message: types.Message):
    await upload_photo(message=message)
    await message.answer("tanlang", reply_markup=keyboard_pdf)
    await PhotoState.upload_photo.set()


@dp.message_handler(text="🌄➡️🗂", state=PhotoState.upload_photo)
async def convertor(message: types.Message, state: FSMContext):
    id = str(message.from_user.id)
    pdf_file = await converter(id)
    await message.delete()
    msg = await message.answer("🌄🔁🗂")
    await message.answer_document(pdf_file)
    await msg.delete()
    await state.finish()
    os.remove(f'items/categories/photo_to_pdf/{id}/document/document.pdf')

