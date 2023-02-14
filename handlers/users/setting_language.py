from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp, db

from states.language import LanguageState
from keyboards.inline.setting_language import setting_language


async def database_language(id, language):
    await db.update_user_language(telegram_id=id, languageuser=language)


@dp.message_handler(Command("language"))
async def change_language_uz(message: types.Message):
    await message.delete()
    user = await db.select_user(telegram_id=message.from_user.id)
    language = user[3]
    if language == "uz":
        await message.answer("Tilni o'zgartiring", reply_markup=setting_language(language))
    elif language == "ru":
        await message.answer("Изменить язык", reply_markup=setting_language(language))
    elif language == "en":
        await message.answer("Change the language", reply_markup=setting_language(language))
    await LanguageState.update.set()


#setting handlers
@dp.callback_query_handler(text="uz", state=LanguageState.update)
async def charge_uz(call: types.CallbackQuery, state: FSMContext):
    id = call.from_user.id
    language = "uz"
    await database_language(id=id, language=language)
    msg = await call.message.answer("Til o'zgardi")
    await call.message.delete()
    await call.answer(cache_time=60)
    await state.finish()


@dp.callback_query_handler(text="ru", state=LanguageState.update)
async def charge_uz(call: types.CallbackQuery, state: FSMContext):
    id = call.from_user.id
    language = "ru"
    await database_language(id=id, language=language)
    msg = await call.message.answer("Язык изменился")
    await call.message.delete()
    await call.answer(cache_time=60)
    await state.finish()


@dp.callback_query_handler(text="en", state=LanguageState.update)
async def charge_uz(call: types.CallbackQuery, state: FSMContext):
    id = call.from_user.id
    language = "en"
    await database_language(id=id, language=language)
    msg = await call.message.answer("The language has changed")
    await call.message.delete()
    await call.answer(cache_time=60)
    await state.finish()
