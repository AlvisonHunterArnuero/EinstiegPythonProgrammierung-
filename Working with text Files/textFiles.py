# This function will generate a random string with a lenght based on user input number.
# This can be useful for temporary passwords or even for some temporary login tokens.
# The information is saved afterwards in a text file with the date and the username
# of the person who requested the creation of the new password.
# may you have questions of comments, reach out to me at alvison@gmail.com
import random
import time
from datetime import date
def main():
        today = date.today()
        print("░░░░░░░░░░░░░░░░ Password Generator Tool ░░░░░░░░░░░░░░░")
        username = input("Enter user name: ")
        numCharacters = int(input("Insert the desired number of characters: "))
        if numCharacters > 70:
            print ("The entered amount is too big, number has to be less than 70")
        else:
            baseString = list ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@*+&^%$#!")
            strResult = ""
            generated_list = random.sample(baseString, numCharacters)

        for character in generated_list:
                strResult += character

        print("Generating new password, please hold...")
        time.sleep(1)
        print("The new password is: {} created by {} on {}".format(strResult, username,today.strftime("%b-%d-%Y")))

        f=open("mypwdfile.txt", "a+")
        f.write("\nThe new password is: {} created by {} on {}".format(strResult, username,today.strftime("%b-%d-%Y")))
        f.close()
        print("Passwords were successfully updated on the mypwdfile.txt as well.".format(username))
        print("░░░░░░░░░░░░░░░░ Powered by Alvison Hunter ░░░░░░░░░░░░░░░")

if __name__== "__main__":
    main()
