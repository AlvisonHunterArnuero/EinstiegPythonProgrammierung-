# Find the sum of an N integer number given by the user using a Gauss Approach
# Made with ❤️ in Python 3 by Alvison Hunter - January 15th, 2021
def gauss_sum():
    # This variable will help us controlling the while loop
    exit_out = 'n'
    # While this var keeps being different than y or "", we keep looping
    while exit_out != 'y' or exit_out == "":
        # let us put this  into action, this is the  famous try except block
        # that will help capture a serie of errors that could happen when the user
        # enters any character in the n variable, let us check it out, ya'all!!
        try:
            n = int(input('Please Enter a positive number: \n'))

            # Let's validate first if the entered number is negative and handle that
            # exception. That can be done with the assert: AssertionError methods
            assert(n >= 0), "Oops! Only positive numbers accepted. Please try again."
            # If user does not type integer numbers but other type of characters
            # let us call a ValueError Exception and handle it with an error message
            if type(n) is not int:
                raise ValueError
            elif n <=1:
                print('1')
                return n
            else:
                # Time to do the sum, transform it to string to remove the ending zeros
                rem_dot = str((n * (n + 1)) / 2)
                # Ternary Operator to remove the dots from the string
                print(rem_dot.rstrip('0').rstrip('.')
                      if '.' in rem_dot else rem_dot)
            # Let us ask the user if they want to quit this program
            exit_out = input(
                "Would you like to leave this program (y/n)? \n").lower()
        # Let  us handle some of the most common exceptions for this scenario
        except ValueError:
            # Display the error msg and pass this exception to capture the number again
            print("Oops!  That was not a valid integer number.  Please Try again...")
            pass
        except AssertionError as msg:
            # Display the error generated in this exception and continue to capture the number again
            print(msg)
            pass
        except:
            # If something different happens, let us simply terminate the routine.
            print('An unexpected error has ocurred. Program will shutdown now.')
            quit
        else:
            # This is the culmination of all the routine, including all exceptions ended.
            print('Thanks for using the recursive sum routine. Keep coding in Python!')


# let us call the main  function now, folks!
gauss_sum()
