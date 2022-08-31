# import cv2
import pytesseract
import numpy as np


def textdetection(img):
    pytesseract.pytesseract.tesseract_cmd = r"D:\Other Files\Tesseract\tesseract\tesseract.exe"
    boxes = pytesseract.image_to_boxes(img)
    s1 = pytesseract.image_to_string(img)
    s = ''
    for b in boxes.splitlines():
        b = b.split(' ')
        s = s + b[0]
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    if s == '~':
        return 'No Text Detected'
    else:
        return  s1.split('  ')
img = r"D:\ONEDRIVE\Desktop\alt text.jpg"
s = textdetection(img)
#print(s)


