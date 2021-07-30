# --------------------------------------------------------------------------------
# Bike rentals. 100 mins = 7xmin, 101 > 1440 = 50 x min, 1440 > 96000
# Made with ❤️ in Python 3 by Alvison Hunter - March 23th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# --------------------------------------------------------------------------------
def bike_rental_payment():
    REGULAR_RATE = 7
    OVERTIME_RATE = 50
    regular_charge = 0
    overtime_charge = 0
    exceeding_charge = 0
    total = 0
    while True:
        # Error handling try...except init block
        try:
            usage_time = int(input("Please enter total amount of rented minutes: \n"))
            if(usage_time<=0):
                print("Invalid amount of rented minutes. Please try again.")
                continue
            if(usage_time <= 100):
                regular_charge = usage_time * REGULAR_RATE
            elif(usage_time>100 and usage_time <= 1440):
                regular_charge = 100 * REGULAR_RATE
                overtime_charge =  (usage_time - 100) * OVERTIME_RATE
            else:
                regular_charge = 100 * REGULAR_RATE
                overtime_charge = 1300 * OVERTIME_RATE
                exceeding_charge = 0 if usage_time < 1440 else 96000

        # Error handling exceptions
        except ValueError:
            print ("ValueError: This value should be a number.")
            continue
        except:
            print("Uh oh! Something went really wrong!. Please try again.")
            quit
        else:
            total = regular_charge + overtime_charge + exceeding_charge
            print(f"Invoice Total: U${total}.")
            break



bike_rental_payment()

