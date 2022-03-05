# -------------------------------------------------------------------------
# Given a phrase, along with a vowel, convert it to upper in the phrase
# Made with ❤️ in Python 3 by Alvison Hunter - January 14th, 2022
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# -------------------------------------------------------------------------


digits = {0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
num = input("Enter number: ")
x = '<br/>'.join([f'{value}' for key, value in digits.items()])
print(x)