# -------------------------------------------------------------------------
# Basic operations with colletion types | Python exercises | Beginner level
# Calculate sum & average of 5 given numbers entered by the user in a loop.
# Made with ❤️ in Python 3 by Alvison Hunter Arnuero - April 8th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# -------------------------------------------------------------------------

# [print(f"{c+1} - {item}") for c, item in enumerate(['a','b','c'])]
from itertools import permutations


def next_smaller(n):
    next_sm = 0
    is_found = False
    lst = list(str(n))
    while True:
        n -= 1
        perm = list(permutations(lst))
        if (len(perm) == 1):
            print("--")
            return -1
            break
        for ind, per in enumerate(perm):

            result = int(''.join(per))

            if result <= n:
                print(result)
                break
            else:
                continue

        for el in lst:
            is_found = True if el in lst else False
        if(is_found):
            break
        else:
            continue


next_smaller(21) == 12
next_smaller(531) == 513
next_smaller(2071) == 2017
next_smaller(907) # 790)
next_smaller(135) # -1)
next_smaller(2071) # 2017)
next_smaller(414) # 144)
next_smaller(123456798) # 123456789)
next_smaller(123456789) # -1)
next_smaller(1234567908) # 1234567890)
