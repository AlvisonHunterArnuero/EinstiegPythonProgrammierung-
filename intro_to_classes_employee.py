# --------------------------------------------------------------------------------
# Introduction to classes using getters & setters with an employee details example.
# Made with ❤️ in Python 3 by Alvison Hunter - March 16th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# --------------------------------------------------------------------------------
class Employee:
    # Constructor and Class Attributes
    def __init__(self, first, last, title, department):
        self.first = first
        self.last = last
        self.title = title
        self.department = department
        self.email = first.lower()+"."+last.lower()+"@email.com"

    # REGULAR METHODS
    def display_divider(self, arg_char = "-", line_length=100):
        print(arg_char*line_length)

    def display_information(self):
        self.display_divider("-",45)
        print(f"Employee Information | {self.first} {self.last}".center(45, ' '))
        self.display_divider("-",45)
        print(f"Title: {self.title} | Department: {self.department}")
        print(f"Email Address: {self.email}")
        print("\n")

    # GETTERS
    @property
    def fullname(self):
        print(f"{self.first} {self.last}")

    # SETTERS
    @fullname.setter
    def fullname(self,name):
        first, last = name.split(" ")
        self.first = first
        self.last = last
        self.email = first.lower()+"."+last.lower()+"@email.com"

    # DELETERS
    @fullname.deleter
    def fullname(self):
        print("Name & Last name has been successfully deleted.")
        self.first = None
        self.last = None

# CREATE INSTANCES NOW
employee_01 = Employee("Alvison","Hunter","Web Developer","Tiger Team")
employee_01.display_information()
employee_01.fullname = "Lucas Arnuero"
employee_01.display_information()
del employee_01.fullname


