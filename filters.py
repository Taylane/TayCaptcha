from modules import *

def thresholdImage(image):
    image = np.asarray(image)
    image = scipy.misc.toimage(image)
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.namedWindow('Threshold', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('Threshold',image)
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    