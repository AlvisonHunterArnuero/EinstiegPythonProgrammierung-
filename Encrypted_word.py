#Encriptacion de palabras simple, algo bien sencillito nada fancy!
# Made with ❤️ in Python 3 by Alvison Hunter - November 29th, 2020
IN = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
OUT = "ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba"

def encrypt_phrase():
    str = input('Ingrese la frase que desea cifrar: \n')
    print (str.translate(str.maketrans(IN, OUT)))

encrypt_phrase()
