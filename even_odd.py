# Create two lists containing even and odd numbers and then return it
# in two contatenated long strings for each of the cases respectively
# -------------------------------------------------------------------
# Made with ❤️ in Python 3 by Alvison Hunter - December 27th, 2020
# Website: https://alvisonhunter.com/

def is_even_or_odd():
    even_lst = [] # temp list for even numbers
    odd_lst=[] # temp list for odd numbers

    # Time to iterate in a fixed range, this could also
    # be handle dynamically by passing arguments for this range
    for el in range(1,87):
        # Ternary operator to solve this in a single line
        even_lst.append(str(el)) if(el % 2) == 0 else odd_lst.append(str(el))

    # Now let us convert those temp list into long strings
    # containing those numbers concatenated as the exercises states
    even_str=''.join([str(el) for el in even_lst])
    odd_str=''.join([str(el) for el in odd_lst])

    # Time to display it on the screen, shall we?
    print(f"Even Numbers: \n{even_str}")
    print(f"Odd Numbers: \n{odd_str}")

# Last, call the function to print those strings with numbers on the screen!
is_even_or_odd()


