# Represents any school member.
class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Initialized SchoolMember: {self.name}")

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

t = Teacher('Guido Van Rossum', 64, 95000)
s = Student('Alvison Hunter', 41,900)

print('='*80)

members = [t, s]
for member in members:
    # Let's print both Teachers and Students details
	member.tell()
