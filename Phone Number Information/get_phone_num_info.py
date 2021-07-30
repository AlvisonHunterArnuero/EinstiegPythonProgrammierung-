# Phone Number Tracker to display country, location, SIM, service provider and if available, user information
# Installation: Install using pip with: pip install phonenumbers
# Made with ❤️ in Python 3 by Alvison Hunter - January 27th, 2021
import phonenumbers
from phonenumbers import carrier as car
from phonenumbers import geocoder as gc
def get_phone_num_info():
    while True:
        try:
            phone_num = input("Please Enter Phone Number with area code:")
            print("Obtaining phone number information, please wait...")
            num = phonenumbers.parse(phone_num)
            print(num)
            print(f"Country: {gc.country_name_for_number(num,'en')} | Description: {gc.description_for_number(num,'en')}")
            print(f"Carrier: {car.name_for_number(num,'en')} | {car.safe_display_name(num,'en')}")

        except Exception as err:
            print(f"Uh Oh! An error has occurred: {err}")
            pass
        else:
            print(f"{phone_num} was successfully decoded.")
            break

get_phone_num_info()
