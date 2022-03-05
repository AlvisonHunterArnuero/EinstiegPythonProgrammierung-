# -------------------------------------------------------------------------
# Basic Example of the use of list comprehension to reduce code lines,
# Made with ❤️ in Python 3 by Alvison Hunter - January 24th, 2022
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# -------------------------------------------------------------------------
num_lst = [9,3,4,6,7,1,8]

[print(f"Par: {num}" if(num % 2) == 0 else f"Impar: {num}") for num in num_lst]

# Regular way of doing this
for num in num_lst:
    if(num % 2) == 0:
        print(f"Even: {num}")
    else:
        print(f"Odd: {num}")
