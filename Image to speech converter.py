import cv2
import pytesseract
import pyttsx3
from Language_Converter import translater



__author__ = 'Sujith Anumala'
print(f'This is language Translator has been implemented by {__author__}')

class Language_Translator:
  def __init__(self,path=None):
    self.path = path
    if not path:
        raise FileNotFoundError('Enter a valid path for tesseract file (link provided in readme)')
    print('Loaded the file successfully..........!')
    
  def Video(self,show = True):
    video = cv2.VideoCapture(0)
    audio = pyttsx3.init()
    audio.setProperty('rate', 150)
    voices = audio.getProperty('voices')
    audio.setProperty('voice', voices[0].id)
    try:
      pytesseract.pytesseract.tesseract_cmd = self.path
    except:
      raise FileNotFoundError('Please enter a valid path for tesseract file')
    while True:
        _, img = video.read()
        hImg, wImg, _ = img.shape
        #s = pytesseract.image_to_string(img)
        key = cv2.waitKey(1)
        if key == ord('t'):
            s = pytesseract.image_to_string(img,lang='tel')
            c = 'tel'
        elif key == ord('j'):
            s = pytesseract.image_to_string(img,lang ='Japanese')
            c = ''
        elif key == ord('k'):
            s = pytesseract.image_to_string(img, lang='Kannada')
        elif key == ord('b'):
            s = pytesseract.image_to_string(img, lang='Bengali')
        elif key == ord('g'):
            s = pytesseract.image_to_string(img, lang='Gujarati')
        elif key == ord('m'):
            s = pytesseract.image_to_string(img, lang='Malayalam')
        else:
            s = pytesseract.image_to_string(img)
        '''boxes = pytesseract.image_to_boxes(img)
        s = ''
        for b in boxes.splitlines():
            # print(b)
            b = b.split(' ')
            s = s + b[0]
            x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
            cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (50, 50, 255), 2)
            cv2.putText(img, b[0], (x, hImg - y + 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)
    '''
        cv2.imshow('img', img)
        s = translater(s)
        if s == None:
            audio.say('No Text Detected')
        else:
            print(s)
            audio.say(s)
        audio.runAndWait()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video.release()
    cv2.destroyWindow()



