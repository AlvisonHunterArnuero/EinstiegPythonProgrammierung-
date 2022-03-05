# -------------------------------------------------------------------------
# Write a program to print following pattern. if input is 5, output is:
# 5
# 4 5
# 3 4 5
# 2 3 4 5
# 1 2 3 4 5
# Made with ❤️ in Python 3 by Alvison Hunter - March 5th, 2022
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# -------------------------------------------------------------------------
usr_npt = int(input("Enter Number: "))
frt_lst = [str(elem) for elem in range(usr_npt,0,-1)]
[print(' '.join(frt_lst[:int(e)+1])[::-1]) for e in range(usr_npt)]

