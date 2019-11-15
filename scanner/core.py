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
    IMAGE_PATH = Path(filepath)

    text = pytesseract.image_to_string(Image.open(IMAGE_PATH))

    return text

print (ocr_processing(".\\test\\resources\\test_image.png"))