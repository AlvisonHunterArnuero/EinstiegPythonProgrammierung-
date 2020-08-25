#3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error.
# If the score is between 0.0 and 1.0, print a grade using the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#If the user enters a value out of range, print a suitable error message and exit.
#For the test, enter a score of 0.85. This should return B afterwards.

#Made with ❤️ in Python 3 by Alvison Hunter - August 20th, 2020
def main():
    val = input("Enter Score: \n")
    try:
        score=int(val)
        if int(val) and int(val)>1:
            print(score,"Is an integer number greater than 1! Score range should be between 0.0 and 1.0.")
            print('Please try again with a number within the given range. Good bye!')
        exit
    except ValueError:
        try:
            score = float(val)
            print("Your Final Score Grade is: ")
            if score >=0.9 and score <=1.0:
                print("A")
            elif score >=0.8 and score <0.9:
                print("B")
            elif score >=0.7 and score <0.8:
                print("C")
            elif score >=0.6 and score <0.7:
                print("D")
            elif score <0.6:
                print("F")
            else:
                print('Entered value is out of range.')
            exit
        except ValueError:
            print("Your input is not a number. It's a string")
        exit
    
if __name__== "__main__":
    main()
