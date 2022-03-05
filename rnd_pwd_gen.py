#----------------------------------------------------------------------------
# Generate a Random Password based on the length requested by the user
# Made with ❤️ in Python 3 by Alvison Hunter Arnuero - January 26th, 2022
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
#----------------------------------------------------------------------------
import random as r, string as s
pwd_len = int(input("Enter Password Length: "))
print("New Password: ",''.join(r.sample(s.printable[:-7],pwd_len)))