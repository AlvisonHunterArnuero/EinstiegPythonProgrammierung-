# Realice un programa que almacena las 10 calificaciones en letras de un alumno. Las calificaciones
# pueden ser (A,B,C,D ó F). Al final debe contar la cantidad de A,B,C,D ó F que obtuvo el alumno.
# Made with ❤️ in Python 3 by Alvison Hunter - November 27th, 2020
import collections
def count_marks():
    # Aqui agregaremos las notas del alumno para cada clase
    lst_final_marks = []
    tup_int_to_ord = ('primera','segunda','tercera','cuarta','quinta','sexta','séptima','octava','novena','décima')
    # Ahora probemos nuestra rutina, manejando cualquier error por aca
    try:
        #Obtengamos el nombre del alumno para que se vea mas bonito el programa
        name = input('Por Favor ingrese nombre del Alumno: \n')
        max_marks_amount = int(input('Ingrese cantidad de notas a agregar: '))
        #no es necesario, pero vamos a restringir la cantidad maxima de notas agregadas
        if(max_marks_amount > 10):
            print('No se puede ingresar mas de diez notas')
            quit

        #si son diez o menos, procedamos entonces con este problema
        for n in range(max_marks_amount):
            #capturar aca cada una de estas notas
            mark = input(f'Ingrese {tup_int_to_ord[n]} nota del alumno: ')
            #ahora se las agregamos al list
            lst_final_marks.append(mark)


        # aqui manejamos cualquier exception, todo aqui mismo por cualquier cosa
    except:
        print("Uh oh! Algo salio realmente mal, muchach@s!")
        quit
        # Si todo salio bien, procedamos a contar cada nota a ver cuantas veces se repitieron
    finally:
        print(f'Resultados Finales de {len(lst_final_marks)} Calificaciones para {name}:')
        count_results = collections.Counter(lst_final_marks)
        for k,v in count_results.items():
            print(f'Las notas con {k} fueron un total de {v}')


count_marks()
