from typing import Optional
def dna_to_rna(dna):
    print(dna.replace("T","U"))

age = 12
    
def saludarAguacate(argName: Optional[str] = None) -> str or None:
    while True:
        try:
            # Crear una referencia a la variable global
            global age 
            age = int(input("Escriba Edad: "))
            
            # Validar si el argumento viene o no
            if not isinstance(argName,str):
                print("Esto no es string", type(argName))
                break
            else:
                str_to_print = f"Hola a Todos, {argName}!"
                print(str_to_print if (argName) else "Ahi nos Vemos!")
                break
        except ValueError:
            print(f'You entered {age}, which is not a positive number.')
            break

dna_to_rna("TTTT")
saludarAguacate("Santiago")
dna_to_rna("GCAT")
saludarAguacate("Meyling")
dna_to_rna("GACCGCCGCC")
saludarAguacate(1)