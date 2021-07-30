# ---------------------------------------------------------------------------------------------
# Get a number from user and return its equivalency in letters using Python 3
# Made with ❤️ in Python 3 by Alvison Hunter - July 5th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# ---------------------------------------------------------------------------------------------
numbers = {
    1: "Uno",
    2: "Dos",
    3: "Tres",
    4: "Cuatro",
    5: "Cinco",
    6: "Seis",
    7: "Siete",
    8: "Ocho",
    9: "Nueve",
    10: "Diez",
    11: "Once",
    12: "Doce",
    13: "Trece",
    14: "Catorce",
    15: "Quince",
    16: "Dieciséis",
    17: "Diecisiete",
    18: "Dieciocho",
    19: "Diecinueve",
    20: "Veinte"
}

num = int(input("Ingrese un numero del 1 al 20: "))
if num not in numbers.keys():
    print("Solo enteros no mas grande de 20 pueden ingresarse!")
    quit()
print(
    f"Escojiste el {num}, cuyo equivalente en letras es el NUMERO {numbers[num].upper()}.")
