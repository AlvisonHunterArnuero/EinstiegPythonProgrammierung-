# --------------------------------------------------------------------------------
# Routine to Find the eldest person out of two in an iteration
# Made with ❤️ in Python 3 by Alvison Hunter - March 12th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# --------------------------------------------------------------------------------
def find_oldest():
    person_dict = {}
    for i in range(2):
        name = input("Please enter name: ").title()
        age = int(input("Please enter age: "))
        person_dict[age] = name
    
    if len(person_dict) == 1:
        print("Both individuals have the same age")
    else:
        older = max(list(person_dict.keys()))
        print(f"Oldest person is: {person_dict[older]} with {older} years old.")
    
find_oldest()


