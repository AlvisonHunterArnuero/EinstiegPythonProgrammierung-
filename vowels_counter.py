# -------------------------------------------------------------------------
# This routine counts all vowels present in a sentence typed by the user
# Made with ❤️ in Python 3 by Alvison Hunter - January 24th, 2022
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# -------------------------------------------------------------------------
from collections import defaultdict

word = input("Enter a Phrase: ")
counter = defaultdict(int)
for letter in word.casefold():
    if(letter in "aeiou"):
        counter[letter] += 1
        
print(dict(counter))