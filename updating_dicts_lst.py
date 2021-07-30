# -------------------------------------------------------------------------
# Basic operations with colletion types | Python exercises | Beginner level
# Generate list with random elements, find the first odd number and its index
# Create empty dict, fill up an empty list  with user input & update dictionary
# Made with ❤️ in Python 3 by Alvison Hunter Arnuero - May 30th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# -------------------------------------------------------------------------

import random
# lista aleatoria
lst = []
name_lst = []
empty_dict = {}

# llenar lista aleatoria
for el in range(10):
    lst.append(random.randrange(10))

# mostrar la lista genarada
print(lst)

# encontrar el primer numero impar
for ind, num in enumerate(lst):
    if num % 2 == 0:
        pass
    else:
        print(f"El número {num} es impar y esta en la posicion {ind}.")
        break
# llenar lista vacia de nombres con user input
amnt = int(input("Escriba Cuantos nombres ingresaras? \n"))
[name_lst.append(
    input(f"Escriba Nombre #{elem+1}: ").title()) for elem in range(amnt)]

# llenar diccionario vacio con datos de la lista llenada
for indx, name in enumerate(name_lst):
    empty_dict[str(indx+1)] = name_lst[indx]

# Imprimimos dictionary ya con los datos listos
print(f"{empty_dict}")

