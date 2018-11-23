from modules import *
pytesseract.pytesseract.tesseract_cmd = '../../utils/tesseract/tesseract'

def reconize(image):
	image = np.asarray(image) 

	phrase = pytesseract.image_to_string(image, lang='eng')
	phrase = pytesseract.image_to_string(image, config="-c tessedit"
												"_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
												" -l osd"
												" ")
	return phrase

def recognizeFromLetters(letters):
	result = ""
	for letter in letters:
		
		letter = np.asarray(letter) 
		
		phrase = pytesseract.image_to_string(letter, config="-c tessedit"
                                             "_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
                                             " --psm 10"
                                             " -l osd"
                                             " ")

		cv2.imshow('image',letter)
		cv2.waitKey(0)
		cv2.destroyAllWindows()

		#phrase = pytesseract.image_to_string(letter, lang='eng')
		# phrase = pytesseract.image_to_string(letter, config="-c tessedit"
		# 											"_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
		# 											" -l osd"
		# 											" ")

		print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa:',phrase)
		result = result + phrase
	return result