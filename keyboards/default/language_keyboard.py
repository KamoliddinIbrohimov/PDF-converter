from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

language_keyboard = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="🇺🇿UZ"),
            KeyboardButton(text="🇷🇺РУ")
        ],
        [
            KeyboardButton(text="🇺🇸EN")
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)