try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from pathlib import Path 

def ocr_processing(filepath):
    """
    Processes an image of text into a string of that text
    """
    #ya it's hardcoded, need a prettier solution
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'

    IMAGE_PATH = Path(filepath)

    text = pytesseract.image_to_string(Image.open(IMAGE_PATH))

    return text