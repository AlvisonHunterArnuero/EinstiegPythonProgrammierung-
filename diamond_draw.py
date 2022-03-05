# -----------------------------------------------------------------------
# Python Tricks and tips for better coding -Basic Python coding
# Made with ❤️ in Python 3 by Alvison Hunter - November 23th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# -----------------------------------------------------------------------
  
print('\n')
final_str = ' '
print("*".center(14," "))
for i in range(2,12):
    if(i%2!=0):
        print(f"*{final_str}*".center(14," "))
        final_str = ' '*i

for e in range(9,-1,-1):
    if(e%2!=0):
        print(f"*{final_str}*".center(14," "))
        final_str =" "*e
print("*".center(14," "))

        

