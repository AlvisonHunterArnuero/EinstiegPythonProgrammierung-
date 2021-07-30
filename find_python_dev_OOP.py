# Description: Create a Class, generate a list with several instances of
# this class and filter the developers that works with Python from that list
# Author: Made with ?? in Python 3 by Alvison Hunter - May 19th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj

class Developer:
    def __init__(self, fullname, title, language, salary):
        self.fullname = fullname.title()
        self.title = title.title()
        self.language = language.title()
        self.salary = salary

    def __str__(self):
        return f"""
        Full Name: {self.fullname}
        Job Title: {self.title}
        Programming Language: {self.language}
        Monthly Salary: ${self.salary}
        """


# Create the list with several instances of this class
devs_lst = [
    Developer("Alvison Hunter", "Python Developer", "Python", 1500),
    Developer("Ernesto Gutierrez", "Software Engineer", "CSharp", 2500),
    Developer("Antonio Flores", "Full Stack Developer", "JavaScript", 3000),
    Developer("Engel Torres", "Python Developer", "Python", 1200),
    Developer("Luis Guido", "Software Developer", "Kotlin", 3500),
]

# Create an object filtering only python devs data
python_developers = filter(
    lambda dev: dev.language == "Python", devs_lst)

# Iterate this object printing its elements information
for pythoneer in python_developers:
    print(pythoneer)
