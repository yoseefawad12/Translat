
from googletrans import Translator

print("download vide YouTube")
print("programer Zero")

translator = Translator()

text = input("text Translator : ")

translated = translator.translate(text, dest='ar')

print(translated.text)