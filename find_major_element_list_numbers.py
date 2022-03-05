# -----------------------------------------------------------------------
# Python Tricks and tips for better coding -Basic Python coding
# Made with ❤️ in Python 3 by Alvison Hunter - November 21st, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# -----------------------------------------------------------------------

arr_Numbers = []
while True:
    try:
        num = int(input("Enter an INTEGER: "))
    except ValueError:
        print("You must enter an INTEGER, not any other format of data")
    else:
        if num == 0:
            break
        else:
            arr_Numbers.append(num)


print("Max Number is: ", max(arr_Numbers))