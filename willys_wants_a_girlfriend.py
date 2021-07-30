# -------------------------------------------------------------------------------
# Wally is searching for a girlfriend, older than 30, art lover, from Mendoza.
# Find all possible matches with the requirements Wally provided. The program
# must print the names of the girls separated by commas, and details such as
# each of the matches details such as age, hobbies & the city they come from.
# Made with ❤️ in Python 3 by Alvison Hunter Arnuero - Wed, July 28th, 2021
# Get More JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# --------------------------------------------------------------------------------
dates_lst = [
    {
        "name": "Julia",
        "sex": "femenino",
        "age": 29,
        "hobbies": ["correr", "musica", "leer"],
        "city": "Cordoba",
    },
    {
        "name": "Juan",
        "sex": "masculino",
        "age": 41,
        "hobbies": ["leer", "alpinismo", "Juegos de Mesa"],
        "city": "Mendoza",
    },
    {
        "name": "Camila",
        "sex": "femenino",
        "age": 18,
        "hobbies": ["escribir", "arte"],
        "city": "Mendoza",
    },
    {
        "name": "Lucia",
        "sex": "femenino",
        "age": 35,
        "hobbies": ["arte"],
        "city": "Mendoza",
    },
    {
        "name": "Daniel",
        "sex": "masculino",
        "age": 50,
        "hobbies": ["boxeo", "leer", "arte"],
        "city": "Mendoza",
    },
    {
        "name": "Onice",
        "sex": "femenino",
        "age": 31,
        "hobbies": ["cantar", "arte"],
        "city": "Mendoza",
    },
]
possible_dates = []
for el in dates_lst:
    if (
        el["sex"] == "femenino"
        and el["age"] > 30
        and "arte" in el["hobbies"]
        and el["city"] == "Mendoza"
    ):
        possible_dates.append(
            [el["name"], el["age"], el["hobbies"], el["city"]])

print("Matches found for a date:", ", ".join(
    [grl[0] for grl in possible_dates]))
print("-" * 60)
print("Dates Details:")
[print(grl_det) for grl_det in possible_dates]
