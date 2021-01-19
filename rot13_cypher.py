#ROT13 is a simple letter substitution cipher that replaces a letter with
#the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

#Create a function that takes a string and returns the string ciphered with Rot13.
#If there are numbers or special characters included in the string, they should be
#returned as they are. Only letters from the latin/english alphabet should be shifted,
#like in the original Rot13 "implementation".

# Made with ❤️ in Python 3 by Alvison Hunter - January 17th, 2021
UNCYPHERED ="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
ROT13="NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
def rot13(message):
    ciphered_str = message.translate(message.maketrans(UNCYPHERED, ROT13))
    print(ciphered_str)

#let us call the function with capitalized text
rot13("This  Is Rot13 Cypher From Carazo, Nicaragua.")
# then will uppercase text
rot13("THIS  IS ROT13 CYPHER FROM CARAZO, NICARAGUA.")
# last but not least, let us do it with lowercase text
rot13("this  is rot13 cypher from carazo, nicaragua.")
