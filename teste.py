from matplotlib import pyplot as plt
import numpy as np
import cv2
from PIL import Image
import pytesseract
from pytesseract import Output

filename = "sample.jpeg"
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread(filename)
#img = np.array(Image.open(filename))
#norm_img = np.array(Image.open(filename))

# Conversão Img2Dict
results = pytesseract.image_to_data(img, output_type=Output.DICT)

# Bounding box arredor do texto
for i in range(0, len(results["text"])):
    x = results["left"][i]
    y = results["top"][i]

    w = results["width"][i]
    h = results["height"][i]

    text = results["text"][i]
    conf = int(results["conf"][i].split('.')[0])
    # A função Int() não pode receber valores double, como no caso do dado "conf" da imagem (95.572105), para resolver o problema, é usada a função split() onde o valor é divido no ponto "." e é utilizado apenas o índice[0], ou seja, 95
    # Neste caso não se faz necessário o arredondamento, mas se sim, o problema pode ser solucionado com if(results["conf"][i].split('.')[1][0] > 6): conf = int(results["conf"][i].split('.')[0]) + 1
    # A função round não pode ser usada neste caso pelo fato de type(results["conf"][i]) = str ; a função round apenas aceita valores int

    if conf > 70:
        text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(img, text, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 200), 2)

# Redução de ruido da imagem "sample2.png"
#cv2norm_img = np.zeros((img.shape[0], img.shape[1]))
#img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
#img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]
#img = cv2.GaussianBlur(img, (1, 1), 0)

plt.imshow(img)
plt.show()

# Conversão Img2String
#text = pytesseract.image_to_string(img)

#print("Resultado: ", results)
