# --------------------------------------------------------------------------------
# Generate a list of 6 elems, use that to generate a dict with rand values
# Find the 3 biggest values and print them on the screen afterwards
# Made with ❤️ in Python 3 by Alvison Hunter - April 4th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# --------------------------------------------------------------------------------
from random import *

# generare la lista utilizzando el list comprehension
base_lst = list(["C"+str(i) for i in range(1, 6)])

# generare il dizionario con dict comprehension
gen_dict = {el: randint(1, 99) for el in range(len(base_lst))}

# genera gli chiavi e valori separatamente en lists
k_lst = list(gen_dict.keys())
v_lst = list(sorted(gen_dict.values(), reverse=True))

# Assegna i 3 primi elementi di v_lst a una nuova lista
max_val_lst = v_lst[:3]

# Visualizza sullo schermo gli oggetti generati
print(f"Questa è la lista generata: {base_lst}")
print(f"Questo è il dizionario generato: {gen_dict}")

# Visualizzare i 3 valori più grandi del dizionario e su posizione actuale
print(f"3 Valori piu grandi delle dizionario: {max_val_lst}")
print(
    f"Posizionato a: {[k_lst[list(gen_dict.values()).index(val)] for val in max_val_lst]}")

# Per suggerimenti su JavaScript e Python, visita il nostro canale: https://bit.ly/3p9hpqj
