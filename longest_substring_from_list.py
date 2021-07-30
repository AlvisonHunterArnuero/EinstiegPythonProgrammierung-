# -------------------------------------------------------------------------
# Basic operations with colletion types | Python exercises | Beginner level
# Find the longest substr of a string, display it on the screen afterwards
# Made with ❤️ in Python 3 by Alvison Hunter Arnuero - April 8th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# -------------------------------------------------------------------------
phrase = "caracter"
substr_lst = []
lst_elem = ""
while True:
    if(len(phrase) <= 1):
        break
    for i, v in enumerate(phrase):
        if phrase[i] in lst_elem:
            substr_lst.append(lst_elem)
            phrase = lst_elem[-1] + phrase.split(lst_elem, 1)[1]
            lst_elem = ""
            break
        else:
            lst_elem += phrase[i]
if(len(substr_lst) <= 0):
    print("-1")
else:
    print(f"Longest Substring: {max(substr_lst)}")
