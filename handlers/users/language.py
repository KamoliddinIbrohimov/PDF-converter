from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, db

from states.language import LanguageState

async def database_language(id, language):
    await db.update_user_language(telegram_id=id, languageuser=language)


@dp.message_handler(text="🇺🇿UZ", state=LanguageState.start)
async def uz_menu(message: types.Message, state: FSMContext):
    await message.delete()
    await message.answer("🇺🇿Siz O'zbek tilini tanladinggiz\n"
                         "❕Botdan rasmni pdf yoki pdf farmatdagi faylni \n"
                         " rasm korinishiga keltirishda foydalanishinggiz \n"
                         " mumkin. \n\n"
                         "<b>Sinab ko'rish uchun pdf fayl yoki rasm yuboring</b>📤")
    id = message.from_user.id
    language = "uz"
    await database_language(id, language)
    await state.finish()


@dp.message_handler(text="🇷🇺РУ", state=LanguageState.start)
async def uz_menu(message: types.Message, state: FSMContext):
    await message.delete()
    await message.answer("🇷🇺Вы выбрали русский\n"
                           "❕Конвертировать изображение из бота в pdf или файл в формате pdf\n"
                           " используйте для отображения изображения\n"
                           " возможный.\n\n"
                           "<b>Отправьте pdf-файл или изображение для тестирования</b>📤")
    id = message.from_user.id
    language = "ru"
    await database_language(id, language)
    await state.finish()

@dp.message_handler(text="🇺🇸EN", state=LanguageState.start)
async def en_menu(message: types.Message, state: FSMContext):
    await message.delete()
    await message.answer("🇺🇸You have selected English\n"
                          "❕Convert image from bot to pdf or file in pdf format \n"
                          " use to display the image \n"
                          " possible.\n\n"
                          "<b>Send a pdf file or image for testing</b>📤")
    id = message.from_user.id
    language = "en"
    await database_language(id, language)
    await state.finish()
