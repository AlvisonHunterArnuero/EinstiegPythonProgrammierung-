#The classic Rocks, Scissors Paper Game brought to life with Python
# Made with ❤️ in Python 3 by Alvison Hunter - December 10th, 2020

import random
items_list = ['r', 'p', 's']

def play():
    exit_flag = False
    print("Welcome to the ~ Rock Paper Scissors Game ~)")
    print("I assume you know how to play, so let's begin.")
    print("You are playing against the computer.")
    comp_wins = 0
    user_wins = 0
    while(exit_flag != True):
        print(f'Current Score: You: {user_wins} - Computer: {comp_wins}')
        user_selection = 0
        comp_selection = random.choice(items_list)
        user_selection = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
        print("Computer has selected ", comp_selection)
        if(user_selection not in items_list or user_selection ==""):
            print('You have entered an invalid or empty value. Game Terminated.')
            exit_flag = True
        elif(user_selection == comp_selection):
            print('None of the players won. Please try again.')
        # If one player chooses rock and the other player chooses scissors, then rock wins.
        elif(user_selection == 'r' and comp_selection=='s'):
            print('You won! Rock smashes scissors')
            user_wins += 1
        # If one player chooses scissors and the other player chooses paper,
        # then scissors wins.
        elif(user_selection == 's' and comp_selection=='p'):
            print('You won! Scissors cut paper')
            user_wins += 1
        # If one player chooses paper and the other player chooses rock,
        # then paper wins.
        elif(user_selection == 'p' and comp_selection=='r'):
            print('You won! Paper wraps rock')
            user_wins += 1
        else:
            print(f'Computer wins with {comp_selection} against {user_selection}')
            comp_wins += 1

    print('='*60)
    print(f'Final Score: \nYou: {user_wins} \nComputer: {comp_wins}')
    if(user_wins > comp_wins):
        print(f'CONGRATULATIONS, YOU HAVE WON {user_wins} - {comp_wins}!')
    elif(user_wins < comp_wins):
        print('COMPUTER WON!')
    else:
        print("Dead heat: None of you guys won!")


play()

