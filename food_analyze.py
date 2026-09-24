# First we check if we are in the right place
import os

print("Current directory:", os.getcwd)
# If-else statement
data_path = "project/othersales.csv"
if os.path.exists(data_path):
    print("SUCCESS : You are in the right path")
else:
    print(" FAIL : Couldn't find path")
    print("Make sure you are using the correct directory")


import pandas as pd
from for_project import for_total, currency
import json
import os

# Read data
df = pd.read_csv('project/othersales.csv')

# Calculate total for each row
totals = []
for index, row in df.iterrows():
    total = for_total(row['quantity'], row['price'])
    totals.append(total)

df['total'] = totals

#Display with formatted totals
print("Sales data: ")
for index, row in df.iterrows():
    format_currency = currency(row['total'])
    print(f"{row['product']} : {format_currency}")

#Show grand total

grand_total = df['total'].sum()
formatted_grand_total = currency(grand_total)
print(f"\nGrand Total: {formatted_grand_total}")

#JSON:
df.to_json('project/othersales.json', orient = 'records', indent = 2)

#CSV:
df.to_csv('project/othersales_with_totals.csv', index = False)
#EXCEL:
df.to_excel('project/othersales.xlsx', index = False)

print("\nFiles saved:")
print("- output/sales_data.json")
print("- output/sales_data.xlsx") 
print("- output/sales_with_totals.csv")
