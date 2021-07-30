# --------------------------------------------------------------------------------
# Get the breakdwon sum of an integer number, calculate sum and print it afterwards.
# Made with ❤️ in Python 3 by Alvison Hunter - July 5th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# --------------------------------------------------------------------------------
num = input("Enter Number: ")
num_lst = list(num)
str_breakdown = num_lst[0]
for elem in range(1, len(num_lst)):
    str_breakdown += "+" + num_lst[elem]

print(f"Breakdown for {str_breakdown} is: {sum([int(el) for el in num_lst])}")
