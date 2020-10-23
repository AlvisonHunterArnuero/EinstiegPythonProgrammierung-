# Build Tower by the following given argument:
# number of floors (integer and always greater than 0).
# Tower block is represented as *  | Python: return a list;
# Made with ❤️ in Python 3 by Alvison Hunter - Friday, October 16th, 2020
def tower_builder(n_floor):
    lst_tower = []
    pattern = '*'
    width = (n_floor * 2) - 1
    for items in range(1, 2 * n_floor, 2):
        asterisks = items * pattern
        ln = asterisks.center(width)
        lst_tower.append(ln)
    print(lst_tower)
    return lst_tower

#let's test it out!
tower_builder(1)# ['*', ])
tower_builder(2)# [' * ', '***'])
tower_builder(3)# ['  *  ', ' *** ', '*****'])
