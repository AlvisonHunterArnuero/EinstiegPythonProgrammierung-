# -------------------------------------------------------------------------
# Basic operations with colletion types | Python exercises | Beginner level
# In a company there are n employees whose salaries range between $100 & $1000
# Build a program that reports how many employees earn less than $500 a month
# and how many employees earn more than $500 a month. This program must also
# report the total that the company spends on each of its employees monthly.
# Made with ❤️ in Python 3 by Alvison Hunter Arnuero - June 6th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# -------------------------------------------------------------------------
wages_dict = {}
less_than_500 = 0
more_than_500 = 0
total_spent = 0
try:
    num_workers = int(input("Enter number  of  workers: "))
    if(num_workers <= 0):
        print("You must add at least 1 worker!")
        quit()
    else:
        for w in range(num_workers):
            name = input("Enter Worker Name: ")
            salary = float(input("Enter Worker Salary: "))
            wages_dict[name] = salary
        print("="*30)
        print("Monthly Wages Table by Worker:")
        print("="*30)
        print(f"{wages_dict}")

        for key, value in wages_dict.items():
            total_spent += value
            if value < 500:
                less_than_500 += 1
            else:
                more_than_500 += 1
except ValueError:
    print("Expected an Integer, but got String! Try again later.")
    quit()
else:
    print("-"*50)
    print(f"Total Company's Spends for this month: U${total_spent}")
    print(f"{less_than_500} of these workers earn less than U$500 a month.")
    print(f"{more_than_500} of these workers earn more than U$500 a month.")
