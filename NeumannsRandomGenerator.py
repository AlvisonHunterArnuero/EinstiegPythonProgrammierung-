# Random numbers are often used in programming games and scientific researches, but also they could be useful even in
# business applications (to generate unique user keys, passwords etc.). Here is one of the earliest methods for producing
# sequence of seemingly independed (i.e. pseudorandom) numbers: I took this to create a Credit Card Random Number
#generator based on Neumann's Random Generator at http://www.codeabbey.com/index/task_view/neumanns-random-generator

import os
import time
import datetime
import random
clear = lambda: os.system('clear')

def main():
    clear()
    now = datetime.datetime.now()
    currYear = str(now.year+3)
    month = now.month
    numberList = [1,2,3,4,5,6,7,8,9,0]
    securitycode = ""
    title= "Neumann's Random Number Sequences Generator".upper()
    print(f"░░░░░  {title}  ░░░░░")
    name = input("Please type in your Name ").upper()
    firstsequence= int(input("Please type your 4-digits number: "))
    if len(str(firstsequence)) >= 4:
        tmp =(firstsequence*firstsequence)
        print("Generating first value... ",tmp)
        tmp2 = str(tmp)
        time.sleep(0.05)
        secondsequence = int(tmp2[2:-2])
        tmp =(secondsequence*secondsequence)
        print("Generating second value...",tmp)
        tmp2 = str(tmp)
        time.sleep(0.05)
        print("Generating third value... ",tmp2)
        thirdsequence = int(tmp2[1:-2])
        tmp =(thirdsequence*thirdsequence)
        print(" Generating Fourth value...",tmp)
        tmp2 = str(tmp)
        fourthsequence = int(tmp2[2:-2])
        print("Generating security code... ")
        for x in range(4):
            securitycode = securitycode + str(random.choice(numberList))
        print("Finalizing card's details")
        for n in range(6):
            print("»"*n, end ="")
            time.sleep(0.05)

        print("",end="\n")
        print("═"*30)
        print(f"NEW CARD NUMBER: \t{firstsequence} - {secondsequence} - {thirdsequence} - {fourthsequence}")
        print(f"SECURITY CODE: {securitycode}  EXPIRES ON: {month}/{currYear[2:]}")
        print(f"CARD HOLDER: {name}")
        print("═"*30)
        print("\n Made with ❤️ in Python 3 by Alvison Hunter - August 8th, 2020")
    else:
        return print(f"We are unable to continue with this process. {firstsequence} is an invalid 4-digits number[E.g. 2345].")
    print("\nPlease verify your number and try again later. Thanks!")

if __name__ == "__main__":
    main()

