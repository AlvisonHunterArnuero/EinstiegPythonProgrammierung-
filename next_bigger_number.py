# -----------------------------------------------------------------------------
# Description: Create a function that takes a positive integer and returns the
# next bigger number that can be formed by rearranging any of its digits.
# Author: Made with ❤️ in Python 3 by Alvison Hunter - June 11th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# -----------------------------------------------------------------------------
from itertools import permutations


def next_bigger(n):
    next_big_num = ""
    lst = list(str(n))

    # let's start with the conditionals
    if((len(lst) == 1) or (len(lst) == 3 and (lst[0] == lst[1] and lst[1] == lst[2]))):
        next_big_num = '-1'

    if(len(lst) == 2):
        lst.reverse()
        validator = ''.join(str(el) for el in lst)
        if(int(validator) > n):
            next_big_num = validator
        else:
            next_big_num = '-1'

    # We will use permutations. We could've applied it to
    # the entire code but I have another idea for numbers
    # bigger than three digits, so, let's do it, folks!
    if(len(str(n)) == 3):
        perm_lst = []
        perm_tpl = permutations(lst)
        for tpl in perm_tpl:
            str_num = ''.join(str(el) for el in tpl)
            perm_lst.append(int(str_num))
        perm_lst.sort()

        for p in perm_lst:
            if(int(p) > n):
                next_big_num = p
                break

    # Let's use another algorithm here. First, I will find the part of the
    # number that shouldna change, then find the right part of the number
    # that actually changes to make the number the next bigger, and finally
    # find the pivot number in between these 2 parts so that I can increment
    # number only with the right part by sorting the left again once I reach
    # the next bigger number. Can this be made with permutations, yes, but
    # I would like to experience it with this other idea, I think it'll work

    if(len(lst) > 3):
        # Reversing the list first to find the common pivot
        lst.reverse()
        # getting a common pivot number to compare the others
        pivot = lst[0]

        # let's find the pivot, split the list and make the
        # changes in order to find th next number, shall we?
        for idx, elem in enumerate(lst):
            if(int(elem) < int(pivot)):
                pivot = elem
                heads = lst[idx+1:]
                tail = lst[:idx]
                # With thi for, I will find the popped number
                # that will replace the pivot to alter the original number
                for i, n in enumerate(tail):
                    # Once found, insert it in tails, break the loop
                    if(int(n) > int(elem)):
                        popped = n
                        tail[i] = elem
                        tail.insert(0, popped)
                        break
                    else:
                        pass
                # sort the list now, to built the final number
                heads.reverse()
                final_lst = heads + tail
                next_big_num = ''.join(str(e) for e in final_lst)
                break
            else:
                pivot = elem

    # Well, now that we have it, if the value is none or empty, return -1 otherwise
    # return the integer value of next_big_num, using a ternary operator for it.
    return(-1) if(next_big_num == None or next_big_num == '') else (int(next_big_num))


print(next_bigger(9))  # -1
print(next_bigger(12))  # returns 21
print(next_bigger(96))  # -1
print(next_bigger(111))  # -1
print(next_bigger(414))  # 441
print(next_bigger(144))  # 414
print(next_bigger(531))  # -1
print(next_bigger(513))  # returns 531
print(next_bigger(708))  # 780
print(next_bigger(783))  # 837
print(next_bigger(2017))  # returns 2071
print(next_bigger(21581957621))  # 21581961257
print(next_bigger(59884848459853))  # 59884848483559
