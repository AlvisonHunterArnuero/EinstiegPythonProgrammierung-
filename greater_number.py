# -------------------------------------------------------------------------
# Find the greater number among two numbers given by a user
# Made with ❤️ in Python 3 by Alvison Hunter - January 14th, 2022
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# -------------------------------------------------------------------------

def find_greater_number():
    while True:
        num = int(input("Please enter a number: "))
        if(num==3):
            print("Please try again!")
            continue
        else:
            print("My number is Bigger" if(num<3) else "Your Number is Bigger")
        break

find_greater_number()