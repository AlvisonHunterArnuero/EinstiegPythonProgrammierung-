#The classic Rocks, Scissors Paper Game brought to life with Python
# Made with ❤️ in Python 3 by Alvison Hunter - November 27th, 2020

from random import randint
items_list = ['rock','paper','scissors']

def play():
    exit_flag = False
    print("Welcome to the ~ Rock Paper Scissors Game ~)")
    print("I assume you know how to play, so lets begin. You are playing against the computer.")
    comp_wins = 0
    user_wins = 0
    while(exit_flag != True):
        print(f'Current Score: You: {user_wins} - Computer: {comp_wins}')
        user_selection = 0
        comp_selection = int(randint(0,2))
        user_selection = input('Type 0 for rock, 1 for paper, and 2 for scissors\n')
        print("Computer has selected ",items_list[comp_selection])
        if(user_selection ==""):
            print('You have decided to end this game. Good bye for now.')
            exit_flag = True
        elif(int(user_selection)>2):
            print('You have entered an invalid value. Game Terminated.')
            exit_flag = True

        elif(int(user_selection) == comp_selection):
            print('None of the players won. Please try again.')
        # If one player chooses rock and the other player chooses scissors, then rock wins.
        elif(int(user_selection) == 0 and comp_selection==2):
            print('You won! Rock smashes scissors')
            user_wins += 1
        # If one player chooses scissors and the other player chooses paper,
        # then scissors wins.
        elif(int(user_selection) == 2 and comp_selection==1):
            print('You won! Scissors cut paper')
            user_wins += 1
        # If one player chooses paper and the other player chooses rock,
        # then paper wins.
        elif(int(user_selection) == 1 and comp_selection==0):
            print('You won! Paper wraps rock')
            user_wins += 1
        else:
            print(f'Computer wins with {items_list[comp_selection]} against {items_list[int(user_selection)]}')
            comp_wins += 1

    print(f'Final Score: \nYou: {user_wins} \nComputer: {comp_wins}')
    if(user_wins > comp_wins):
        print(f'CONGRATULATIONS, YOU HAVE WON {user_wins} - {comp_wins}!')
    elif(user_wins < comp_wins):
        print('COMPUTER WON!')
    else:
        print("Dead heat: None of you guys won!")


play()

