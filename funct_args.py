# function declaration and argument types
# Python Keyword Arguments
# Python Arbitrary Arguments
# Made with ❤️ in Python 3 by Alvison Hunter - December 9th, 2020
def developer(*names):
    for el in names:
        print(f'Python is the favorite language of {el}.')

developer('Bill Gates','Guido Van R.', 'Engel Torrez', 'Ernesto Gutierrez', 'Alvison Hunter','David Arauz')

