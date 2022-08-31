from googletrans import Translator
import pyttsx3

audio = pyttsx3.init()
audio.setProperty('rate', 150)

translate = Translator()
text = translate.translate('नमस्ते यह दुनिया की सबसे अच्छी जगह है जहाँ मैं कभी गया हूँ')
audio.say(text.text)
audio.runAndWait()
print(text.text)
