# Made with ❤️ in Python 3 by Alvison Hunter - December 23rd, 2020
# Website: https://alvisonhunter.com/

def display_arrows():
    for elem in range(1,14):
        if (elem % 2) != 0:
            print(str('*'*elem).center(14,' '))

    # Lets paint the trunk of the tree now using an inline sentence
    [print('**********'.center(14,' ')) for i in range(3)]

# Let us call the function now and draw the arrows on the screen!
display_arrows()
