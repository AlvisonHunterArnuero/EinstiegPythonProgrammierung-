# This program will check if a given number is prime or not
# Made with ❤️ in Python 3 by Alvison Hunter - August 19th, 2020

# First, let's validate if what the user types is indeed a int number
try:
    num =int(input('Please enter a Number [Type 1 to exit]: \n'))
    while num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(f"{i} is not a prime number.")
                break
            else:
                print(f"{i} is a prime number.")

        num =int(input('Please enter a Number [0 to exit]: \n'))

    print("Thank you for using the Prime Number Calculator!")

except ValueError:
    print("That's not an integer number, fellow! Thank you for using this program!")
    num=1

