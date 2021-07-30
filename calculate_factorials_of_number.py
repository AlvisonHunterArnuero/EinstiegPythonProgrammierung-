# -------------------------------------------------------------------------
# Basic operations with colletion types | Python exercises | Beginner level
# Calculate the factorial of n Number entered by  user using a for loop.
# Made with ❤️ in Python 3 by Alvison Hunter Arnuero - May 29th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# -------------------------------------------------------------------------

import math

prev = 1
num = int(input("Enter a number: "))
# Using a for loop to make this calculation
for el in range(1, num+1):
    prev *= el
print(f"The factorial of {num} using for loop is : {prev}")

# Using the math factorial method to calculate this
print(
    f"The factorial of {num} using math.factorial is : {math.factorial(int(num))}")
