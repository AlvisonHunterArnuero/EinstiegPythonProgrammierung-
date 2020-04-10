import os
def changeNameLastName():
    print ('░'*60)
    print('hello '+ os.getlogin() +', How are you?')
    print ('≡'*60)
    str01 = input('º What is your name? ')
    str02  = input('º What is your last name? ')
    tmp = ""
    tmp = '{0}, {1}'.format(str01.upper(), str02.upper())
    str02 = '{0}, {1}'.format(str02.upper(), str01.upper())
    str01 = tmp
    print('Let us switch these strings, will ye?:\n')
    print(f'» Original string was: {str01}. \n » Switched String: {str02}')
    print ('≡'*60)
    print('Happy Python Coding, Viva Nicaragua!'.upper())
    print ('░'*60)
changeNameLastName()
