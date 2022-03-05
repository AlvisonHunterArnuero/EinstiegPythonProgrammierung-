# -------------------------------------------------------------------------
# Introduction to list sorting, specific type list item extractions
# Made with ❤️ in Python 3 by Alvison Hunter -January 13th, 2022
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# -------------------------------------------------------------------------
import numbers
input = [5,'ac',3,'ab','1',2,'ad','6',4,'aa']

print(sorted([e for e in input if isinstance(e, numbers.Number)]))
# Should Output [2,3,4,5]

print(sorted([int(n) for n in input if str(n).isdigit()]))
# Should Output [1, 2, 3, 4, 5, 6]