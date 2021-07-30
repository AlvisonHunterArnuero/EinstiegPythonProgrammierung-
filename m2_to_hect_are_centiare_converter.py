# -----------------------------------------------------------------------------------------
# From user input numbers in m2, calculate its equivalence in Hectare, Are & Centiare
# -----------------------------------------------------------------------------------------
# Made with ❤️ in Python 3 by Alvison Hunter - March 29th, 2021
# For JavaScript, Python & Web Development tips, visit our channel: https://bit.ly/3p9hpqj
# -----------------------------------------------------------------------------------------
def calculate_surface():
    HECT = 10000
    ARE = 100
    CENTIARE = 1
    while True:
        try:
            square_meter_surface = int(input("Please enter surface in m²: \n"))
            if(square_meter_surface<=0):
                print("This number should be at least 1.")
                continue
        except ValueError:
            print ("Error: This value should be an amount in m².")
            continue
        except:
            print("Uh oh! Something went really wrong!")
            break
        else:
            hectare = square_meter_surface / HECT
            are = square_meter_surface / ARE
            centiare = square_meter_surface / CENTIARE
            print(f"The given {square_meter_surface}m² is equivalent to:")
            print(f"Hectare: {hectare} | Are: {are} | Centiare: {centiare}")
            break


calculate_surface()
