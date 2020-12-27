# Calculate current Age and generation classification for an individual
# Made with ❤️ in Python 3 by Alvison Hunter - December 26th, 2020
# Website: https://alvisonhunter.com/

import datetime # We will need this to assign current year to a variable
def calculate_age_generation_type():
    #  Let us define the generation classification on a dictionary
    generation_type_dict = {"01": "The Silent Generation","02":"Baby Boomers","03":"Generation X","04":"Millennials","05":"Generation Z"}
    # Gather the information needed for this task
    now = datetime.datetime.now()
    currYear = now.year
    age_range = ""
    generation_type = ""
    try:
        print("░░░░░░░░░░░░░░░░  Age Splitted by Year, Days, Hours & Generation Type  ░░░░░░░░░░░░░░░")
        name = input("Please type in your Name \n")
        birth_year = input("Please type your Year of Birth: \n")
        years = currYear - int(birth_year)
        months = years * 12
        days = years * 365
        hours = days * 24

        # Time to classify this individual by age and generation type
        if (years < 10):
            age_range = "you are still a child"
            generation_type = generation_type_dict.get('05')
        elif(years >= 10 and years <= 18):
            age_range = "you are now a teenager"
            generation_type = generation_type_dict.get('04')
        elif (years > 18 and years <= 30):
            age_range = "you are certainly young"
            generation_type = generation_type_dict.get('03')
        elif (years > 30 and years <  60):
            age_range = "you are unquestionably an adult"
            generation_type = generation_type_dict.get('02')
        else:
            age_range = "You are now in the Seniors category"
            generation_type = generation_type_dict.get('01')
    except:
        print("Uh oh, something went really wrong. Exiting this program.")
        return

    finally:
    #Let us format the way we want this message to be displayed on the screen
        summary = """
        Hello {}:
        Your current age is aproximately {} Years Old, meaning that {}.
        Based on your current age, you've lived so far {:,} months or an equivalent of {:,} days
        which are {:,} Total Hours of Life.
        """
        print(summary.format(name.title(), years, age_range, months, days, hours))
    # let us display the generation classification for this individual
        print(f"According to Current Generation Types on Demographic Studies, You belong to the {generation_type}.")

calculate_age_generation_type()
