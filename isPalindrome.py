import re
def is_palindrome():
    phrase = input("Please enter your word: \n")
    forwards = ''.join(re.findall(r'[a-z]+',phrase.lower()))
    backwards = forwards[::-1]
    boolResponse = forwards == backwards
    return print(f"Is this a Palindrome? {boolResponse}")

is_palindrome()
