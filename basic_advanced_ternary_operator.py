#----------------------------------------------------------------------------
# Basic and advanced conditional using ternary operators to print strings
# Made with ❤️ in Python 3 by Alvison Hunter Arnuero - February 1st, 2022
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
#----------------------------------------------------------------------------

name = "ALVISON HUNTER"

# First Approach
print(f"HELLO {name}" if name.isupper() else f"Hey {name}")

#Second Approach
print((f"Hey {name}",f"HELLO {name}")[True if name.isupper() else False])