# --------------------------------------------------------------------------------
# A simple Phone Number formatter routine for nicaraguan area codes
# Made with ❤️ in Python 3 by Alvison Hunter - April 4th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# --------------------------------------------------------------------------------
def format_phone_number(ind, lst_numb):
    # Create a whole string with the elements of the given list
    lst_to_str_num = ''.join(str(el) for el in lst_numb)

    # Format the string we just built with the appropiate characters
    fmt_numb = f"{ind+1} - ({''.join(lst_to_str_num[:3])}) {''.join(lst_to_str_num[3:7])}-{''.join(lst_to_str_num[7:11])}"
    # print a line as a divider
    print("-"*20)
    # print the formatted string
    print(fmt_numb)


#  list of lists to make these formatting as our driver's code
phone_lst = [
    [5, 0, 5, 8, 8, 6, 3, 8, 7, 5, 1],
    [5, 0, 5, 8, 1, 0, 1, 3, 2, 3, 4],
    [5, 0, 5, 8, 3, 7, 6, 1, 7, 2, 9],
    [5, 0, 5, 8, 5, 4, 7, 2, 7, 1, 6]
]

# List comprehension now to iterate the list of lists
# and to apply the function to each of the list elements
[format_phone_number(i, el) for i, el in enumerate(phone_lst)]
print("-"*20)
