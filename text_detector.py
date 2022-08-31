import pytesseract
from PIL import Image
from skimage.morphology import opening
from skimage.morphology import disk
import numpy as np
import cv2

black = 0
white = 255
threshold = 160

pytesseract.pytesseract.tesseract_cmd = r"D:\Other Files\Tesseract\tesseract\tesseract.exe"

def textdetection(img):
    pixels = np.array(img)[:, :, 0]
    pixels[pixels > threshold] = white
    pixels[pixels < threshold] = black
    blobSize = 1
    structureElement = disk(blobSize)
    pixels = np.invert(opening(np.invert(pixels), structureElement))

    newImg = Image.fromarray(pixels).convert('RGB')
    newImg.save('Sujith.PNG')

    boxes = pytesseract.image_to_string(img)
    s = ''
    '''for b in boxes.splitlines():
        b = b.split(' ')
        s = s + b[0]'''
    if s == None:
        return 'No Text Detected'
    return 'detected text'+' ' + str(s)


