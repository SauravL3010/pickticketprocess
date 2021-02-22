import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image = cv2.imread("test.png")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

threshold_img = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# cv2.imshow('threshold image', threshold_img)

# cv2.waitKey(0)

# cv2.destroyAllWindows()

custom_config = r'--oem 3 --psm 6'
details = pytesseract.image_to_data(threshold_img, output_type=pytesseract.Output.DICT, config=custom_config, lang='eng')

total_boxes = len(details['text'])

for sequence_number in range(total_boxes):
    if int(details['conf'][sequence_number]) >30:
        (x, y, w, h) = (details['left'][sequence_number], details['top'][sequence_number], details['width'][sequence_number],  details['height'][sequence_number])
        threshold_img = cv2.rectangle(threshold_img, (x, y), (x + w, y + h), (0, 255, 0), 2)

print(details['text'])

cv2.imshow('captured text', threshold_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(details['text'])