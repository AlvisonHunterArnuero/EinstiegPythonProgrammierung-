# Ok, Let's Suppose you have $100, which you can invest with a 10% return each year.
#After one year, it's 100×1.1=110 dollars, and after two years it's 100×1.1×1.1=121.
#Add code to calculate how much money you end up with after 7 years, and print the result.
# Made with ❤️ in Python 3 by Alvison Hunter - September 4th, 2020
# note: this can also be simply done by doing the following: print(100 * 1.1 ** 7)
import sys

def user_input(args_lbl_caption, args_input_caption):
    """This function sets a Label above an input and returns the captured value."""
    try:
        print(args_lbl_caption.upper())
        res = int(input(args_input_caption+": \n"))
        return res
    except ValueError:
        sys.exit("Oops!  That was no valid number.  Try again...")
        exit

def calculate_investment():
    """This function calculates the yearly earnings based on user input from cust_input function."""
    #this tuple will contain all of my captions for the user input function that I am using on this routine
    input_captions_tuple = (
        "Initial Investment:",
        "Amount of money that you have available to invest initially",
        "Estimated Interest Rate:",
        "Your estimated annual interest rate[10,15,20 etc]",
        "Length of Time in Years:",
        "Length of time, in years that you are planning to invest"
        )
    #This will serve as an accumulator to store the interest per year
    acc_interest = 0
    #let's get the information using a called function to get and validate this data
    initial_investment=user_input(input_captions_tuple[0],input_captions_tuple[1])
    interest_rate_per_year=user_input(input_captions_tuple[2],input_captions_tuple[3])
    length_of_time_in_years=user_input(input_captions_tuple[4],input_captions_tuple[5])

# if the called function returns an empty object or value, we will inform about this error & exit this out
    if initial_investment  == None or interest_rate_per_year  == None or length_of_time_in_years  == None:
        sys.exit("These values should be numbers: You entered invalid characters!")
#If everything goes well with the user input, let us proceed to make this calculation
    for year in range(length_of_time_in_years):
        acc_interest = initial_investment *(interest_rate_per_year/100)
        initial_investment = initial_investment + acc_interest

# print the results on the screen to let the user know the results
    print("The invested amount plus the yearly interest for {} years will be $ {:.2f} dollars.".format(year+1, initial_investment))

#let's call the function to put it into action now, cheers, folks!
calculate_investment()

#This could also be done by using python simplicity by doing the following:
print(f'a simpler version: {100 * 1.1 ** 7}')



