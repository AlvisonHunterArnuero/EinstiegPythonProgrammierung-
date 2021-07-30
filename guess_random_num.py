# -------------------------------------------------------------------------
# Basic operations with Python 3 | Python exercises | Beginner level
# Generate a random number, request user to guess the number
# Made with ❤️ in Python 3 by Alvison Hunter Arnuero - June 4th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# -------------------------------------------------------------------------
import random
attempts = 0
rnd_num = random.randint(1, 10)
player = input("Please Enter Your Name: ")
while True:
    attempts += 1
    num = int(input("Enter the number: \n"))
    print(f"Attempts: {attempts}")
    if (num == rnd_num):
        print(
            f"Well done {player}, you won! {rnd_num} was the correct number!")
        print(
            f" You got this in {attempts} Attempts.")
        break
    else:
        pass
print("End of Game")
