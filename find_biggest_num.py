# --------------------------------------------------------------------------------
# Routine to Find index of the last of the biggest number in a list
# Made with ❤️ in Python 3 by Alvison Hunter - March 4th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# --------------------------------------------------------------------------------
prices = [1,2,3,1,5,1,3,5]
max_num = max(prices)
max_num_index = 0
print(f"Initial Max Number: {max_num}")
for index, value in enumerate(prices):
    print(f"Index {index} | Value {value}")
    if value>= max_num:
        max_num = value
        max_num_index = index
        print(f"Max number is {max_num} positioned at index {index}")

print(f"Final Max Number is: {max_num} in the {max_num_index} index")


