# Made with ❤️ in Python 3 by Alvison Hunter - July 10th, 2020
def get_middle(word):
    if(len(word) % 2 == 0):
        print("" + word[(int(len(word) / 2) - 1 )] + word[(int(len(word) / 2))])
    else:
        print(word[(int(len(word)/2))])

get_middle("test") 
get_middle("testing")
get_middle("middle") 
get_middle("A") 
