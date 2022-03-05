# Represents any school member.
class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Initialized SchoolMember for: {self.name}")

    # Tell my details.
    def tell(self):
        print(f"Name: {self.name} Age: {self.age}")


# Represents a teacher.
class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print(f"Initialized Teacher: {self.name}")

    def tell(self):
        SchoolMember.tell(self)
        print(f"Salary: {self.salary}")


# Represents a student.
class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print(f"Initialized Student: {self.name}")

    def tell(self):
        SchoolMember.tell(self)
        print(f"Marks: {self.marks}")


class Counselor(SchoolMember):
    def __init__(self, name, age):
        SchoolMember.__init__(self, name, age)


class Principal(SchoolMember):
    def __init__(self, name, age):
        super().__init__(name, age)


class Nurse(SchoolMember):
    def __init__(self, name, age, phone):
        SchoolMember.__init__(self, name, age)
        self.phone = phone

    def greet(self):
        print(
            "Hello, ",
            self.name,
            ".\nYour Age is ",
            self.age,
            " years old and your Phone is: ",
            self.phone,
        )


# Let us put these babies in action by creating instances, shall we?
sm = SchoolMember("Bill Gates", 56)
t = Teacher("Guido Van Rossum", 64, 95000)
s = Student("Alvison Hunter", 41, 900)
c = Counselor("Mark Zuckerberg", 34)
p = Principal("Evan You", 23)
n = Nurse("Sarah Drasner", 24, 99887766)

# Declare an list containing all these instances
members = [t, s, c, p, n]

for member in members:
    # Let's print each of their details
    member.greet() if(member == n) else member.tell()
