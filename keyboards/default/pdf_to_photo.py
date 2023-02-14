from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard_pdf = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🗂➡️🌄"),
            KeyboardButton(text="❌")
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)