def calculate_gross_pay():
    hrs = float(input("Enter Worked Hours: "))
    rt = float(input("Enter Hourly Rate: "))
    return ((hrs * rt) + ((hrs - 40) * (rt * 0.50))) if (hrs > 40) else  (hrs * rt)

print(f'Gross Pay: ${calculate_gross_pay():.2f}')
