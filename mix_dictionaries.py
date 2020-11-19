# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
numbers_dict = {}
upper_dict = {}
lower_dict = {}
NUMBERS = 48
UPPER = 65
LOWER = 32
for number in range(NUMBERS, 58):
    numbers_dict[number]= chr(number)
    
for character in range(UPPER,91):
    upper_dict[character]=chr(character)
    lower_dict[character+LOWER]=chr(character+LOWER)

print('The Numbers: \n',numbers_dict)
print('Upper letters: \n',upper_dict)
print('Lower Letter: \n',lower_dict)
print('All together is: \n',{**numbers_dict,**upper_dict,**lower_dict})
