# This routine calculates the Body Mass Index based on user input of weight in pounds.
import enum
def main():
    class bmi_category(enum.Enum):
        first ="Underweight"
        second = "Normal weight"
        third = "Overweight"
        fourth = 'Obesity'
    try:
        logout = "n"
        while logout != "y":
                   print("░░░░░░░░░░░░░░░░ Body Mass Index Calculator ░░░░░░░░░░░░░░░")
                   weight = 0
                   height = 0
                   pndskg= 0.453592
                   name = input("Please provide us with your name: ")
                   weight = float(input("Enter your weight [pounds] "))
                   height = float(input("Enter your height [meters] "))
                   isfloat = isinstance(height, float)
                   if isfloat :
                       BMIgrades = ''
                       BMI = 0
                       BMI = (weight*pndskg)/ (height*height)
                       if BMI < 18.5:
                           BMIgrades = bmi_category.first.value
                       elif BMI >= 18.5 and BMI < 25.0:
                           BMIgrades = bmi_category.second.value
                       elif BMI >= 25.0 and BMI < 30.0:
                           BMIgrades = bmi_category.third.value
                       else:BMIgrades = bmi_category.fourth.value

                       print('≡'*80)
                       print(f"Hello {name.title()}: \nPlease find below your BMI results based on the provided information:")
                       print("BODY MASS INDEX:  {:.2f} \nBMI GRADE:   {} ".format(BMI, BMIgrades))
                       print('≡'*80)
                       print("COVID-19: Severe Obesity (a BMI of 30 or Higher) May Raise Risk of Severe Illness.")
                       logout = input("Exit this program? [y/n]: ")
                       if logout.lower() == "y":
                        print('Program has ended. Thank you for using our products.')
                        print("Made with ❤️ in Python 3 by Alvison Hunter - April 11th, 2020")
                        break

    except ValueError:
            print("Error: Your input should be a number not an string. Please try again later.")

if __name__== "__main__":
    main()

