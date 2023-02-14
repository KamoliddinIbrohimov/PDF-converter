# import module
from pathlib import Path

from pdf2image import convert_from_path


async def upload_pdf(message):
    id = str(message.from_user.id)
    path_to_download = Path().joinpath("items", "categories", "subcategory", "document", id)
    path_to_download.mkdir(parents=True, exist_ok=True)
    path_to_download = path_to_download.joinpath("file.pdf")
    await message.document.download(destination_file=path_to_download)
    return path_to_download


async def convertor(id):
    # Store Pdf with convert_from_path function
    images = convert_from_path(f'items/categories/subcategory/document/{id}/file.pdf')
    path = []
    path_to_download = Path().joinpath("items", "categories", "subcategory", "photo", id)
    path_to_download.mkdir(parents=True, exist_ok=True)
    for i in range(len(images)):
        # Save pages as images in the pdf
        images[i].save(f'items/categories/subcategory/photo/{id}/page' + str(i) + '.jpg', 'JPEG')
        i = (f'items/categories/subcategory/photo/{id}/page' + str(i) + '.jpg')
        path.append(i)

    return path
