# ---------------------------------------------------------------------------------------------
# Description: Capture two different lists of names separated by commas and
# create a final list with these, in alphabetical order, with no repeated items.
# Author: Made with ❤️ in Python 3 by Alvison Hunter - June 14th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# Website: https://alvisonhunter.com/
# ---------------------------------------------------------------------------------------------
# Get list of names, split them and assign them in list variables
lst1 = input("Please Enter First List of Names:").split(",")
lst2 = input("Please Enter Second List of Names:").split(",")

# Extend lst1 by adding all the content of lst2 on it using extend(
lst1.extend(lst2)

# Create a set object, to store a list of non repeated elements
this_set = set()

# Let's iterate on lst1 to add all of its element to this_set set.
# Clearing any extra spaces, and convert these elements to title() case.
for elem in lst1:
    this_set.add(elem.strip().title())

# Print the results in a string, shall we?
print(' | '.join(sorted(list(this_set))))








