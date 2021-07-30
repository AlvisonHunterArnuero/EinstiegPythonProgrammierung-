# -------------------------------------------------------------------------------
# Take an order from a customer in a restaurant, write all dishes separated by commas.
# print order details of only available dishes with prices & the order total to pay
# Made with ❤️ in Python 3 by Alvison Hunter Arnuero - Saturday, July 17th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# --------------------------------------------------------------------------------

dishes = {
    "Ajiaco": 20,
    "Hamburguesa": 19,
    "Churrasco": 15,
    "Mondongo": 22,
    "Picada": 18,
    "Tamal": 10
}

ordered_dishes = input(
    "Enter your ordered dishes separated by commas:\n").title().split(",")
if len(ordered_dishes) <= 1 and ordered_dishes[0] == "":
    print("Nothing was ordered. Have a good day!")
else:
    total_to_pay = 0
    available_dishes = []

    for dish in ordered_dishes:
        cur_dish = dishes.get(dish)
        if dishes.get(dish):
            total_to_pay += cur_dish
            available_dishes.append(dish.title()+" - $"+str(cur_dish))

    if len(available_dishes) > 0:
        print(
            f"Please find the description of your order: \n{available_dishes}")
        print(f"Total to Pay: ${total_to_pay} dollars.")
    else:
        print("None of the ordered dishes are available in our menu.")
