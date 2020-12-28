# Made with ❤️ in Python 3 by Alvison Hunter - December 28th, 2020
import re
pattern = r"00"
lst_numbers = ["0014665611","001563354","140006256"]
for str in lst_numbers:
    match = re.search("\A00", str)
    if match:
        newstr = re.sub(pattern, "+", str)
        print(newstr)
    else:
        print(str)
