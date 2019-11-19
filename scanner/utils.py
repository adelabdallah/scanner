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