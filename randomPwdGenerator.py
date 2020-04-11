# This function will generate a random string with a lenght based on user input number.
# This can be useful for temporary passwords or even for some temporary login tokens.
import random
import time
def fnRandomString():
    print("░░░░░░░░░░░░░░░░ Password Generator Tool ░░░░░░░░░░░░░░░")
    numCharacters = int(input("Insert the desired number of characters: "))
    if numCharacters < 70:
        baseString = list ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@*+&^%$#!")
        strResult = "" 
        generated_list = random.sample(baseString, numCharacters) 
        for character in generated_list:  
          strResult += character
        print("Generating new password, please hold...")
        time.sleep(2)
        print("The new password is:\n {}".format(strResult))
    else:
        print ("The entered amount is too big, number has to be less than 70")
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
fnRandomString()
