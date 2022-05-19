from matplotlib import pyplot as plt
import numpy as np
import cv2
from PIL import Image
import pytesseract
from pytesseract import Output

filename = "curriculo_exemplo.jpg"
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread(filename)

results = pytesseract.image_to_data(img, output_type=Output.DICT)

for i in range(0, len(results["text"])):
    x = results["left"][i]
    y = results["top"][i]

    w = results["width"][i]
    h = results["height"][i]

    text = results["text"][i]
    conf = int(results["conf"][i].split('.')[0])
    if conf > 0:
        if results["text"][i] == 'Fernanda' or 'Silva' or 'Trentin':
            #text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # cv2.putText(img, text, (x, y - 10),
            #            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 200), 2)

print("Conf: ", results["conf"])
print("Text: ", results["text"])
plt.imshow(img)
plt.show()
