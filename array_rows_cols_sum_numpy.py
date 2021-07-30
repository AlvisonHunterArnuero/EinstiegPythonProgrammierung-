# ---------------------------------------------------------------------------------------------
# Sum rows and columns of a numpy array generated from a given list
# Made with ❤️ in Python 3 by Alvison Hunter - May 10th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# ---------------------------------------------------------------------------------------------
import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,13,14,15,16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,28,29,30]
tmp_lst = []
[tmp_lst.append(int(input("Enter a number: "))) for i in range(30)]

arr = np.array(tmp_lst)

newarr = arr.reshape(5, 6)
cols_lst = newarr.sum(axis=0)
rows_lst = newarr.sum(axis=1)

print(f"Columns Total: {cols_lst}")
print(f"Rows Total: {rows_lst}")
