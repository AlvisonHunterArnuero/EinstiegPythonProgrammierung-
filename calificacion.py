# Made with ❤️ in Python 3 by Alvison Hunter - February 9th, 2021
# Tips de Python & JavaScript en: https://bit.ly/3p9hpqj
grados_dict = {
    0.9: "Sobresaliente",
    0.8: "Notable",
    0.7: "Buena",
    0.6: "Suficiente",
    0.5: "Insuficiente",
}


def validar_calificacion():
    calificacion = 0
    while True:
        try:
            calificacion = float(input("Digitar calificacion obtenida: \n"))
            if calificacion in grados_dict:
                print(f"Calificacion: {grados_dict.get(calificacion).upper()}")
                break
            elif (calificacion < 0.6):
                print(f"Calificacion: {grados_dict.get(0.5).upper()}")
                break
            else:
                print(f"{calificacion} esta fuera del rango de calificaciones.")
                continue
        except ValueError:
            print("El valor ingresado no es válido. Vuelva a intentarlo.")
            continue

    print("Gracias por usar KALEEFPython Software.")

# Llamemos aca la funcion
validar_calificacion()



