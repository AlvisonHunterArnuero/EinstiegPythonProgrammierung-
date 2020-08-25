#Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
#Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
#Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).

#You should use input to read a string and float() to convert the string to a number.
#Do not worry about error checking the user input - assume the user types numbers properly.

#Made with ❤️ in Python 3 by Alvison Hunter - August 20th, 2020

def main():
    totalHours = float(input("Enter total working hours: \n"))
    hourly_rate  = float(input("Enter hourly rate:  \n"))
    try:
        weeklyHours = 40
        overtimeHours= totalHours - weeklyHours
        weeklyRate = 10.50
        overtimeRate = float(hourly_rate) * 1.5
        gross_pay = 0
        if totalHours <= 40:
            totalPayment = totalHours * hourly_rate
            print(f'Your payment is: => {totalPayment}')

        elif totalHours > 40:
            gross_pay = (weeklyHours * hourly_rate) + (overtimeHours * overtimeRate)
            print(f'Your payment is: => {gross_pay}')
        else:
            print(f'Invalid input on {totalHours} or in the {hourly_rate}')

        print('Thank you for using our products.')
    except ValueError:
            print("Your input is not a number. It's a string")
    
if __name__== "__main__":
    main()
