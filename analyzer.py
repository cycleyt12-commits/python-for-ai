import os

# Check if we're in the right place
print("Current directory:", os.getcwd())

# Check if our data file exists
data_path = "data/sales.csv"
if os.path.exists(data_path):
    print(f"✅ Found {data_path}")
else:
    print(f"❌ Cannot find {data_path}")
    print("Make sure you're running from the sales-analysis folder!")


"""
Best practices

    Keep data separate - Don’t mix code and data files
    Use clear names - data for input files, output for results
    Simple structure - Keep your main script at the project level
    Test as you go - Use Shift+Enter to run code step by step

"""

import os

print("Current directory:", os.getcwd())

data_path = "analyzer.py"
if os.path.exists(data_path):
    print(f"Found {data_path}")
else:
    print(f"Cannot find {data_path}")





import pandas as pd
import json
import os

# Read the CSV file
df = pd.read_csv('data/sales.csv')
print("CSV Data:")
print(df)
print(f"\nShape: {df.shape[0]} rows, {df.shape[1]} columns")

# Quick operation: calculate total for each row
df['total'] = df['quantity'] * df['price']
print("With totals:")
print(df)

# Create output directory
os.makedirs('output', exist_ok=True)

# Save as different formats
# 1. JSON format (good for web APIs)
df.to_json('output/sales_data.json', orient='records', indent=2)

# 2. Excel format (good for sharing)
df.to_excel('output/sales_data.xlsx', index=False)

# 3. Updated CSV (with our new total column)
df.to_csv('output/sales_with_totals.csv', index=False)

print("\nFiles saved:")
print("- output/sales_data.json")
print("- output/sales_data.xlsx") 
print("- output/sales_with_totals.csv")


# JSON - Great for APIs and web applications
{
  "date": "2024-01-01",
  "product": "Laptop",
  "quantity": 2,
  "price": 999.99
}

# CSV - Simple, universal, good for data analysis


# Excel - Feature-rich, good for business users
# (Binary format with formatting, formulas, etc.)

# LOAD DIFFERENT FILE TYPES:

# CSV
df = pd.read_csv('data/file.csv')

# JSON
df = pd.read_json('data/file.json')
# or for simple JSON:
with open('data/config.json', 'r') as f:
    data = json.load(f)

# Excel
df = pd.read_excel('data/file.xlsx')

# Text files
with open('data/file.txt', 'r') as f:
    text = f.read()









# analyzer.py
import pandas as pd
from helpers import calculate_total, format_currency

# Read data
df = pd.read_csv('data/sales.csv')

# Calculate total for each row
totals = []
for index, row in df.iterrows():
    total = calculate_total(row['quantity'], row['price'])
    totals.append(total)

# Add the totals to our data
df['total'] = totals

# Display with formatted totals
print("Sales Data:")
for index, row in df.iterrows():
    formatted_total = format_currency(row['total'])
    print(f"{row['product']}: {formatted_total}")

# Show grand total
grand_total = df['total'].sum()
formatted_grand_total = format_currency(grand_total)
print(f"\nGrand Total: {formatted_grand_total}")

print(grand_total)

"""
How imports work
When you write from helpers import calculate_total:

    Python looks for helpers.py in the same folder
    It runs that file and makes the functions available
    You can now use calculate_total() directly

The file must be in the same folder for this simple import to work
"""


"""
What you’ve accomplished
Look at what you’ve built! You started with a single Python file and now have:

    An organized project structure
    Understanding of how Python finds files
    Code that reads real data and saves results
    Reusable functions in separate files

This is how real Python projects work. You’re ready to build bigger things!
"""





#EXERCISE
"""
Build a small project that extracts data from another file using import
(like I did with helpers) and a csv file. Get creative and make it somewhat how I built
it in here (like using the csv file for data and helpers.py to calculate totals)
Good luck!
"""



import pandas as pd

df = pd.DataFrame({
    "Product": ["Laptop", "Mouse", "Keyboard"],
    "Price": [5000, 250, 400],
    "Quantity": [2, 10, 5]
})

df.to_excel("sales_data.xlsx", index=False)



import zipfile
import os

file = "sales_data.xlsx"

print("Exists:", os.path.exists(file))
print("Size:", os.path.getsize(file), "bytes")
print("Is valid ZIP:", zipfile.is_zipfile(file))

if zipfile.is_zipfile(file):
    with zipfile.ZipFile(file, "r") as z:
        print("\nFiles inside:")
        for name in z.namelist():
            print(name)

# IGNORE THIS MESSAGE AND CODE THAT I AM GOING TO WRITE AFTER, IT IS JUST A GITHUB TEST

print("Hello world")
print("This is a github test")

"UPDATES"

