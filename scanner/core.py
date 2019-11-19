try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import os
import cv2
import re


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
    Processes an image of a receipt into the total price on that receipt
    """
    TOTAL = 0
    # ya it's hardcoded, need a prettier solution
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'

    binarizeImage(pathToImage)

    text = pytesseract.image_to_string(Image.open(
        "temp.png"), config='-c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.$ ')

    for value in text.splitlines():
        if ("total" in value or "Total" in value or "TOTAL" in value):
            # regex for a number, a period, then a number
            TOTAL = re.findall('\d+[.]?\d+', value)

    if not TOTAL:
        # try again but with page segmentation mode (psm) set to 4: Assume a single column of text of variable sizes
        text = pytesseract.image_to_string(Image.open(
            "temp.png"), config='--psm 4 -c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.$ ')
        for value in text.splitlines():
            if ("total" in value or "Total" in value or "TOTAL" in value):
                TOTAL = re.findall('\d+[.]?\d+', value)

    os.remove("temp.png")
    # print(text)
    return TOTAL


# print(ocrProcessing('scanner\\tests\\resources\\receipt_2.jpg'))
# print(ocrProcessing('scanner\\tests\\resources\\receipt_3.jpg'))
