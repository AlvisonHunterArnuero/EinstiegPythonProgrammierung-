# --------------------------------------------------------------------------------
# Introduction to classes using a basic grading score for an student
# Made with ❤️ in Python 3 by Alvison Hunter - March 6th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# --------------------------------------------------------------------------------
people_dict = {12:"Critican", 10:"Chismosos", 6:"Creen En Ti", 3:"Te Motivan", 1:"Ayudan"}
def display_people_in_your_life():
    print("Asi Son Las Personas En Tu Vida:")
    for key, value in people_dict.items():
        print(f"Los que {value}: {'‍🏃'*key}")

display_people_in_your_life()
