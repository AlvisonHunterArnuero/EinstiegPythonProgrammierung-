# Made with ❤️ in Python 3 by Alvison Hunter - January 22nd, 2020
def multiply_by_two():
    while True:
        try:
            num = int(input('Please Enter a number: '))
        except ValueError as msg:
                print(msg)
                pass
        else:
            print(f"{num} x 2 = {num*2}")
            print('Thanks for using python')
            break

multiply_by_two()
# Para videos de python visita : https://bit.ly/3p9hpqj


