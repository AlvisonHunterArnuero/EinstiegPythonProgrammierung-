totalHours = float(input("Enter total working hours: \n"))
weeklyHours  = float(input("Maximum hours per Week?  \n"))
overtimeHours= totalHours - weeklyHours
weeklyRate = 10.50
overtimeRate = 5.75
totalPayment = 0
if totalHours <= 40:
    totalPayment = totalHours * weeklyRate
    print(f'Your payment is: => {totalPayment}')

elif totalHours > 40:
    totalPayment = (totalHours * weeklyRate) + (overtimeHours * overtimeRate)
    print(f'Your payment is: => {totalPayment}')
else:
    print(f'Invalid input on {totalHours} or in the {weeklyHours}')

print('Thank you for using our products') 
