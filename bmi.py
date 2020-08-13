# This routine calculates the Body Mass Index based on user input of weight in pounds and height in meters
def main():
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
                BMIgrades = "Underweight"
                print('≡'*80)
                print(f"Hello {name}: \nPlease find below your BMI results based on the provided information:")
                print("BODY MASS INDEX:  {:.2f} \nBMI GRADE:   {} ".format(BMI, BMIgrades))
                print('≡'*80)
            elif BMI >= 18.5 and BMI < 25.0:
                BMIgrades = "Normal weight"
                print('≡'*80)
                print(f"Hello {name}: \nPlease find below your BMI results based on the provided information:")
                print("BODY MASS INDEX:  {:.2f} \nBMI GRADE:   {} ".format(BMI, BMIgrades))
                print('≡'*80)
            elif BMI >= 25.0 and BMI < 30.0:
                BMIgrades = "Overweight"
                print('≡'*80)
                print(f"Hello {name}: \nPlease find below your BMI results based on the provided information:")
                print("BODY MASS INDEX:  {:.2f} \nBMI GRADE:   {} ".format(BMI, BMIgrades))
                print('≡'*80)
            else:
                BMIgrades = "Obesity"
                print('≡'*80)
                print(f"Hello {name}: \nPlease find below your BMI results based on the provided information:")
                print("BODY MASS INDEX:  {:.2f} \nBMI GRADE:   {} ".format(BMI, BMIgrades))
                print("COVID-19: \nSevere Obesity (a BMI of 30 or Higher) May Raise Risk of Severe Illness.")
                print('≡'*80)

            logout = input("Exit this program? [y/n]: ")
            if logout == "y" or logout == "Y":
                    print('Program has ended. Thank you for using our products.')
                    print("# Made with ❤️ in Python 3 by Alvison Hunter - April 11th, 2020")
            break

        else:
            break
if __name__== "__main__":
    main()

