#Move the first letter of each word to the end of it, then add "ay"
# to the end of the word. Leave punctuation marks untouched.
# Made with ❤️ in Python 3 by Alvison Hunter - October 13th, 2020

def pig_it(str_arg):
    new_string = ''
    lst1 = list(str_arg.split(' '))

    for elem in lst1:
        if(elem.isalnum()):
            new_string += elem[1:] + elem[:1] + "ay "
        else:
            new_string += elem +" "

    print('New String is: ',new_string)
    return new_string[:-1]

#Let us try our logic on this one, I included some latin lingo in the last two test cases!
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
pig_it('O tempora o mores !')# Oay emporatay oay oresmay !
pig_it('Quis custodiet ipsos custodes ?')# uisQay ustodietcay psosiay ustodescay ?'
