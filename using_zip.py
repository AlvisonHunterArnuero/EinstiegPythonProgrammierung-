# Using zip to package or unpackage list into dictionaries or viceversa
# Made with ❤️ in Python 3 by Alvison Hunter - January 14th, 2021
def list_to_iterable_obj_zip():
    lang_creators = ['Niklaus Wirth','Bjarne Stroustrup','Guido van Rossum','Anders Hejlsberg','Alan Cooper','Brendan Eich']
    favorite_languages = ['Pascal','C++','Python','C#','Visual Basic','JavaScript']
    try:
        # let's put these two lists together in an iterable object
        iterable_obj = zip(lang_creators,favorite_languages)
        # now let us create a list of tuples with these values
        lst_tuples = list(iterable_obj)
        print('-'*130)
        print('List of Tuples: \n',lst_tuples)
        # Next, let us create a dictionary with this new list
        print('Dictionary from list: \n',dict(lst_tuples))
        # We could even pass the list to separated tuples
        lang_creators_tuple, fav_langs_tuple = zip(*lst_tuples)
        print('='*130)
        print(f'Language Creators: \n{lang_creators_tuple} \nFavorite Languages: \n{fav_langs_tuple}')
        print('List based on Creators Tuple:\n',list(lang_creators_tuple))
        print('='*130)
    except ValueError as msg:
        print(msg)
        quit
    except:
        print('An unexpected error has ocurred. Program will shutdown now.')
        quit
    else:
        print('Thank you for using Python! Keep coding for the world.')


list_to_iterable_obj_zip()
