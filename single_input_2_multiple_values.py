# -----------------------------------------------------------------------
# How to convert a single input value into multiple values within a list
# Made with ❤️ in Python 3 by Alvison Hunter - February 28th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# -----------------------------------------------------------------------
def register_students():
    students_list =  []
    list_element = ""
    try:
        iter = int(input("Please Enter amount of Students to register: "))
        print("Enter Name, Age, Weight, Height separated by commas: Ex. Clark,35,230,190")
        for n in range(iter):
            students_list.append(list(input().split(",")))
    except ValueError:
        print("Oopsie! That was not a valid number.  Please Try again later.")
    finally:
        print("-"*50)
        print('The list now contains the following elements:')
        print("-"*50)
        for el in students_list:
            print(el)

register_students()
