# Alpha 0.01 - Image Text Translator

from PIL import Image
from pytesseract import pytesseract
from deep_translator import GoogleTranslator
import cv2
import numpy as np


path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_path = r"C:\Users\Kaan\Desktop\Image Text Translator\example_text.PNG"

img = Image.open(image_path)

pytesseract.tesseract_cmd = path_to_tesseract

text = pytesseract.image_to_string(img)

# dont forget edit the path!
with open(r"C:\Users\Kaan\Desktop\Image Text Translator\saved_text.txt", "w") as f:
    f.write(text[:-1])

translated = GoogleTranslator(source='en', target='tr').translate_file(r'C:\Users\Kaan\Desktop\Image Text Translator\saved_text.txt')

file = open(r"C:\Users\Kaan\Desktop\Image Text Translator\translated_text.txt", "w")
file.write(translated)
file.close()

txt = []

# take image size
img_size = cv2.imread(r"C:\Users\Kaan\Desktop\Image Text Translator\example_text.PNG")
width = img_size.shape[1]
height = img_size.shape[0]

image = cv2.imread(r'C:\Users\Kaan\Desktop\Image Text Translator\example_text.PNG')
x,y,w,h = 0,0,width,height

# black background
cv2.rectangle(image, (x, x), (x + w, y + h), (0,0,0), -1)

# add text
file = open(r"C:\Users\Kaan\Desktop\Image Text Translator\translated_text.txt", "r")
txt = file.read()
file.close()

cv2.putText(image, txt, (x + int(w/10),y + int(h/2)), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255,255,255), 1, cv2.LINE_AA)

# show and save
cv2.imshow('image', image)
cv2.imwrite(r'C:\Users\Kaan\Desktop\Image Text Translator\Translated File\translatedimage.png', image)
cv2.waitKey()
