# Author: Made with ♥ in Python 3 by Alvison Hunter - May 24th, 2021
# Description: grab 5 nums, create a dict with even nums divided by two
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj

def get_even_nums_from_input(nums_amount):
    str_tmp = ""
    even_lst = []
    results_dict = {}
    [even_lst.append(
        float(input(f'Enter digit #{i+1}: '))) for i in range(nums_amount)]
    for ind, el in enumerate(even_lst):
        if el % 2 == 0:
            str_key = "N"+str(ind+1)
            results_dict[str_key] = int((el)/2)

    print("Even Numbers divided by 2:")
    for k, v in results_dict.items():
        str_tmp += f"{k}[{v}], "
    print(str_tmp[:-1])


get_even_nums_from_input(5)
