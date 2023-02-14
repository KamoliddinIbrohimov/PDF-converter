from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def setting_language(language):
    change_language = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🇺🇿UZ", callback_data="uz"),
                InlineKeyboardButton(text="🇷🇺РУ", callback_data="ru")
            ],
            [
                InlineKeyboardButton(text="🇺🇸󠁧󠁥EN", callback_data="en")
            ],
            [
                InlineKeyboardButton(text="🔙", callback_data=language)
            ]
        ])
    return change_language
