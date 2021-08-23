# --------------------------------------------------------------------------------
# Basic Scissors, Paper, Rocks Game to demonstrate use of conditional statement IF
# Made with ❤️ in Python 3 by Alvison Hunter - August 22nd, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# --------------------------------------------------------------------------------
import random as r

rules = {"scissor": "paper", "paper": "rock", "rock": "scissor"}
options_lst = ["rock", "scissor", "paper"]

while True:
    usr_choice = input("Play: Type rock, scissor or paper: ").lower()
    cmpt_choice = r.choice(options_lst)
    if usr_choice not in options_lst:
        print("You entered an invalid option. Please try again!")
        continue
    print(f"You: {usr_choice} | Computer: {cmpt_choice}")
    if usr_choice == cmpt_choice:
        print("It is a Tie!! Please Try again!")
        continue
    elif usr_choice in rules.keys() and cmpt_choice == rules[usr_choice]:
        print(f"You win! {usr_choice} beats {cmpt_choice}")
        break
    else:
        print(f"Computer Wins! {cmpt_choice} beats {usr_choice}")
        break