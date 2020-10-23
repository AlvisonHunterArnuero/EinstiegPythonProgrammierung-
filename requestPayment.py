from random import randrange
list1 = ['nanito', 'chinito', 'morenito','billicito', 'alicito']
def requestPayment() -> str:
    chosen_one =  list1[randrange(4)]
    if(chosen_one=='billicito'):
        print('This person has already taken a turn')
        quit
    else:
        print ('It is your turn now,  ',chosen_one)
        return  chosen_one

requestPayment()
