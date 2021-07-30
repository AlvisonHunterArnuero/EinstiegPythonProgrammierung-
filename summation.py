# -------------------------------------------------------------------------
# Write a program that finds the summation of every number from 1 to num.
# The number will always be a positive integer greater than 0.
# Made with ❤️ in Python 3 by Alvison Hunter - March 2nd, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# -------------------------------------------------------------------------
def summation(num):
    result = sum([i for i in range(1, num+1)])
    print(result)

summation(1) # 1
summation(8) # 36
summation(22) # 253
summation(100) # 5050
summation(213) # 22791
