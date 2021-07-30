# Made with ❤️ in Python 3 by Alvison Hunter - November 3rd, 2020

# primero importaremos este modulo para usar su metodo reduce
import functools as ft

# procedamos ahora a declarar la lista con los numeros que usaremos
numblst = [2, 6, 8, 4, 10, 24, 9, 96]

# Vamos a usar una funcion lambda para hacer nuestro calculo
# aplicandolo a dos de los elementos de la lista numblist
def mcd(a, b): return a if b == 0 else mcd(b, a % b)

# una vez hecho esto, usemos el reduce para iterar en la lista
# aplicando la misma funcion declarada arriba con los valores
# de cada elemento restante de la lista e imprimimos el final
print(ft.reduce(lambda x, y: mcd(x, y), numblst))

# Espero que te sirva, saludos desde Nicaragua. Subire pronto un video
# sobre este algoritmo explicando mas o menos como lo hice en mi canal
# YouTube: https://bit.ly/3mFFgwK
