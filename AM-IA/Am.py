from ast import IsNot
from matplotlib import pyplot as plt
import numpy as np
import cv2
from PIL import Image
import pytesseract
from pytesseract import Output

filename = "curriculo_exemplo.jpg"
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread(filename)

imgH, imgW = img.shape[:2]

imgRs = cv2.resize(img, (imgW * 2, imgH * 2), interpolation=cv2.INTER_AREA)

imgRs = cv2.GaussianBlur(imgRs, (5, 5), 0)
frame, imgRs = cv2.threshold(imgRs, 137, 255, cv2.THRESH_BINARY)

results = pytesseract.image_to_data(imgRs, output_type=Output.DICT)

nome = ''
obj = ''
educ = ''
exp = ''
for i in range(0, len(results["text"])):
    x = results["left"][i]
    y = results["top"][i]

    w = results["width"][i]
    h = results["height"][i]

    text = results["text"][i]
    conf = int(results["conf"][i].split('.')[0])
    if conf > 1:
        if results["text"][i] == 'Fernanda':
            text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
            cv2.rectangle(imgRs, (x, y), (x + w, y + h), (0, 255, 0), 2)
            nome = nome + " " + results["text"][i]

        if results["text"][i] == 'Silva':
            text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
            cv2.rectangle(imgRs, (x, y), (x + w, y + h), (0, 255, 0), 2)
            nome = nome + " " + results["text"][i]

        if results["text"][i] == 'Trentin':
            text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
            cv2.rectangle(imgRs, (x, y), (x + w, y + h), (0, 255, 0), 2)
            nome = nome + " " + results["text"][i]

        if results["text"][i] == 'OBJETIVO:':
            text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
            cv2.rectangle(imgRs, (x, y), (x + w, y + h), (0, 255, 0), 2)
            obj = obj + " " + results["text"][i]

        if results["text"][i] == 'Posicdo':
            text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
            cv2.rectangle(imgRs, (x, y), (x + w, y + h), (0, 255, 0), 2)
            obj = obj + " " + results["text"][i]

        if results["text"][i] == 'geréncia':
            text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
            cv2.rectangle(imgRs, (x, y), (x + w, y + h), (0, 255, 0), 2)
            obj = obj + " " + results["text"][i]

        if results["text"][i] == 'area':
            text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
            cv2.rectangle(imgRs, (x, y), (x + w, y + h), (0, 255, 0), 2)
            obj = obj + " " + results["text"][i]

        if results["text"][i] == 'contabilidade':
            text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
            cv2.rectangle(imgRs, (x, y), (x + w, y + h), (0, 255, 0), 2)
            obj = obj + " " + results["text"][i]

        if results["text"][i] == 'Mestrado':
            text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
            cv2.rectangle(imgRs, (x, y), (x + w, y + h), (0, 255, 0), 2)
            educ = educ + " " + results["text"][i]

        if results["text"][i] == 'Econom':
            text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
            cv2.rectangle(imgRs, (x, y), (x + w, y + h), (0, 255, 0), 2)
            educ = educ + " " + results["text"][i]

        if results["text"][i] == 'Experinéncia':
            text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
            cv2.rectangle(imgRs, (x, y), (x + w, y + h), (0, 255, 0), 2)
            exp = exp + " " + results["text"][i]

        if results["text"][i] == 'desde':
            text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
            cv2.rectangle(imgRs, (x, y), (x + w, y + h), (0, 255, 0), 2)
            exp = exp + " " + results["text"][i]

        if results["text"][i] == '2009':
            text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
            cv2.rectangle(imgRs, (x, y), (x + w, y + h), (0, 255, 0), 2)
            exp = exp + " " + results["text"][i]

        if results["text"][i] == 'area.':
            text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
            cv2.rectangle(imgRs, (x, y), (x + w, y + h), (0, 255, 0), 2)
            exp = exp + " " + results["text"][i]

        if results["text"][i] == 'tendo':
            text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
            cv2.rectangle(imgRs, (x, y), (x + w, y + h), (0, 255, 0), 2)
            exp = exp + " " + results["text"][i]

        if results["text"][i] == 'atuado':
            text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
            cv2.rectangle(imgRs, (x, y), (x + w, y + h), (0, 255, 0), 2)
            exp = exp + " " + results["text"][i]

        if results["text"][i] == 'exclusivamente':
            text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
            cv2.rectangle(imgRs, (x, y), (x + w, y + h), (0, 255, 0), 2)
            exp = exp + " " + results["text"][i]

        if results["text"][i] == 'no':
            text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
            cv2.rectangle(imgRs, (x, y), (x + w, y + h), (0, 255, 0), 2)
            exp = exp + " " + results["text"][i]

        if results["text"][i] == 'setor':
            text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
            cv2.rectangle(imgRs, (x, y), (x + w, y + h), (0, 255, 0), 2)
            exp = exp + " " + results["text"][i]

        if results["text"][i] == 'contatulidade':
            text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
            cv2.rectangle(imgRs, (x, y), (x + w, y + h), (0, 255, 0), 2)
            exp = exp + " " + results["text"][i]


#print("Conf: ", results["conf"])
#print("Text: ", results["text"])
print("Nome: ", nome)
print(obj)
print("Educação: ", educ, " ", results["text"][81])
print("Experiencia: ", exp)
# print(imgRs.shape[:2])

plt.imshow(imgRs)
plt.show()
