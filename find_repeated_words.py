# Made with ❤️ in Python 3 by Alvison Hunter - April  12th, 2021
# Tips de Python & JavaScript en: https://bit.ly/3p9hpqj
from collections import Counter
phrase = "Esto es una repeticion de palabras para ver que si esto funciona con las palabras que el usuario escoja"
found = False
fetched_word = input("Palabra a buscar: ")
if fetched_word == "":
    fetched_word = "--"

for k, v in Counter(phrase.split()).items():
    if (k.lower() == fetched_word.lower()):
        ocurrences = "veces" if v > 1 else "vez"
        print(f"[{fetched_word}] se encuentra {v} {ocurrences} en la frase.")
        found = True

if(not found):
    print(f"[{fetched_word}] no se encuentra en la frase.")
