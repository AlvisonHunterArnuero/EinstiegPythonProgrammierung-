class Hunter:
    def __init__(self, name, age, languages, skills, father_likeness):
        self.name = name
        self.age = age
        self.languages = languages
        self.skills = skills
        self.father_likeness = father_likeness
        self.mother_likeness = 100-father_likeness

    def displayFamilyMember(self):
        print(f"Current age: {self.age} years old.")
        print(f"Spoken languages: {self.languages}")
        print(f"Skills: {self.skills}")
        print(f"Likeness to Father: {self.father_likeness}%")
        print(f"Likeness to Mother: {self.mother_likeness}%")

    def Goodbye(self):
        print(f"\nGood bye for now, {self.name[:self.name.find(' ')]}.")

class Son(Hunter):
  def Greet(self):
    print(f"\nHello! My name is {self.name}.")
    super().displayFamilyMember()
    super().Goodbye()

Declan = Son("Declan Jaleel Hunter",7,"English & Spanish","musician, painter, singer",95)
Declan.Greet()
Liam = Son("Liam Andre Hunter",3,"English & Spanish","singer, builder",15)
Liam.Greet()
