# --------------------------------------------------------------------------------
# Find Emerald bird finding horizontal, vertical or lateral sequences of 4 characters.
# Made with ❤️ in Python 3 by Alvison Hunter - March 19th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# --------------------------------------------------------------------------------
from collections import Counter
horizontal_list = ["ABDCDA","ADBDAA","AACBCD","ADAABC","BADDCD","ADDAAA"]
lateral_list = []
vertical_list = []

# Fill lateral list
for ind, elem in enumerate(horizontal_list):
    lateral_list.append(elem[ind])
print("LAT: ", lateral_list)

# Fill the vertical list
for ind, elem in enumerate(horizontal_list):
    vertical_list.append(elem[ind])
print("VERT: ", vertical_list)

# Find Sequences
for el in DNA:
    counter = Counter(el)
    for i in el:
        if(counter[i]>3):
            print(f"{i*4}")
            break
        else:
            pass
