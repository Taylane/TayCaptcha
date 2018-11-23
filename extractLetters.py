from modules import *
import functions

def extractLetters(image):
    counts = {}
    letters = []
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.copyMakeBorder(image, 8, 8, 8, 8, cv2.BORDER_REPLICATE)
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    contours = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]

    letter_image_regions = []

    for contour in contours:
        (x, y, w, h)  = cv2.boundingRect(contour)


        # x = points[0]
        # y = points[1]
        # w = points[2]
        # h = points[3]


        if w / h > 1.25:
            half_width = int(w / 2)
            letter_image_regions.append((x, y, half_width, h))
            letter_image_regions.append((x + half_width, y, half_width, h))
        else:
            letter_image_regions.append((x, y, w, h))

        if len(letter_image_regions) != 4:
            continue

    letter_image_regions = sorted(letter_image_regions, key=lambda x: x[0])

    for letter_bounding_box, letter_text in zip(letter_image_regions, functions.getFileName()):
        x, y, w, h = letter_bounding_box
        letter_image = image[y - 2:y + h + 2, x - 2:x + w + 2]

        save_path = os.path.join('OUTPUT_FOLDER', letter_text)
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        
        count = counts.get(letter_text, 1)
        p = os.path.join(save_path, "{}.png".format(str(count).zfill(6)))
        cv2.imwrite(p, letter_image)

        letters.append(letter_image)
        # cv2.imshow('image',letter_image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        counts[letter_text] = count + 1

    return letters