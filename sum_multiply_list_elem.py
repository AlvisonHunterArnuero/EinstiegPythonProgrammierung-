# -----------------------------------------------------------------------------------------
# Get 5 numbers from user input, add them to a list & calculate addition & multiplication
# -----------------------------------------------------------------------------------------
# Made with ❤️ in Python 3 by Alvison Hunter - March 26th, 2021
# For JavaScript, Python & Web Development tips, visit our channel: https://bit.ly/3p9hpqj
# -----------------------------------------------------------------------------------------
import math

# List to store the entered numbers, variables to store results
num_lst = []
num = 0
total = 0
product = 0

# Try... except block to handle errors
try:
    for n in range(5):
        if n == 2 or n == 4:
            num = float(input("Please Enter decimal number: \n"))
            num_lst.append(num)
        else:
            num = int(input("Please Enter integer number: \n"))
            num_lst.append(num)

    # Calculations of the sum & multiplication of the list elements
    total = sum(num_lst)
    product = math.prod(num_lst)

    # Display results now in a whole sentence, shall we?
    results = f"Total: {total:.2f} | Product: {product}"

    print("-"*len(results)) # to draw a divider in the screen
    print(results)
    print("-"*len(results)) # to draw a divider in the screen

# Exceptions handling when user enters wrong input type
except ValueError as ve:
    print("Oh no!:Only numbers are allowed! Please try again later.")
    quit
# This exception works for any non declared error
except:
    print("Uh oh! Something went really wrong!. Please try again later.")
    quit
