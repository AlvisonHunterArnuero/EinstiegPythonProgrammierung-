# --------------------------------------------------------------------------------
# Create a list with 5 people's name, last name and current age.
# return the list along with the amount of adults on this list.
# Made with ❤️ in Python 3 by Alvison Hunter - June 17th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# --------------------------------------------------------------------------------
people_lst = []
adults_counter = 0
found_msg = "adults were found on this list."

for e in range(5):
    name = input("Please Enter Name: ")
    last_name = input("Please Enter Last Name: ")
    age = int(input("Enter Age: "))
    if age >= 18:
        adults_counter += 1
    people_lst.append([name.title(), last_name.title(), age])

print("+"*35)
for person in people_lst:
    print(f"- {person[0]} {person[1]} is {person[2]} years old.")

print("."*35)
print(f"{adults_counter} {found_msg}." if adults_counter >
      0 else f"No {found_msg}")
print("."*35)
