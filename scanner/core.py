try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import os
import cv2


def binarizeImage(pathToImage):
    """
    Processes image with thresholding and blurring
    """

    image = cv2.imread(pathToImage)
    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # thresholding to preprocess image
    # useful for reading dark text over grey shapes
    grey = cv2.threshold(grey, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # blur to remove noise
    grey = cv2.medianBlur(grey, 3)

    filename = "temp.png"
    cv2.imwrite(filename, grey)


def ocrProcessing(pathToImage):
    """
    Processes an image of text into a string of that text
    """
    # ya it's hardcoded, need a prettier solution
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'

    binarizeImage(pathToImage)
    text = pytesseract.image_to_string(Image.open("temp.png"))
    os.remove("temp.png")

    return text


print(ocrProcessing('scanner\\tests\\resources\\receipt_1.jpg'))
# print(ocrProcessing('tests\\resources\\test_image.png'))
