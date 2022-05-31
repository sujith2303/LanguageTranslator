import numpy as np
import cv2
import os
import json
import pytesseract

class user_alphabets:
    def __init__(self,path):
        print(path + r'\alphabet_dictionary.txt')
        if os.path.exists(path+r'\alphabet_dictionary.txt'):
            self.alphabet_dictionary = json.load(open(os.path.join(path,r'\alphabet_dictionary.txt')))
            print('Loaded the file Successfully !!!!!!!!!')
        else:
            self.alphabet_dictionary = self.read_alphabets(path)
            json.dump(self.alphabet_dictionary, open(path+r'\alphabet_dictionary.txt', 'w'))

    def read_alphabets(self,path):
        d = {}
        for i in os.listdir(path):
            if i.endswith('.txt'):
                continue
            j = i.split('.')[0]
            img = cv2.imread(os.path.join(path, i))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img = cv2.resize(img, (20, 20))
            d[j] = img.tolist()
        return d

class textdetection:
    def __init__(self,path,img):
        pytesseract.pytesseract.tesseract_cmd = path
        self.text = pytesseract.image_to_string(img)
if __name__=='__main__':
    a = user_alphabets("D:\ONEDRIVE\Desktop\Alphabets_sujith")
    path = r"D:\Other Files\Tesseract\tesseract\tesseract.exe"   #path to tesseract file
    image = r"D:\ONEDRIVE\Desktop\alt text.jpg"
    b = textdetection(path,image)
    print(b.text)