# Made with ❤️ in Python 3 by Alvison Hunter - January 20th, 2020
largest = None
smallest = None
msg01 = "Please type in several numbers and we will  find the smallest & largest number entered."
msg02 ="NOTE: If you wish to end this program, please type in the letter 'x'."
print(f'{msg01}\n{msg02}')
while True:
    try:
        num = input("Enter a number:  ")
        if num.upper() == "X" : break

        num = int(num)

        if largest is None:
            largest = num
        elif num > largest:
                largest = num

        if smallest is None:
                    smallest = num
        elif num < smallest:
                    smallest = num
    except ValueError:
        print(f"Invalid input! Please type in the numbers again.")
        continue
    except:
        print ("Uh Oh! An unexpected error has occurred. We are exiting this program.")
        quit

if (smallest == largest):
    print("You only typed in the exact same number!")
    quit
else:
    print("=========== Final Results =========")
    print(f"Largest Number is => {largest}")
    print(f"Smallest Number is => {smallest}")
    print("===================================")
