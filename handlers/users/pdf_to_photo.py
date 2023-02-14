import asyncio
import os

from aiogram import types
from aiogram.types import InputFile, MediaGroup

from keyboards.default.pdf_to_photo import keyboard_pdf
from loader import dp
from utils.misc.pdf_to_photo import upload_pdf, convertor


@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def get_document(message: types.Message):
    await upload_pdf(message=message)
    await message.reply("tanlang", reply_markup=keyboard_pdf)


@dp.message_handler(text="🗂➡️🌄")
async def send_photo(message: types.Message):
    id = str(message.from_user.id)
    await message.delete()
    msg = await message.answer("🗂🔁🌄")
    path = await convertor(id=id)
    album = MediaGroup()
    if len(path) > 10:
        for p in path:
            photo_file = InputFile(path_or_bytesio=p)
            await message.answer_photo(photo_file)

    else:
        for p in path:
            photo_file = InputFile(path_or_bytesio=p)
            album.attach_photo(photo_file)
        await message.answer_media_group(media=album)
    await msg.delete()
    await asyncio.sleep(3)
    os.remove(f'items/categories/subcategory/document/{id}/file.pdf')
    for d in path:
        os.remove(d)
