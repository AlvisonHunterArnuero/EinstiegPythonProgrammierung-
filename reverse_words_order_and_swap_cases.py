# Esta es una antigua Forma de comunicacion inventada por un famoso general salvadoreño
# llamado Francisco Malespin en 1845 a las tropas en el salvador, honduras y nicaragua.
# Made with ❤️ in Python 3 by Alvison Hunter - November 27th, 2020

IN = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
OUT = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def reverse_words_order_and_swap_cases(sentence):
    str_res = sentence.translate(sentence.maketrans(IN, OUT))
    lst = str_res.split()
    reversed_lst = lst[::-1]
    return (" ".join(reversed_lst))

reverse_words_order_and_swap_cases("rUns dOg")


