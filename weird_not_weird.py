# -------------------------------------------------------------------------
# Given an integer,n, perform the following conditional actions:
# If  n is odd, print Weird
# If  n is even and in the inclusive range of 2 to 5, print Not Weird
# If  n is even and in the inclusive range of 6 to 20, print Weird
# If  n is even and greater than 20, print Not Weird
# Input Format: A single line containing a positive integer, n.
# -------------------------------------------------------------------------
# Made with ❤️ in Python 3 by Alvison Hunter - August 12th, 2022
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# -------------------------------------------------------------------------

n = 3
is_weird = False if n > 20 else True

if n % 2 == 0:
    if 2 <= n <= 5:
        is_weird = False
    elif 6 <= n <= 20:
        is_weird = True
else:
    is_weird = True

print(["Not Weird", "Weird"][is_weird])
