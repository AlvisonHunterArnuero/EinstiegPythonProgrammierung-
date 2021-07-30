# ---------------------------------------------------------------------------------------------
# Get 10 numbers, find out if they are all positive, minor or equal to 99 & if 99 was typed.
# Made with ❤️ in Python 3 by Alvison Hunter - May 17th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# ---------------------------------------------------------------------------------------------
cardinals = [
    "First",
    "Second",
    "Third",
    "Fourth",
    "Fifth",
    "Sixth",
    "Seventh",
    "Eighth",
    "Ninth",
    "Tenth",
]
tmp_lst = []
print("Enter 10 positive numbers: \n")
[tmp_lst.append(int(input(f"Enter {cardinals[i]} Number: ")))
 for i in range(10)]
[
    print(f"{el} is positive.") if (el >= 0) else print(f"{el} is negative.")
    for el in tmp_lst
]
[
    print("Positive number 99 was typed.")
    if (any(e == 99 for e in tmp_lst))
    else print("Positive number 99 was NOT typed.")
]
