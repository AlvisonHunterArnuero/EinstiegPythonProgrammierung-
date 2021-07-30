# --------------------------------------------------------------------------------
# A group of spies want to send encrypted codes via automation. They have a generated
# encoded list for their superiors, with messages created with Uppercase letters
# separated with an space. We expect to have two separate lists from this list and
# first one must contain non repeated uppercases letters fron the initial list and in
# the second list we should reflect the amount of times each element of list1 is repeated
# This routine will allow them to send the msg with separated lists only if these exist.
# Made with ❤️ in Python 3 by Alvison Hunter - June 27th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# --------------------------------------------------------------------------------
from collections import Counter
# this is the list we will use as the base to create two separated ones
encrypted_msg = ['B', 'B', 'B', 'B', 'B', 'B', 'D', 'D', 'D',
                 'D', 'D', 'D', 'D', 'D', 'T', 'A', 'G', 'G', 'G', 'U', 'U', 'U']

# list1 contains all the letters(none repeated) of the base list, in uppercase mode
lst1 = Counter(encrypted_msg).keys()
# list2 reflect the amount of times each element of list1 is repeeated
lst2 = Counter(encrypted_msg).values()

# display on screen with a ternary operator to validate if the lists contains
# at least one element, meaning is not a none result.
print(lst1 or "No data returned")
print(lst2 or "No data returned")
