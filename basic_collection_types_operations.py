# -------------------------------------------------------------------------
# Basic operations with colletion types | Python exercises | Beginner level
# Calculate sum & average of 5 given numbers entered by the user in a loop.
# Made with ❤️ in Python 3 by Alvison Hunter Arnuero - April 8th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# -------------------------------------------------------------------------
import statistics as st
# Empty list to capture all of the user entered values
num_lst = []

# While we have not yet calculate the whole enchilada or
# we find some value errors or non numeric inputs, carry on
while True:

    # Error handler comes to  the rescue for basic cases
    try:
        # list comprehension to add this captures to the declared list
        [num_lst.append(float(input("Please enter number: \n")))
         for n in range(5)]

    # Exception handling
    except ValueError:
        print(f"ValueError: could not convert string to float: Starting to collect info again...")
        continue
    except:
        print("Uh Oh: An unexpected error has ocurred. Shuting down this app...")
        break
    else:
        print("-"*25)
        # let's print two methods of resolving this scenario
        print(f"TOTAL: {sum(num_lst)}")

        # Regular way of calculating average without modules
        avg = sum(num_lst) / len(num_lst)
        print("-"*25)
        print(f"AVERAGE: {avg}")

        # or simply using a built in module, to make it easier
        print("-"*25)
        print(f"MEAN: {st.mean(num_lst)}")
        break
