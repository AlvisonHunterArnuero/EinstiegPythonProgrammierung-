str_given = "2 2 5 5 5 5 5 5 2 6 6 6 6 4 4 6 6 6 5 6 6 6 6"
# 2 5 2 6 4 6 5 6
# 2 6 1 4 2 3 1 4

# Dados cargados
# Suponga que usted está jugando dados con un amigo y quieren saber si los dados están cargados, es decir, si los dados tienden a caer más en un número que en otro. Para ello, toman un solo dado, empiezan a lanzarlo repetidas veces y van llevando el registro del resultado, o sea del número de veces que un valor cae repetidas veces seguidas.
# Debe crear un programa que reciba en una solo entrada los diferentes resultados del dado y en el orden en que fueron apareciendo. Como resultado deben imprimirse dos salidas, primero los valores que fueron apareciendo, sin repetirse consecutivamente, y segundo el número de veces que apareció ese valor.
# Entrada
# La entrada debe ser los diferentes resultados del lanzamiento del dado. Estos resultados deben ir separados por espacio.
# Salida
# La primera salida deben ser los valores del dado que van saliendo, pero sin repetirse consecutivamente, y separados por espacio. La segunda salida deben ser el número de veces que cayó seguidamente un resultado, también separados por espacio.
# Adicional a ello la impresión de salir así:
lst = str_given.split()
first_elem = lst[0]
lst_tmp = []
count_dict = {}
lst_tmp.append(first_elem)
count_dict[first_elem] = 1
counter = 0
print(count_dict)
for el in lst:
    if(el != first_elem):
        first_elem = el
        lst_tmp.append(first_elem)
        counter = 0
    else:
        counter += 1
        count_dict[first_elem] = counter

print(lst_tmp)
print(count_dict)
