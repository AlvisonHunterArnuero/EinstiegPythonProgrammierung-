#Convert list of lists into a single list with 3 different methods
# Made with ❤️ in Python 3 by Alvison Hunter - October 11th, 2020
lst_best_football_players = [['Cristiano Ronaldo', 'Lionel Messi'],['Antoine Griezmann', 'Mohamed Salah']]

def transform_to_single_list(lst_obj):
    print("Original list of lists",lst_obj)
    #Method 1
    nested_list_comprehension = [x for l in lst_best_football_players for x in l]
    #Method 2
    unpack_list = [*lst_best_football_players[0], *lst_best_football_players[1]]
    #Method 3
    extend_list = []
    for l in lst_best_football_players:
        extend_list.extend(l)

    print("Method 1: List Comprehension")
    print(nested_list_comprehension)
    print("Method 2: Using the unpacking operator to get these values in a single variable")
    print(unpack_list)
    print("Method 3: Extend Method")
    print(extend_list)

#let's put this into action
transform_to_single_list(lst_best_football_players)

