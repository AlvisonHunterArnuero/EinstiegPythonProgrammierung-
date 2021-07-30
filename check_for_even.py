# ---------------------------------------------------------------------------------------------
# Find all even numbers from a list and add them to a new list
# Made with ❤️ in Python 3 by Alvison Hunter - March 1st, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# ---------------------------------------------------------------------------------------------
votes_list = [1,2,5,6,7,3,8,12,10]

def check_for_even(num_list):
    even_list = []
    [even_list.append(n) for n in num_list if n%2==0]
    print(f"New List: {even_list}")
    
# This Should return New List: [2, 6, 8, 12, 10]
check_for_even(votes_list)
