
#ROT13 is a simple letter substitution cipher that replaces a letter with
#the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

#Create a function that takes a string and returns the string ciphered with Rot13.
#If there are numbers or special characters included in the string, they should be
#returned as they are. Only letters from the latin/english alphabet should be shifted,
#like in the original Rot13 "implementation".
# Made with ❤️ in Python 3 by Alvison Hunter - December 2nd, 2020
UNCYPHERED ="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
ROT13="NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
def rot13(message):
    ciphered_str = message.translate(message.maketrans(UNCYPHERED, ROT13))
    print(ciphered_str)


#let us call the function here now.
rot13("alvison hunter")
rot13("Alvison Hunter")
