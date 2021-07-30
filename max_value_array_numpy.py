# ---------------------------------------------------------------------------------------------
# Find Maximum value of an array created in numpy based on a list. we will use max from numpy
# Made with ❤️ in Python 3 by Alvison Hunter - May 1st, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# ---------------------------------------------------------------------------------------------
import numpy as np
tmp_lst = []
[tmp_lst.append(int(input("Enter a number: "))) for i in range(6)]
print('Max value is: ', np.max(np.array(tmp_lst)))
