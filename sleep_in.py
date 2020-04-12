# This routine will validate if you are on weekend and on vacation,
# if weekday is False and vacation True, you can certainly sleep in.
from datetime import date
import enum
class SleepIn(enum.Enum):
   TRUE = "you can certainly sleep in."
   FALSE = "you cannot sleep in."

def sleep_in(weekday, vacation, day, name):
    weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
    boolResponse = False
    if weekday == False and vacation == True:
        boolResponse = True
        print("Hello {}, since today is {} and you're on vacations, \n{}!".format(name, weekDays[day], SleepIn.TRUE.value))
    elif weekday == True and vacation == False:
        boolResponse = False
        print("{}, you are neither on vacations nor on weekends, \nhence, {}".format(name,SleepIn.FALSE.value))
    else:
        boolResponse = True
        print("{} is a weekend day, {} however, you're not on vacations,\nthus, {}".format(weekDays[day], name, SleepIn.FALSE.value))
    return boolResponse

def main():
    weekday = False
    vacation = False
    today = date.today()
    day = today.weekday()
    print("=========================================")
    name = input("What is you name, please? ")
    isOnVacation = input("Are you on vacations today? ")
    if day >= 5 and isOnVacation.upper() =="YES":
        weekday = False
        vacation = True
        sleep_in(weekday, vacation, day, name)
    elif day < 5 and isOnVacation.upper() =="YES":
        weekday = True
        vacation = True
        sleep_in(weekday, vacation, day, name)
    else:
        vacation = False
        weekday = False
        sleep_in(weekday, vacation, day, name)

if __name__== "__main__":
    main()
