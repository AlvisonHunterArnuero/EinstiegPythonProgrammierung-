# -------------------------------------------------------------------------
# Basic operations with Python 3 | Python exercises | Beginner level
# check if a given word typed by the user has all vowels included, if all
# vowels are present in the given word, return True or False otherwise.
# Made with ❤️ in Python 3 by Alvison Hunter Arnuero - May 31st, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# -------------------------------------------------------------------------

vowels_lst = ["a", "e", "i", "o", "u"]
# Some Spanish examples of these words just in case you need them
# "Murcielago", "Cuestionar", "Secundario", "Hipotenusa", "Mozambique"


def check_vowels(word):
    for letter in vowels_lst:
        if letter not in word.lower():
            return False
    return True


# Let us give this function a try, shall we?
w = input("Enter a word: \n")
print(check_vowels(w))
