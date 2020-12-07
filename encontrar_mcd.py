#Esta función implementa el algoritmo euclidiano para encontrar el
# factor común más alto (HCF) de dos números pasados a una funcion
# Made with ❤️ in Python 3 by Alvison Hunter - November 3rd, 2020
def find_GCD(int1, int2):
    while(int2):
        int1, int2 = int2, int1 % int2
#retornemos el valor final del bucle para int1
    return int1

#nuestra lista de numeros a usar en la funcion declarada
numblst = [2,6,8,4,10,24,9,96]
#asignemos los primeros dos elementos para calcular la primer iteracion
lst_item_01 = numblst[0]
lst_item_02 = numblst[1]

#ahora aqui pasamos estos argumentos a la funcion
highest_common_factor = find_GCD(lst_item_01,lst_item_02)
#llego la hora de iterar el resto de elementos de la lista con la funcion
for i in range(2,len(numblst)):
    highest_common_factor = find_GCD(highest_common_factor, numblst[i])

#culminado este paso procedemos a pintar el resultado final
print(f'Resultado Final es: {highest_common_factor}')
#Espero que te sirva, saludos desde Nicaragua. Subire pronto un video
# sobre este algoritmo explicando mas o menos como lo hice en mi canal
# YouTube: https://bit.ly/3mFFgwK


