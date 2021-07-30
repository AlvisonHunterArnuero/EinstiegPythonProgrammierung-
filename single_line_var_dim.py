# --------------------------------------------------------------------------------
# Declare variables to be used in several cases. reset when needed in a single line.
# Made with ❤️ in Python 3 by Alvison Hunter - June 27th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# --------------------------------------------------------------------------------
import random as r


def example():
    first_val = second_val = 2 if(r.randint(0, 50) <= 24) else 1
    print(first_val, second_val)

# Test drive this function
example()


