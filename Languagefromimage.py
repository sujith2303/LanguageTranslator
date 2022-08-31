import cv2
import pytesseract
import pyttsx3
from googletrans import Translator

translate = Translator()

video = cv2.VideoCapture(0)

audio = pyttsx3.init()
audio.setProperty('rate', 150)


pytesseract.pytesseract.tesseract_cmd = r"D:\Other Files\Tesseract\tesseract\tesseract.exe"

lang='tel'
while True:
    _, img = video.read()
    hImg, wImg, _ = img.shape
    cv2.imshow('img', img)
    text = pytesseract.image_to_string(img,lang=lang)
    print(text)
    translated_text = translate.translate(text)
    print(translated_text.text)
    audio.say(translated_text.text)
    audio.runAndWait()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyWindow()

'''cv2.imshow('img', img)
    text = pytesseract.image_to_string(img,lang='tel')
    translated_text = translate.translate(text)
    string = f'detected {LANGUAGES[translated_text.src]} language and converted into {translated_text.text}'
    audio.say(string)
    audio.runAndWait()'''
