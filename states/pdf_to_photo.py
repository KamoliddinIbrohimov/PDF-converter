from aiogram.dispatcher.filters.state import StatesGroup, State


class PdfState(StatesGroup):
    upload_pdf = State()