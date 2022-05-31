import string

import HandWriting_final_utils
import cv2
import numpy as np

class HandWritingConverter:
    def __init__(self,original_image,height,width,path_to_handwriting,path_to_tesseract_file):
        self.original_image = original_image
        A = HandWriting_final_utils.user_alphabets(path_to_handwriting)
        self.dictionary = A.alphabet_dictionary
        string = HandWriting_final_utils.textdetection(path_to_tesseract_file,original_image)
        self.handwriting(string,self.dictionary,width,height)

    def handwriting(self,string,dictionary,width,height):
        blank_img = np.zeros([height, width])
        blank_img.fill(1)
        no_letters = width//25
        string = string.text.replace(' ',"'")
        string = string.replace(r'\n','|')
        constant = 0
        print(string)
        for i in range(len(string)-1):
            a = string[i].lower()
            if a not in self.dictionary and a!='\n':
                continue
            if a=='\n':
                constant+=5
                continue
            img = self.dictionary[a]
            x = 20 * (i % no_letters) + 10
            y  = (i//no_letters) * 30 + constant
            for k in range(20):
                for l in range(20):
                    if img[k][l] < 100:
                        blank_img[y + k][x + l] = 0
        cv2.imshow('img',blank_img)
        cv2.imshow('original',self.original_image)
        cv2.waitKey(0)

if __name__=='__main__':
    img_original = r"D:\ONEDRIVE\Desktop\img.png"
    image_original = cv2.imread(img_original)
    height,width,_ = image_original.shape
    obj = HandWritingConverter(image_original,height,width,r"D:\ONEDRIVE\Desktop\Alphabets_cursive",r"D:\Other Files\Tesseract\tesseract\tesseract.exe")