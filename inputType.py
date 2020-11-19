# Made with ❤️ in Python 3 by Alvison Hunter - November 6th, 2020
def inputType():
    try:
        msg=''
        string = input('Escriba numero o cadena: \n')
        if(string.isnumeric()):
            msg= 'Esto es definitivamente un numero.'
        elif(string.isalpha()):
            msg='Esto es por supuesto una cadena.'
        else:
           msg = 'Esto es cadena mesclada con numerico.'
    except:
        print('Oopsie! Algo salio mal con esta rutina.')
    finally:
       print(msg)
   
inputType()