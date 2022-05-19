from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
import pytesseract

filename = "sample.jpeg"
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = np.array(Image.open(filename))

text = pytesseract.image_to_string(img)

print("Resultado: ", text)
