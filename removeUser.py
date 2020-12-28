# Made with ❤️ in Python 3 by Alvison Hunter - December 28th, 2020
import random
def remove_lang_creator(arg_remove):
    name = ''
    if arg_remove:
        devs_lst = ["Guido van Rossum","Yukihiro Matsumoto", "James Gosling", "Dennis Ritchie", "Bjarne Stroustrup", "Rasmus Lerdorf", "Brendan Eich"]
        name = random.choice(devs_lst)
        devs_lst.remove(name)
        print(name)
        print(f"{str(name)} was successfully removed from our List.")
        return
remove_lang_creator(True)
