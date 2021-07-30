# In a small town the population is p0 = 1000 at the beginning of a year.
# The population regularly increases by 2 percent per year and moreover
# 50 new inhabitants per year come to live in the town. How many years
# does the town need to see its population greater or equal to p = 1200 inhabitants?
#  -------------------------------------------------------
# At the end of the first year there will be:
# 1000 + 1000 * 0.02 + 50 => 1070 inhabitants
# At the end of the 2nd year there will be:
# 1070 + 1070 * 0.02 + 50 => 1141 inhabitants (number of inhabitants is an integer)
# At the end of the 3rd year there will be:
# 1141 + 1141 * 0.02 + 50 => 1213
# It will need 3 entire years.

# Note:
# Don't forget to convert the percent parameter as a percentage in the body
# of your function: if the parameter percent is 2 you have to convert it to 0.02.
# Made with ❤️ in Python 3 by Alvison Hunter - January 27th, 2021
# Website: https://alvisonhunter.com/
def nb_year(p0, percent, aug, p):
    growth = (p0 + 1000) * percent



# Examples:
nb_year(1000, 5, 100, 5000) -> 15
nb_year(1500, 5, 100, 5000) -> 15
nb_year(1500000, 2.5, 10000, 2000000) -> 10
