# GET BIRTHDAY DAY WITH PYTHON
# Made with ❤️ in Python 3 by Alvison Hunter - December 26th, 2020
# Website: https://alvisonhunter.com/
import datetime as dt
import calendar as cal

def get_birthday_day():
    try:
        date = input("Enter DOB (day/month/year) : \n")
        birthDate = dt.datetime.strptime(date, '%d/%m/%Y')
        day = birthDate.weekday()
    except:
        print("Uh oh, something went really wrong")
        return
    finally:
        print(f"According to Python, You were born on a {cal.day_name[day]}.")

# Let us test this baby now....
get_birthday_day()
