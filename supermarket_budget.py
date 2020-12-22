# Made with ❤️ in Python 3 by Alvison Hunter - December 21st, 2020
food_dict = {"Rice":2000,"Potatoes":1520,"Spaghetti":2000,"Oranges":1523}
def shopping_budget():
    try:
        print("Ud va a su supermercado mas cercano y encuentra estos precios: ")
        print(food_dict)
        budget = int(input("Ingrese budget actual: \n"))
        total_costo = sum(food_dict.values()) - budget
    except:
        print("Uh oh! Algo salio realmente mal, cerremos esta app!")
        quit
    finally:
        msg ="Le Sobran: " if total_costo < 0 else "Le faltan: "
        print(msg,abs(total_costo))

shopping_budget()
