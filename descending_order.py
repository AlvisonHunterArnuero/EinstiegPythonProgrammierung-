# --------------------------------------------------------------------------------
# Your task is to make a function that can take any non-negative integer as an
# argument and return it with all of its digits in descending order.
# Essentially, rearrange the digits to create the highest possible number.
# Made with ❤️ in Python 3 by Alvison Hunter - March 3rd, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# --------------------------------------------------------------------------------
def descending_order(num):
    result = ""
    if (num < 1):
        print(num)
    else:
        num_lst = sorted([int(x) for x in str(num)], reverse=True)
        for el in num_lst:
            result += str(el)
        print(result)

# Test it with different escenarios
descending_order(0) # 0
descending_order(42145) # 54421
descending_order(145263) # 654321
descending_order(123456789) # 987654321
descending_order(15) # 51
descending_order(123456789) # 987654321
