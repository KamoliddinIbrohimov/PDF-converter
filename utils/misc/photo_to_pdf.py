from pathlib import Path
# from aiogram.types import InputFile
import os

from aiogram.types import InputFile
from fpdf import FPDF

from PIL import Image


async def upload_photo(message):
    id = str(message.from_user.id)
    path_to_download = Path().joinpath("items", "categories", "photo_to_pdf", id)
    path_to_download.mkdir(parents=True, exist_ok=True)
    await message.photo[-1].download(destination_dir=path_to_download)


async def converter(id):
    path_to_download = Path().joinpath("items", "categories", "photo_to_pdf", id, "document")
    path_to_download.mkdir(parents=True, exist_ok=True)
    path = f'items/categories/photo_to_pdf/{id}/photos/'
    dirs = os.listdir(path)

    pdf1 = FPDF()
    # pdf1.add_page()
    for img in dirs:
        pdf1.add_page()
        pdf1.image(path + img, w=210, h=297, x=0, y=0)
        os.remove(path + img)

    path_to_download = str(path_to_download) + "/document.pdf"
    pdf1.output(path_to_download, "F")
    pdf_file = InputFile(path_or_bytesio=path_to_download)
    return pdf_file