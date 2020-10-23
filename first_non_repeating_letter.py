"""
Write a function named first_non_repeating_letter that takes a string input, and returns the
first character that is not repeated anywhere in the string.
For example, if given the input 'stress', the function should return 't', since the letter t
only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character,
but the function should return the correct case for the initial letter. For example, the input 'sTreSS'
should return 'T'.
If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.
"""

from collections import Counter
def first_non_repeating_letter(sentence):
    word_counts = Counter(sentence)

    for word, count in word_counts.items():
        if(count ==1):
            print(word)
            return word
        elif(count>1):
            print("None")
            return None

first_non_repeating_letter('a')
first_non_repeating_letter('aaa')
first_non_repeating_letter('stress')
first_non_repeating_letter('moonmen')
first_non_repeating_letter('')
first_non_repeating_letter('abba')
first_non_repeating_letter('aa')
first_non_repeating_letter('~><#~><')
first_non_repeating_letter('hello world, eh?')
first_non_repeating_letter('sTreSS')
first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!')





