from modules import *

from filters import thresholdImage
from filters import thresholdImages

from tess import reconize
from tess import recognizeFromLetters

from extractLetters import extractLetters

path = os.path.join('working-image',"{}.png".format(str(2)))
application = None
originalImage = None

def saveImage(image):
	cv2.imwrite(path, image)

def getImage():
	image = cv2.imread(path)
	return image

def selectImage(self):
	global application, originalImage
	application = self
	originalImage = filedialog.askopenfilename()
	image = cv2.imread(originalImage,0)
	cv2.imwrite(os.path.join('working-image',"{}.png".format(str(1))), image)
	if not os.path.exists('working-image'):
		os.makedirs('working-image')
	saveImage(image)
	setExpected(application.lblTextOutputExpected)
	image = ImageTk.PhotoImage(file=originalImage)

	application.lblImageOriginal.image = image
	application.lblImageOriginal.configure(image = image)

def setImage(frame, image):
	image = np.asarray(image)
	image = ImageTk.PhotoImage(file=path)

	frame.image = image
	frame.configure(image = image)

def applyThresholdImage():
	image = getImage()
	image = thresholdImage(image)
	application
	setImage(application.lblImageOutput, image)		

def showResult():
	image = getImage()
	result = reconize(image)
	if(result == application.lblTextOutputExpected.cget('text')):
		application.lblTextOutputAnswer.configure(bg = "green")
	else:
		application.lblTextOutputAnswer.configure(bg = "red")
	application.lblTextOutputAnswer.configure(text=result)

def setExpected(frame):
	frame.configure(text=getFileName())

def solveFromLetters():
	image = getImage()
	letters = extractLetters(image)
	letters = thresholdImages(letters)
	result = recognizeFromLetters(letters)
	
	if(result == application.lblTextOutputExpected.cget('text')):
		application.lblTextOutputAnswer.configure(bg = "green")
	else:
		application.lblTextOutputAnswer.configure(bg = "red")
	application.lblTextOutputAnswer.configure(text=result)

def getFileName():
	global originalImage
	text = os.path.basename(originalImage)
	text = os.path.splitext(text)[0]
	return text