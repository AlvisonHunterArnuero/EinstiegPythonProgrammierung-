# -------------------------------------------------------------------------
# Introduction to classes using a basic grading score for an student
# Made with ❤️ in Python 3 by Alvison Hunter - March 12th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# -------------------------------------------------------------------------
class Jedi:
    # Constructor and Class Attributes
    def __init__(self, name, age, height , weight, weapon):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.weapon = weapon

    # Methods
    def get_jedi_summary(self):
        print('-'*52)
        print(f"Jedi Name: {self.name} | Age: {self.age} years old.")
        print(f"Jedi's Height: {self.height} | Jedi's Weight: {self.weight}.")
        print(f"Jedi's Favorite weapon is:{self.weapon}")
        print('-'*52)

# Creating instances of the Jedi class
first_jedi = Jedi("Obiwan Kenobi",57,1.85,80, "double-bladed lightsaber")
second_jedi =  Jedi("Luke Skywalker",19,1.72,73,"lightsaber pike")
# find the older jedi of them all
if first_jedi.age > second_jedi.age:
    first_jedi.get_jedi_summary()
else:
    second_jedi.get_jedi_summary()



