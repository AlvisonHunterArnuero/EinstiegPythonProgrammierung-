from itertools import chain
inputlist = [[8, 3, 8], [6, 2, 9], [7, 1, 5]]
def avelist(inputlist):
    lst = list(chain.from_iterable(inputlist))
    return sum(lst) / len(lst)

    return  print(f" This is the total {total}")
