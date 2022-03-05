from datetime import date
f_date = date(2021, 3, 1)
l_date = date(2022, 1, 15)
delta = l_date - f_date
print(delta.days)
