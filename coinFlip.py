import random

def coin_flip():
    if random.randint(0, 1) == 1:
        return 'Head'
    else:
        return 'Tails'


def coin_flip_simulator():
    coin_dict = {'Head': 0, 'Tails': 0}
    player_name = input('What is your name? \n ')
    ask_player = input(f'{player_name}, Would you like to flip a coin? (Y/N): ').upper()
    while ask_player != 'N':
        flip = coin_flip()
        coin_dict[flip] += 1
        print(f"Current Score is: ==> {coin_dict}")
        ask_player = input(f'Would you like to flip again? ').upper()

    print(f'\nNo worries,{player_name}!, thank you so much for playing! \nYour total score was => {coin_dict}')

coin_flip_simulator()
