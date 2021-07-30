# ---------------------------------------------------------------------------------------------
# Find all ASCII code from string characters, add them, change 7 for 1, substract both amount
# and return is final result
# Made with ❤️ in Python 3 by Alvison Hunter - March 30th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# ---------------------------------------------------------------------------------------------
def calc(x):
    total1 ="".join(str(ord(elem)) for elem in x)
    total2 =total1.replace('7','1')
    print(sum(int(num) for num in total1) - sum(int(num2) for num2 in total2))
    return sum(int(num) for num in total1) - sum(int(num2) for num2 in total2)

calc('ABC')
calc('abcdef')
calc('ifkhchlhfd')
calc('aaaaaddddr')
calc('jfmgklf8hglbe')
calc('jaam')
