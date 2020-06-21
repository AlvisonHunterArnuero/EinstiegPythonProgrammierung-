#First, you only need the random function to get the results you need :)
import  random
#Let us start by getting the response from the user to begin
repeat = input('Would you like to roll the dice [y/n]?\n')

#As long as the user keeps saying yes, we will keep the loop
while repeat != 'n':
# How many dices does the user wants to roll, 2 ,3 ,4 ,5  who knows. let's ask!
    amount = int(input('How many dices would you like to roll? \n'))
# Now let's roll each of those dices and get their results printed on the screen
    for i in range(0, amount):
       diceValue = random.randint(1, 6)
       print(f"Dice {i+1} got a [{diceValue}] on this turn.")
#Now, let's confirm if the user still wants to continue playing.       
    repeat = input('\nWould you like to roll the dice [y/n]?\n')

# Now that the user quit the game, let' say thank you for playing
print('Thank you for playing this game, come back soon!')
# Happy Python Coding, buddy! I hope this answers your question.


