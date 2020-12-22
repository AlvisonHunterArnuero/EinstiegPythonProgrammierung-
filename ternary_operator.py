# Ternary Operators in Python 3 - several scenarios and cases
# var = true_val if condition else false_val
# Made with ❤️ in Python 3 by Alvison Hunter - December 13th, 2020

rd = "" #to open an input on every case
numb = 6
# USING USUAL IF-ELSE
response = ""
if(numb%2 == 0):
  response = "Even"
else:
  response = "Odd"
print(response)
rd = input("Hit << Enter >> to continue")
# USING TERNARY OPERATOR
response = "Even" if numb%2 == 0 else "Odd"
print(response)
rd = input("Hit << Enter >> to continue")
# Another good example is this
loves_python = True
res = "You're the Coolest" if loves_python else "You should learn Python!"
print(res)
rd = input("Hit << Enter >> to continue")

# Another more obscure and not widely used example involves tuples.
# Here is some sample code: (if_test_is_false, if_test_is_true)[test]
nice = True
personality = ("mean", "nice")[nice]
print("The cat is ", personality)

rd = input("Hit << Enter >> to continue")
# ShortHand Ternary
output = None
msg = output or "No data returned"
print(msg)
rd = input("Hit << Enter >> to continue")

# let us put this into action with a function
def my_function(real_name, optional_display_name=None):
    optional_display_name = optional_display_name or real_name
    print(optional_display_name)

my_function("Alvison") # This one will return Alvison
my_function("Declan", "djJager") # This one will return djJager



