#Made with ❤️ in Python 3 by Alvison Hunter - Last Edited on July 9th, 2020
# calculate the age in years, days and hours for an individual as well as preferred programming language.
from enum import Enum
import datetime
def main():
    # Using enum class to create the age range enumerations
    class age_cat(Enum):
        BABY = "you are still a baby"
        CHILD = "you are still a child"
        YOUNG = "you are certainly young"
        ADULT = "you are unquestionably an adult now"
        SENIOR = "You are now a fit for the Seniors category"

   # This dict holds the list of devs that I have registered on my list already
    dict_names = {
        "ELEAZAR":"\n - Python \n - Django \n - Proficient knowledge of Vue.js.",
        "BILLI": "\n - React \n - Currently learning TypeScript.",
        "HECTOR": "\n - React.js \n - React Native.",
        "ALVISON":"\n - ASP.NET \n - VB.NET \n - VBA \n - Proficient knowledge of ES6.",
        "AUGUSTO":"\n - PHP and all related Frameworks.",
        "ERNESTO":"\n - MS.NET \n - ASP.NET \n - .NET Core & Entity Framework"
 }

    # gather the information needed for this task
    now = datetime.datetime.now()
    currYear = now.year
    name = input("Please type in your Name ").upper()
    birthYear = int(input("Please type your Year of Birth "))
    years = currYear - birthYear
    months = years * 12
    days = years * 365
    hours = days * 24

    msg = ""
    ageRange = ""
    if years < 3: ageRange = age_cat.BABY.value
    elif years >= 3 and years < 15: ageRange = age_cat.CHILD.value
    elif years >= 15 and years <  24: ageRange = age_cat.YOUNG.value
    elif years >= 24 and years <  64: ageRange = age_cat.ADULT.value
    else: ageRange = age_cat.SENIOR.value

    #Let us format the way we want this message to be displayed on the screen
    msg = dict_names.get(name)
    summary = "\n Hello {}: \n Your current age is aproximately {} Years Old, meaning that {}. \n Based on your current age, we could say that you've lived so far an equivalent of: \n - {:,} months \n - {:,} days \n - {:,} Hours. \n"
    print(summary.format(name.capitalize(), years, ageRange, months, days, hours))
    if msg != None:
        print(f"The Programming languages you love the most are: {msg}")
    else:
        msg= "Programming languages Information not provided. The Name {} does not exist in our records."
        print(msg.format(name.title()))

if __name__== "__main__":
    main()

