# ---------------------------------------------------------------------------
# Write a Python program that allows n people to enter a survey. The possible
# answers to it would be A, B & C. If another key is pressed the program does
# nothing. If user presses X the program ends. Print the winner if there's one.
# ---------------------------------------------------------------------------
# Made with ❤️ in Python 3 by Alvison Hunter - June 15th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# --------------------------------------------------------------------------------
import random

# Declare several types of correct answers
congrats_responses_lst = [
    "Contratulations, pal! You are the winner!!! [🥳]",
    "Well done! This is one of the correct answers. [🤗]",
    "Way to go! Your answer is in fact correct!! [🤩]"]

# Declare several types of wrong answers
sad_responses_lst = ["Yikes! That's totally incorrect!! [😔]",
                     "Uh oh! Wrong answer, folk! [😭]",
                     "Oops-a-daisy! That's not correct either! [😢]"]

# Declare winning options in a tuple
winning_tpl = ("A", "B", "C")

# Decorate the title between two lines as screen dividers
print("-"*50)
print("WELCOME TO THE GUESS MY SILLY POLL ANSWER GAME.")
print("-"*50)

# while loop to capture as many responses as possible
# until the user types the correct or the exit one
while True:
    usr_inpt = input("Please Enter your vote: \n")

    # if the response is in the tuple, then it is a winner!
    if usr_inpt.upper() in winning_tpl:
        # print the message and leave the program afterwards
        print(f"{random.choice(congrats_responses_lst)}")
        break

    # if user presses X as input, we exit this program out
    elif(usr_inpt.upper() == "X"):
        break

    else:
        # use only pass if you don't want to display anything.
        # you could also skip this else statement if you wish.
        # Or use print to display a message with a sad face
        print(f"{random.choice(sad_responses_lst)}")

# Thanks the user for playing this game, shall we?
print("Thank you for playing this game! Bye 👋")
