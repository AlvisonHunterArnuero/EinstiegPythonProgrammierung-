# -------------------------------------------------------------------------
# Create a function that takes a positive integer and returns the next
# bigger number that can be formed by rearranging its digits. For example:
# 12 ==> 21 |  513 == > 531 | 2017 == > 2071
# Made with ❤️ in Python 3 by Alvison Hunter Arnuero - May 5th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# -------------------------------------------------------------------------
import itertools

def next_bigger(n):
    final_number = ""
    next_num = [int(x) for x in str(n)]
    tmp_set = set(itertools.permutations(next_num))
    tmp_set.pop()
    print(tmp_set)
    # Create a new list which contains each member of the set,
    # so not great if your set is very large.
    tmp_lst = list(tmp_set)[0]
    print(tmp_lst)
    for el in tmp_lst:
        final_number += str(el)
    print(final_number[::-1])


next_bigger(12)  # 21
next_bigger(513)  #531
next_bigger(2017)  #2071
next_bigger(414)  #441
next_bigger(144)  #414
