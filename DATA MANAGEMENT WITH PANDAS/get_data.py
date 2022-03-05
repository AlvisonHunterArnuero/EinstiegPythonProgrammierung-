#----------------------------------------------------------------------------
# Basic CSV file data reading and manipulation using the python pandas library
# Made with ❤️ in Python 3 by Alvison Hunter Arnuero - February 13th, 2022
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
#---------------------------------------------------------------------------
# Dependencies - Modules - Packages
# Pandas:  pip3 install pandas
# Openpyxl: pip3 install openpyxl
# Tabulate: pip3 install tabulate

import pandas as pd
from tabulate import tabulate

# Time to load the information from the file
df = (pd.read_csv('account_transactions.csv'))

# Info on DataFrame
print('Dataframe Information \n', )
print(tabulate(df.info(), headers = 'keys', tablefmt = 'pretty'))
input("Press Enter to continue...") 

# Rows and Columns
print(f'Dataframe contains {df.shape[0]} rows & {df.shape[1]} columns.')
input("Press Enter to continue...") 

# Summary statistics
print('Dataframe Summary \n')
print(tabulate(df.describe(), headers = 'keys', floatfmt=".4f", tablefmt = 'pretty'))
input("Press Enter to continue...") 

# Get the columns names
print('Dataframe Headers: \n',df.columns.values.tolist())
input("Press Enter to continue...") 

# Get first 5 rows of the Dataframe
# displaying the DataFrame
print(tabulate(df.head(5), headers = 'keys', tablefmt = 'grid'))
input("Press Enter to continue...") 

# Get a sample of the dataframe content
print(tabulate(df.sample(20), headers = 'keys', tablefmt = 'simple'))
input("Press Enter to continue...")

# Filtering with query method
new_df = df.query("DESCRIPTION ==' TEF DE:MARIA ELENA ROBELO SOMA'")

# displaying the DataFrame with tabulate formatting
print(tabulate(df, headers = 'keys', tablefmt = 'fancy_grid'))
input("Press Enter to continue...") 

# displaying the DataFrame sorted
new_df.sort_values(by=['DATE'])

# Remove first column and save this dtframe to an excel file
print(tabulate(new_df[1:], headers = 'keys', floatfmt=".4f", tablefmt = 'pretty'))

question = input("Would you like to save this data? (y/n): ")
if(question.lower().strip()[0] == "y"):
    new_df.to_excel('smbs_payments.xlsx',  sheet_name='SMBS PAYMENTS')
    print('Data has successfully written into Excel File')
else:
    print("Thank your for using Python Pandas DataFrame!")
    
    
