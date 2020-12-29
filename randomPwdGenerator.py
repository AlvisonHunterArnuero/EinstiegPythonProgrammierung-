# This function will generate a random string with a lenght based
# on user input number. This can be useful for temporary passwords
# or even for some temporary login tokens.
# Made with ❤️ in Python 3 by Alvison Hunter - December 28th, 2020
from random import sample
import time
from datetime import datetime
# We will incorporate some colors to the terminal
class bcolors:
    PRIMARY ='\033[34m'
    SECONDARY = '\033[95m'
    FOOTER = '\033[37m'
    INFO = '\033[36m'
    SUCCESS = '\033[32m'
    WARNING = '\033[93m'
    DANGER = '\033[31m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Main function is defined here
def generate_rand_pwd():
    try:
        print("░░░░░░░░░░░░░ Hunter Password Generator Tool ░░░░░░░")
        print("============= We do not store any passwords. =======")
        numCharacters = int(input("Please Enter Password Length: \n"))
        if numCharacters < 70:
            baseString = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@*+&^%$#!"
            strResult = ''.join(sample(baseString, numCharacters))
            print(f"{bcolors.WARNING}Generating new password, please hold...{bcolors.ENDC}")
            time.sleep(1)
            print(f"{bcolors.INFO}The new password is:{bcolors.ENDC}\n {bcolors.SUCCESS}{strResult}{bcolors.ENDC}")
        else:
            print ("The password length is too big, number has to be less than 70")
            return
    except:
        print('Uh Oh, something went wrong!')
    finally:
        print(f"{bcolors.FOOTER}© {datetime.today().strftime('%Y-%m-%d')} Hunter Password Generator Tool. All rights reserved.{bcolors.ENDC}")


# Time to call the function now, fellows
generate_rand_pwd()
