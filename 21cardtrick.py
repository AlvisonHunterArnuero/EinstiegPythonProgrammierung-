import itertools, random
import time
import sys
n = (0)
shuffledcards=[]
#Shuffling a deck of 52 cards
cards =list(itertools.product(range(1,14),['spade','heart','diamond','club']))
random.shuffle(cards)

print("Pick a card from:")
#Picking the first 21 cards
for i in range(21):
  card=(cards[i][0], "of", cards[i][1])
  shuffledcards.append(card)
print(shuffledcards)

print("Now i will split the cards into three equal piles.")
time.sleep (1)

#Splitting the 21 cards into three piles of 7
pile_one =[(shuffledcards[0]),(shuffledcards[3]),(shuffledcards[6]),(shuffledcards[9]),(shuffledcards[12]),(shuffledcards[15]),(shuffledcards[18])]
pile_two =[(shuffledcards[1]),(shuffledcards[4]),(shuffledcards[7]),(shuffledcards[10]),(shuffledcards[13]),(shuffledcards[16]),(shuffledcards[19])]
pile_three =[(shuffledcards[2]),(shuffledcards[5]),(shuffledcards[8]),(shuffledcards[11]),(shuffledcards[14]),(shuffledcards[17]),(shuffledcards[20])]

print("PILE ONE")
print(pile_one)
print("PILE TWO")
print(pile_two)
print("PILE THREE")
print(pile_three)

del shuffledcards
shuffledcards=[]

#The pile they state gets placed inbetween the other two in the main arrays
col=int(input("Which pile is your card in? 1, 2 or 3"))
if col == 1:
  for i in range(7):
    shuffledcards.append(pile_two[(n)])
    n=n+1
  n=0
  for i in range(7):
    shuffledcards.append(pile_one[(n)])
    n=n+1
  n=0
  for i in range(7):
    shuffledcards.append(pile_three[(n)])
    n=n+1
  n=0
  
if col == 2:
  for i in range(7):
    shuffledcards.append(pile_one[(n)])
    n=n+1
  n=0
  for i in range(7):
    shuffledcards.append(pile_two[(n)])
    n=n+1
  n=0
  
  for i in range(7):
    shuffledcards.append(pile_three[(n)])
    n=n+1
  n=0 
  
if col == 3:
  for i in range(7):
    shuffledcards.append(pile_one[(n)])
    n=n+1
  
  n=0
  for i in range(7):
    shuffledcards.append(pile_three[(n)])
    n=n+1
  n=0
  for i in range(7):
    shuffledcards.append(pile_two[(n)])
if col != 1:
  if col != 2:
    if col != 3:
      print("Please restart and enter a recognised response")
      sys.exit(1)
  
  
#splitting the cards into 3 piles again
pile_one =[(shuffledcards[0]),(shuffledcards[3]),(shuffledcards[6]),(shuffledcards[9]),(shuffledcards[12]),(shuffledcards[15]),(shuffledcards[18])]
pile_two =[(shuffledcards[1]),(shuffledcards[4]),(shuffledcards[7]),(shuffledcards[10]),(shuffledcards[13]),(shuffledcards[16]),(shuffledcards[19])]
pile_three =[(shuffledcards[2]),(shuffledcards[5]),(shuffledcards[8]),(shuffledcards[11]),(shuffledcards[14]),(shuffledcards[17]),(shuffledcards[20])]

print("The piles are being changed")
time.sleep(2)

print("PILE ONE")
print(pile_one)
print("PILE TWO")
print(pile_two)
print("PILE THREE")
print(pile_three)

del shuffledcards
shuffledcards=[]

col=int(input("Which pile is your card in? 1, 2 or 3"))
if col == 1:
  for i in range(7):
    shuffledcards.append(pile_two[(n)])
    n=n+1
  n=0
  for i in range(7):
    shuffledcards.append(pile_one[(n)])
    n=n+1
  n=0
  for i in range(7):
    shuffledcards.append(pile_three[(n)])
    n=n+1
  n=0
  
if col == 2:
  for i in range(7):
    shuffledcards.append(pile_one[(n)])
    n=n+1
  n=0
  for i in range(7):
    shuffledcards.append(pile_two[(n)])
    n=n+1
  n=0
  for i in range(7):
    shuffledcards.append(pile_three[(n)])
    n=n+1
  n=0 
  
if col == 3:
  for i in range(7):
    shuffledcards.append(pile_one[(n)])
    n=n+1
  n=0
  for i in range(7):
    shuffledcards.append(pile_three[(n)])
    n=n+1
  n=0
  for i in range(7):
    shuffledcards.append(pile_two[(n)])
    n=n+1
if col != 1:
  if col != 2:
    if col != 3:
      print("Please restart and enter a recognised response")
      sys.exit(1)
  
pile_one =[(shuffledcards[0]),(shuffledcards[3]),(shuffledcards[6]),(shuffledcards[9]),(shuffledcards[12]),(shuffledcards[15]),(shuffledcards[18])]
pile_two =[(shuffledcards[1]),(shuffledcards[4]),(shuffledcards[7]),(shuffledcards[10]),(shuffledcards[13]),(shuffledcards[16]),(shuffledcards[19])]
pile_three =[(shuffledcards[2]),(shuffledcards[5]),(shuffledcards[8]),(shuffledcards[11]),(shuffledcards[14]),(shuffledcards[17]),(shuffledcards[20])]

print("The piles are being changed")
time.sleep(2)

print("PILE ONE")
print(pile_one)
print("PILE TWO")
print(pile_two)
print("PILE THREE")
print(pile_three)

del shuffledcards
shuffledcards=[]

col=int(input("Which pile is your card in? 1, 2 or 3"))
if col == 1:
  for i in range(7):
    shuffledcards.append(pile_two[(n)])
    n=n+1
  n=0
  for i in range(7):
    shuffledcards.append(pile_one[(n)])
    n=n+1
  n=0
  for i in range(7):
    shuffledcards.append(pile_three[(n)])
  n=0
  
if col == 2:
  for i in range(7):
    shuffledcards.append(pile_one[(n)])
    n=n+1
  n=0
  for i in range(7):
    shuffledcards.append(pile_two[(n)])
    n=n+1
  n=0
  for i in range(7):
    shuffledcards.append(pile_three[(n)])
  n=0 
  
if col == 3:
  for i in range(7):
    shuffledcards.append(pile_one[(n)])
    n=n+1
  n=0
  for i in range(7):
    shuffledcards.append(pile_three[(n)])
    n=n+1
  n=0
  for i in range(7):
    shuffledcards.append(pile_two[(n)])
if col != 1:
  if col != 2:
    if col != 3:
      print("Please restart and enter a recognised response")
      sys.exit(1)
  
print("Let me think")
time.sleep(2)
print("Your card is")
time.sleep(1)
print(shuffledcards[10])
