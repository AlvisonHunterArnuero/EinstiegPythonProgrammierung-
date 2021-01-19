# Find the recursive sum of an N integer number given by the user
# Made with ❤️ in Python 3 by Alvison Hunter - January 17th, 2021
def recursive_sum(n):
    return n if n <= 1 else n + recursive_sum(n-1)

# Let us proceed by calling the main function to capture the number
# and pass it as a param for the recursive sum function
def main():
       try:
          num = int(input("Please Enter a positive number: \n "))
          # Let's validate first if the entered number is negative and handle that
          # exception. That can be done with the assert: AssertionError methods
          assert(num >= 0), "Oops! Only positive numbers accepted. Please try again."
          # If user does not type integer numbers but other type of characters
          # # let us call a ValueError Exception and handle it with an error message
          if type(num) is not int:
                 raise ValueError
          # Common Exceptions Errors Handlers
       except ValueError:
          # Display the error msg and pass this exception to capture the number again
          print("Oops!  That was not a valid integer number.  Please Try again...")
          quit
       except AssertionError as err:
            # Display the error generated in this exception and continue to capture the number again
          print(err)
          quit
       except:
          print('An unexpected error has ocurred. Program will shutdown now.')
          quit
       else:
            # This is the culmination of all the routine, including all exceptions ended.
            print(f"The sum is: {recursive_sum(num)}")

if __name__== "__main__":
    main()
