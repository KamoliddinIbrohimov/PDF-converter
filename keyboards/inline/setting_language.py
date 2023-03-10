from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def setting_language(language):
    change_language = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="ðºð¿UZ", callback_data="uz"),
                InlineKeyboardButton(text="ð·ðºÐ Ð£", callback_data="ru")
            ],
            [
                InlineKeyboardButton(text="ðºð¸ó §ó ¥EN", callback_data="en")
            ],
            [
                InlineKeyboardButton(text="ð", callback_data=language)
            ]
        ])
    return change_language
