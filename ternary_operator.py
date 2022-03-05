# -------------------------------------------------------------------
# Ternary Operators in Python 3 - several cases & scenarios examples
# var = true_val if condition else false_val
# Made with ❤️ in Python 3 by Alvison Hunter - October 14th, 2021
# -------------------------------------------------------------------

# using regular if then conditional statement
response = ""
n1 = int(input("Please Enter a Number: "))
if n1 % 2 == 0:
    response = "Even"
else:
    response = "Odd"
print(response)
rd = input("Hit << Enter >> to continue")

# using the ternary operator
n2 = int(input("Please Enter a Number: "))
print("Even" if n2 % 2 == 0 else "Odd")

# another good example for the ternary operator
ask_developer = input("Do you love Python? (y/n): ").lower()
loves_python = True if ask_developer == "y" else False
print("You're the Coolest, dude!" if loves_python else "You should learn Python!")

# Another more obscure and not widely used example involves tuples.
# Here is some sample code: (if_test_is_false, if_test_is_true)[test]
dev_response = input("Do you love Python? (y/n): ").lower()
python_lover = True if dev_response == "y" else False
fav_lang = ("JavaScript", "Python")[python_lover]
print(
    f"You're a Python zealot, dude!"
    if (python_lover == True)
    else f"You probably love frigging {fav_lang}!"
)


# ShortHand Ternary
api_response = None
print(api_response or "No data returned")

# Apply this principle to a function, shall we
def my_function(real_name, optional_display_name=None):
    optional_display_name = optional_display_name or real_name
    print(optional_display_name)

# This one should return Alvison Lucas
my_function("Alvison Lucas")

# This one should return Liam Andre  
my_function("Declan Jaleel", "Liam Andre")  
