    # calculate the age in years, days and hours for an individual as well as preferred languague.
    # I am Using python inspired by the coolest Cuzuquito Chapultepeco from Catarina, Masaya: Elotgamu.
    
    # first, I import a clear function from the OS, to clear the console, since phyton does not provide us
    # with this function so we need to borrow it from the OS, we use a lambda function (anonima) a great
    # type of function that seems to be very popular in Phyton nowadays.
    
import os
clear = lambda: os.system('clear')
import datetime # I will need this to assign current year to a variable
# let us define our main function, this is how they do it in python
def main():
    # let us use here the function to clear up the console
    clear()
    # gather the information needed for this task
    now = datetime.datetime.now()
    currYear = now.year
    name = input("Please type in your Name ").upper()
    birthYear = input("Please type your Year of Birth ")
    years = currYear - int(birthYear)
    months = years * 12
    days = years * 365
    hours = days * 24

    ageRange = ""
    if years < 15: ageRange = "you are still a child"
    elif years > 15 and years <  24: ageRange = "you are certainly young"
    elif years > 24 and years <  64: ageRange = "you are unquestionably an adult"
    else: ageRange = "You are now in the Seniors category"

#Let us format the way we want this message to be displayed on the screen
    summary = "\n Hello {}: \n Your current age is aproximately {} Years Old, meaning that {}. \n Based on your current age, we could say that you've lived so far an equivalent of: \n - {:,} months \n - {:,} days \n - {:,} Hours. \n"
    print(summary.format(name.capitalize(), years, ageRange, months, days, hours))

# let us display favorite language based on the name of the person using if since python does not have switch case
# yes, I know you have a switcher function but for my hello world program I would like to start with the basic first.
    msg = ""
    if name == "ELEAZAR": msg = "\n - Python \n - Proficient knowledge of Vue.js."
    elif name == "BILLI": msg = "\n - React \n - Currently learning TypeScript."
    elif name == "HECTOR": msg = "\n - React.js \n - React Native."
    elif name == "ALVISON": msg = "\n - ASP.NET \n - VB.NET \n - VBA \n - Proficient knowledge of ES6."
    elif name == "AUGUSTO" or name =="FLIEGES": msg = "\n - PHP and all related Frameworks."
    elif name == "ERNESTO" or name == "TITO": msg = "\n - MS.NET \n - ASP.NET \n - .NET Core & Entity Framework"
    else: msg = "\n Information not provided."
    print("\n The Programming languages you love most are:",msg)
    return

if __name__ == "__main__":
    main()

