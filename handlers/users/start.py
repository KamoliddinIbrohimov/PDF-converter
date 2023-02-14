import asyncio

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import ADMINS
from keyboards.default.language_keyboard import language_keyboard

from loader import dp, db, bot
import asyncpg
from states.language import LanguageState


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        user = await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 languageuser="null",
                                 username=message.from_user.username)
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)
    text = "🇺🇿Assalomu alekum hurmatli foydalanuvchi!\n" \
           "PDF converter botiga xush kelibsiz🥳\n" \
           "Botdan foydalanishni boshlash uchun o'zinggizga\n" \
           "qulay tilni tanlang✅\n\n" \
           "🇷🇺Здравствуйте, дорогой пользователь!\n" \
           "Добро пожаловать в бот-конвертер PDF🥳\n" \
           "Выберите предпочитаемый язык для запуска\n" \
           "с помощью бота ✅\n\n" \
           "🇺🇸Hello dear user!\n" \
           "Welcome to PDF converter bot🥳\n" \
           "Choose your preferred language to start\n" \
           "using the bot✅"

    await message.answer(text=text, reply_markup=language_keyboard)
    await LanguageState.start.set()

    # Send Admin
    count = await db.count_users()
    if count % 100 == 0:
        msg = f"{user[1]} bazaga qo'shildi \nBazada {count} ta foydalanuvchi bor"
        await bot.send_message(chat_id=ADMINS[0], text=msg)
    else:
        pass


@dp.message_handler(state=LanguageState.start)
async def echo_start_state(message: types.Message, state: FSMContext):
    msg = await message.reply("🇺🇿Siz noto'g'ri buyruq kirgazdinggiz!🤨\n"
                              "Botdan foydalanish uchun tilni tanlang😊\n\n"
                              "🇷🇺Вы ввели неверную команду!🤨\n"
                              "Выберите язык для использования бота😊\n\n"
                              "🇺🇸You entered the wrong command!🤨\n"
                              "Choose a language to use the bot😊",
                              reply_markup=language_keyboard
                              )
    await asyncio.sleep(8)
    await message.delete()
    await msg.delete()
