try:
    from PIL import Image
except ImportError:
    import Image
from . import utils
import pytesseract
import os


def ocrProcessing(pathToImage):
    """
    Processes an image of text into a string of that text
    """
    # ya it's hardcoded, need a prettier solution
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'

    utils.binarizeImage(pathToImage)
    text = pytesseract.image_to_string(Image.open("temp.png"))
    os.remove("temp.png")

    return text


print(ocrProcessing('scanner\\tests\\resources\\receipt_1.jpg'))
# print(ocrProcessing('tests\\resources\\test_image.png'))
