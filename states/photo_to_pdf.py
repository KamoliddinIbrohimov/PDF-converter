from aiogram.dispatcher.filters.state import StatesGroup, State


class PhotoState(StatesGroup):
    upload_photo = State()