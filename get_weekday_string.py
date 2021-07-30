# -----------------------------------------------------------------------------------------
# Get today's date and return its day in number & string, along with the month & the year.
# -----------------------------------------------------------------------------------------
# Made with ❤️ in Python 3 by Alvison Hunter - April 2nd, 2021
# For JavaScript, Python & Web Development tips, visit our channel: https://bit.ly/3p9hpqj
# -----------------------------------------------------------------------------------------
import datetime


def get_weekday():
    dt = datetime.datetime.today()
    weekday_text = dt.strftime('%A')
    weekday_num = dt.strftime('%d')
    mo = dt.strftime('%B')
    yr = dt.strftime('%Y')
    hrs = dt.strftime('%H')
    mins = dt.strftime('%M')
    secs = dt.strftime('%S')
    per = dt.strftime('%p')

    print(f"Today is {weekday_text}, {weekday_num} of {mo} of the year {yr}.")
    print(f"Current Time is: {hrs}:{mins}:{secs} {per}.")


get_weekday()
