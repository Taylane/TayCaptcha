from modules import *
import functions

def thresholdImage(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    image = cv2.bitwise_not(image)
    functions.saveImage(image)
    return image

def thresholdImages(images):
    imagesFiltered = []
    
    for image in images:
        image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        image = cv2.copyMakeBorder(image, 8, 8, 8, 8, cv2.BORDER_REPLICATE)
        image = cv2.bitwise_not(image)
        image = cv2.resize(image,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
        kernel = np.ones((1,1), np.uint8)
        image = cv2.dilate(image,kernel,iterations = 1)
        image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        image = cv2.equalizeHist(image)
        image = cv2.medianBlur(image, 3)

        imagesFiltered.append(image)

    return imagesFiltered
        