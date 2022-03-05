# -------------------------------------------------------------------------
# Given a phrase, along with a vowel, convert it to upper in the phrase
# Made with ❤️ in Python 3 by Alvison Hunter - January 14th, 2022
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# -------------------------------------------------------------------------

import re
while True:
    phrase = input("Please enter Phrase: ")
    vowel = input("Please enter Vowel: ")
    if vowel not in "AEIOUaeiou":
        print(phrase)
        break
    else:
        print(re.sub(rf"{vowel}", vowel.upper(), phrase))
        break
    
