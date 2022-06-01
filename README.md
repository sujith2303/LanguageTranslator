# LanguageTranslator
Takes in an image of text, process it, and gives an audio output of the text in the user-specified language(around 99 different languages). Can able to identify 80 different languages of text(computer as well as handwritten).

# Downloading Dependencies
[Tesseract-OCR](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.1.0.20220510.exe) click here to download Tesseract into your computer.
## Installation 
You can  simply use pip to install the latest version of pytesseract.

> ***`pip install pytesseract`***

### Other Dependencies
Copy the below commands and paste in your command prompt to download the necessities.

> ***`pip install opencv-python`***

> ***`pip install pyttsx3`***

> ***`pip install googletrans`***

<br>

# Steps to follow to run your Language Translator

1. After Downloading all the dependencies, run main.py. You can do it from your ide or if you want it to run from command prompt run the below code
2. ***`py main.py`*** or ***`python -m main.py`***
3. When you run main you need to choose an option of translating from an image or from webcam.

# Working

1. Just writing 2 lines of code helps you to convert the hand writing of your wish.
2. The main step is to create a folder and place all the images of alphabets with the same name of it (i.e., save image of a with name a and image of numbers with the same number and any special symbol with same symbol name.
3. Sample of the folder is shown above
4. Add and empty white image and save it with name '.png or '.jpg . It is used for whitespace character.

## Coding part:-

1. The first step is to create an object of the class HandWritingConverter with the following arguments
  1. Image which you want to convert
  2. Image height
  3. Image width
  4. path to the handwriting folder
  5. path to the tesseract file (the one which you have downloaded from Downloading Dependencies.
2. So just creating the object does every thing to you . Congratulations you have successfully coded to convert handwriting
### Code:-

1. Importing packages needed
<pre>
import HandWriting_final as hf
</pre>
2. Creating the variables
<pre>
path_to_image = r''             # give the path to image in ''
path_to_handwriting = r''       # give the path to handwriting in ''
path_to_tesseract = r''         # give the path to tesseract in ''
</pre>
3. Creating an instance of object
<pre>
image_original = cv2.imread(path_to_image)
height,width,_ = image_original.shape
obj = hf.HandWritingConverter(image_original,height,width,path_to_handwriting,path_to_tesseract)
</pre>
4. Click on any key to stop viewing the image window
5. If you would like to try multiple handwritings simultaneously just create multiple instances of the object
<pre>
obj = hf.HandWritingConverter(image_original,height,width,path_to_handwriting1,path_to_tesseract)
obj = hf.HandWritingConverter(image_original,height,width,path_to_handwriting2,path_to_tesseract)
</pre>
