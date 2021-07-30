# print multiply table of a given number entered by the user.
# Made with ❤️ in Python 3 by Alvison Hunter - March 30th, 2021
# Find more JavaScript & Python Tips at: https://bit.ly/3p9hpqj
def multiplication_table():
    while True:
        try:
            num = int(input("Please Enter a Positive Number: \n"))
            if num <= 0:
                print("Number must be Positive. Please try again.")
                pass
            else:
                print(f"--- TABLE OF {num} ----")
                [print(f"|  {str(num).ljust(2)} x {str(i).ljust(2)} = {str(num*i).ljust(5)} |") for i in range(1,13)]
                break
        except ValueError:
            print ("ValueError: This value should be a positive number.")
            pass
        except:
            print("Uh oh! Something went really wrong!. Please try again.")
            break

multiplication_table()



