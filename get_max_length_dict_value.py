# -------------------------------------------------------------------------
# Routine to Find the value with maximum length stored in a dictionary
# Made with ❤️ in Python 3 by Alvison Hunter - March 2nd, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# -------------------------------------------------------------------------
positions_lst = ['first','second','third']
phrases_dict = {}

# Collect the phrases using commas as separators, this is very important
phrases_list = list(input("Enter 3 phrases separated by commas: ").split(","))

# Reduce the list to 3 elements if the user types in more than that.
if len(phrases_list) > 3:
    phrases_list = phrases_list[:3]

# Destructuring to make use of these variables individually.
first,second,third = phrases_list

# Display in the screen the values of these variables
print(f"First: {first}, Second: {second}, Third: {third}")

# let's iterate over these values to create a dict based on them
for key, value in enumerate(phrases_list):
    phrases_dict[positions_lst[key]] = len(value.strip())

print(f"New Information: {phrases_dict}")

# Find the max value on this dictionary
max_key = max(phrases_dict, key=phrases_dict.get)

# We will use this index to retrieve the longest phrase
current_index = positions_lst.index(max_key)

# All set, let us display all of these details on the screen now.
print(f"Longest Value: {max_key} | Length: {phrases_dict.get(max_key)} | Phrase: {phrases_list[current_index]}")
