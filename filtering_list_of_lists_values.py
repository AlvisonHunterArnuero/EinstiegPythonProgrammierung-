# -------------------------------------------------------------------------------
# Take a location from user and filter the people that live in that area in a list.
# Made with ❤️ in Python 3 by Alvison Hunter Arnuero - Thursday, July 22nd, 2021
# Get More JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# --------------------------------------------------------------------------------
locations = [
    ["Alba", "Juan", "San Fernando"],
    ["Latex", "Martin", "San Miguel"],
    ["Acosta", "Roberto", "Don Torcuato"],
    ["Perez", "Anacleto", "San Miguel"],
    ["Rodriguez", "Marcelo", "San Miguel"],
    ["Martinez", "Laura", "Del Viso"],
    ["Santana", "Carlos", "San Fernando"],
    ["Edreira", "Juana", "Pilar"],
]
location = input("Please Enter Location: ").title()
filtered_lst = list(filter(lambda place: place[2] == location, locations))
if filtered_lst == []:
    print(f"Location not found in our records.")
else:
    print("."*45)
    print(f"The following citizens are from {location}")
    print("."*45)
    for ind, el in enumerate(filtered_lst):
        print(f"{ind+1} - {', '.join(el[:2])}")


# Test Drive Example using this routine
# Please Enter Location: san miguel
# .............................................
# The following citizens are from San Miguel
# .............................................
# 1 - Latex, Martin
# 2 - Perez, Anacleto
# 3 - Rodriguez, Marcelo
