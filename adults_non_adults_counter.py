# -------------------------------------------------------------------------
# Basic operations with colletion types | Python exercises | Beginner level
# Based on user input, calculate how many adults & non adults were entered
# Made with ❤️ in Python 3 by Alvison Hunter Arnuero - April 16th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# -------------------------------------------------------------------------
def msg_box(msg="", chr_type="-", reps=25):
    print(chr_type*reps)
    print(msg)
    print(chr_type*reps)


def calculate_adulthood():
    adults, non_adults = 0, 0
    msg_box("Welcome to the Magic Adulthood Calculator", "-", 45)
    print("To exit this routine, please press 0 - zero")
    while True:
        try:
            edad = int(input("Enter Age: "))
            if (edad == None or edad == 0):
                msg_box(f"Adults: {adults} Non-Adults: {non_adults}", "-", 25)
                break

            adulthood = True if edad > 18 else False
            if(adulthood):
                adults += 1
            else:
                non_adults += 1

        except ValueError:
            print("Age should be a number! Please try again.")
            continue


calculate_adulthood()
