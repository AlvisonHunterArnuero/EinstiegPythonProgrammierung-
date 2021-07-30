# ---------------------------------------------------------------------------------------------
# Python Tricks and tips for better coding - Python 3 - Basic Python coding
# Made with ❤️ in Python 3 by Alvison Hunter - May 3rd, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# ---------------------------------------------------------------------------------------------

# First example
name, age, city = input(
    "Enter your Fist Name, age and city separated by commas: ").split(",")
print(name, age, city)

# Second Example | using the all method to apply all the conditions to an if statement
player, club, league = input(
    "Enter Player name, Club and League separated by commas: ").split(",")

all_conditions = [player == "CR7", club ==
                  "Juventus", league == "UEFA Champions"]

if all(all_conditions):
    print(f"{player} is the best soccer player of the world")
else:
    print("Just another regular soccer player")

# Third Example | using the any method to apply at least of the conditions to an if statement
lang, lib, frm = input(
    "Enter your favorite language, library & framework separated by commas: ").split(",")

any_conditions = [lang == "PYTHON", lib == "TENSORFLOW", frm == "FLASK"]

if any(any_conditions):
    print(f"You are using at least one of the best tools for Python Or Python included")
else:
    print("You can simply get by with this one as well...")

# Fourth Example | Variable swap, very easy but effective method
most_popular_lang = "JavaScript"
less_popular_lang = "Python"
print(
    f"Before Swapping: MOST: {most_popular_lang} | LESS: {less_popular_lang}")
most_popular_lang, less_popular_lang = less_popular_lang, most_popular_lang
print(
    f"After Swapping: MOST: {most_popular_lang} | LESS: {less_popular_lang}")

# Fifth Example | Removing duplicated elements on a list with list comprehension
source_lst = [1, 3, 5, 6, 3, 5, 6, 1, 3, 5, 4, 2, 5]
print("The original list is : " + str(source_lst))
results_lst = []
[results_lst.append(x) for x in source_lst if x not in results_lst]
print("The list after removing duplicates : " + str(results_lst))

# Sixth Example | Using the set collection type to avoid duplicated elements on the list
src_lst = ["a", "j", "f", "a", "b", "a", "l",
           "g", "c", "b", "n", "f", "b", "g", "a"]
print("The original list is : " + str(src_lst))
src_lst = list(set(src_lst))
print("The list after removing duplicates : " + str(src_lst))

# Seventh Example | Find the most repeated element of a list
num_lst = [4, 5, 3, 6, 7, 8, 8, 7, 3, 2, 2, 5, 2, 1, 7, 6, 5, 7]
print("The original list is : " + str(num_lst))
most_rep = max(set(num_lst), key=num_lst.count)
print("The most repeated element is : " + str(most_rep))

# eight Example | Using list comprehension to get even or odd numbers
even_num_lst = [el for el in range(20) if el % 2 == 0]
odd_num_lst = [el for el in range(20) if el % 2 == 1]
print(f"EVEN: {even_num_lst} | ODD: {odd_num_lst}")

# ninth example | Passing several parameters at once to a function


def square_numbers(*numbers):
    sqr_lst = []
    for num in numbers:
        sqr_lst.append(num**2)
    return sqr_lst


print(square_numbers(2, 3, 4, 5, 3, 2, 6, 7, 8, 9, 7, 6))

# Tenth Example | Reversing an string
phrase = "Python is awesome"
print(phrase[::-1])

# Eleventh Example | Find if a string is a palindrome or not
palin = "wow".lower()
print("Is Palindrome" if(palin.find(palin[::-1]) == 0) else "Not a Palindrome")
