# --------------------------------------------------------------------------------
# Introduction to classes using basic grading score for US Presidents as students
# Made with ❤️ in Python 3 by Alvison Hunter - March 16th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# --------------------------------------------------------------------------------
class Student:
    designated_honors = {
        3.5: 'Cum Laude',
        3.65: 'Magna Cum Laude',
        3.85: 'Summa Cum Laude'
        }

    # Constructor and Class Attributes
    def __init__(self, name, school, gpa, cgpa):
        self.name = name
        self.school = school
        self.gpa = gpa
        self.cgpa = cgpa

    # Regular Methods
    def display_divider(self, arg_char = "-", line_length=100):
        print(arg_char*line_length)

    def is_honored(self):
        if(self.cgpa >= 3.5 and self.cgpa <= 3.64):
            print(f"◆ Honor Roll: {self.designated_honors[3.5]}")
        elif(self.cgpa >= 3.65 and self.cgpa <= 3.84):
            print(f"◆ Honor Roll: {self.designated_honors[3.65]}")
        elif(self.cgpa >= 3.85):
            print(f"◆ Honor Roll: {self.designated_honors[3.85]}")
        else:
            print(f"◆ Unfortunately, You are not Eligible for any Honor or Merit Rolls.")

    def display_grading(self):
        self.display_divider("=",45)
        print(f"Grading Results for: {self.name}")
        print(f"◆ Graduated From: {self.school}")
        print(f"◆ Grade Point Average: {self.gpa}")
        print(f"◆ Cumulative Grade Point Average: {self.cgpa}")
        self.is_honored()

# Creating instances of Student for three new students now
first_student = Student("Barack Hussein Obama II","Harvard Law School",1.85,3.70)
second_student = Student("William Jefferson Clinton", "Georgetown University",2.00,4.01)
third_student =  Student("Donald John Trump", "University of Pennsylvania",1.95,3.90)

# Let us display their respective Grading
first_student.display_grading()
second_student.display_grading()
third_student.display_grading()

