# Write a function named first_non_repeating_letter that takes a string input, and returns the
# first character that is not repeated anywhere in the string.
# For example, if given the input 'stress', the function should return 't', since the letter t
# only occurs once in the string, and occurs first in the string.

# As an added challenge, upper- and lowercase letters are considered the same character,
# but the function should return the correct case for the initial letter. For example, the input 'sTreSS'
# should return 'T'.
# If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.
def first_non_repeating_letter(sentence):
    word_counts = list(sentence)
    res = None
    for w in word_counts:
        if(word_counts.count(w.upper())==len(word_counts)):
            print('None: Letras todas repetidas')
            res = None
            return res
        elif(word_counts.count(w)<=1):
            res = w
            print('Letra no repetida es: ',res)
            return res
        else:
            pass

    print('Final Result',res)
    return res


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





