import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from tabulate import tabulate
from colorama import Fore, init

# Start the colorama module setting the autoreset to True
init(autoreset=True)

# Import the csv file we will be using for the main & secondary dataframes
corona_dt_frm_from_csv = pd.read_csv("Datasets/covid19_Confirmed_dataset.csv")

# Find the shape of the dataframe, to know amount of rows and columns
rows, cols = corona_dt_frm_from_csv.shape
print(Fore.CYAN + f"DATAFRAME ROWS: {rows} DATAFRAME COLS: {cols}")

# Erase unusual columns, such as lat and long in this case
# we will erase it from the source dataframe but it could
# also be done by adding the new content to a variable to avoid
# touching the original one, to save source data like this:
# Example: new_df = corona_dt_frm_from_csv.drop(["Lat", "Long"], axis=1)
corona_dt_frm_from_csv.drop(["Lat", "Long"], axis=1, inplace=True)

# Create another data frame grouping the totals by country and region
corona_group_by_df = corona_dt_frm_from_csv.groupby("Country/Region").sum()

# Find maximum infection rate for all of these countries
countries_lst = list(corona_group_by_df.index)
max_infection_rates_lst = []
for country in countries_lst:
    max_infection_rates_lst.append(
        corona_group_by_df.loc[country].diff().max())

# Add this new list of max infection rate values to our dataframe
corona_group_by_df["max_infection_rates"] = max_infection_rates_lst

# Create a simplified dataframe containing country/region + last data of the month
corona_data_summary = pd.DataFrame(corona_group_by_df["max_infection_rates"])

# Select first 10 rows & 2 columns to display this data in tabulated mode on the screen
print(Fore.LIGHTCYAN_EX +
      "\nGrouped by Country/Region & Maximum Daily Infection Rates:".upper())

# Set the headers Titles for the grid
headers = ["Country/Region", "Maximum Daily Infection Rates"]
print(Fore.LIGHTMAGENTA_EX + tabulate(
    corona_data_summary.iloc[:10, :2],
    headers=headers,
    tablefmt='grid'))

# Select first 10 rows & 1 column from new groupby dataframe to display on screen
print(Fore.YELLOW + "Grouped by Country and Region:")

# Set the headers Titles for the grid
headers = ["Country/Region",
           "Monthly Total of Infections", "Maximum Daily Infection Rates"]

print(Fore.LIGHTBLUE_EX +
      tabulate(corona_group_by_df.iloc[:12, 99:], headers=headers, tablefmt='grid'))

# Time to put all this to action, let's trace any errors during the process
try:
    # Grab the names of the first 5 countries to check data for, separated by comma
    countries_lst = input(
        "Please Enter 5 countries separated by commas: ").split(",")

    for i, cnt in enumerate(countries_lst):
        cnt = cnt.strip().title()
        corona_group_by_df.loc[cnt].plot()

    # Add legend and title on the plot. Call the show method afterwards to display img
    plt.legend()
    plt.title("COVID19 daily cases impact by country".upper(), loc='center')
    plt.xlabel("Average per day")
    plt.ylabel("Maximum Cases")
    plt.tick_params(
        axis='x',          # changes apply to the x-axis
        which='major',      # major tick is affected
        labelbottom=False)         # ticks along the bottom edge are off

    # display grid & customize its colors
    plt.grid(color='green', linestyle='--', linewidth=0.7)

    # display the graph now
    plt.show()

    print("")
    print(Fore.YELLOW + "Daily Maximum Infection per day - listed by Country".upper())
    infections_per_day = {}
    for c in countries_lst:
        c = c.strip().title()
        infections_per_day[c] = corona_group_by_df.loc[c].diff().max()
    headers = ["Country", "Infections Per Day"]
    print(Fore.LIGHTYELLOW_EX+tabulate(infections_per_day.items(),
          headers=headers, tablefmt='grid'))
except KeyError:
    print(Fore.RED +
          "Some of the countries you entered are not present in our records.")
