"""
Common errors

Understand Python’s error types
​
Errors you’ll encounter
Here are the most common Python errors and how to fix them. Understanding these will save you hours of debugging.
​
FileNotFoundError
Happens when a file doesn’t exist:

# This fails if file doesn't exist
with open('missing.txt', 'r') as f:
    content = f.read()
"""
#Fix:

import os

# Check first
if os.path.exists('data.txt'):
    with open('data.txt', 'r') as f:
        content = f.read()
else:
    print("File not found")

# Or use try-except
try:
    with open('data.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    content = ""  # Default value


ValueError
#Happens when a value is wrong type or format:

# These cause ValueError
int("hello")        # Can't convert to number
int("12.5")         # int() doesn't accept decimals
list.remove("x")    # Item not in list

#Fix:

# Validate user input
try:
    age = int(input("Age: "))
except ValueError:
    print("Please enter a number")

# Convert carefully
float_str = "12.5"
number = int(float(float_str))  # Convert to float first


KeyError
#Happens when a dictionary key doesn’t exist:

user = {"name": "Alice", "age": 25}
print(user["email"])  # KeyError - no email key

#Fix:

# Check if key exists
if "email" in user:
    print(user["email"])

# Use get() with default
email = user.get("email", "no-email@example.com")

# Or handle the error
try:
    print(user["email"])
except KeyError:
    print("Email not found")


IndexError
#Happens when accessing invalid list position:

numbers = [1, 2, 3]
print(numbers[5])  # IndexError - only 3 items

#Fix:

# Check length first
if len(numbers) > 5:
    print(numbers[5])

# Use negative indexing carefully
last_item = numbers[-1] if numbers else None

# Handle the error
try:
    print(numbers[5])
except IndexError:
    print("List too short")


TypeError
#Happens when operations use wrong types:

# These cause TypeError
"hello" + 5            # Can't add string and number
len(42)                # Numbers don't have length
int([1, 2, 3])         # Can't convert list to int

#Fix:

# Convert types explicitly
"hello" + str(5)       # "hello5"
str(42)                # "42"

# Check type first
value = "IGNORE THIS"
if isinstance(value, str):
    print(len(value))

AttributeError
#Happens when accessing non-existent attributes:

text = "hello"
text.append("!")  # AttributeError - strings don't have append

#Fix:

# Use correct methods
text = "hello"
text = text + "!"  # Strings are immutable

# Check if attribute exists
obj = 10
item = "This doesnt matter it's just example"
if hasattr(obj, 'append'):
    obj.append(item)
"""
Error messages are your friends! They tell you:

    What went wrong (error type)
    Where it happened (file and line number)
    Why it happened (error message)

Always read the full error message before trying to fix it.
​
Reading error messages
Python error messages show a “traceback”:

Traceback (most recent call last):
  File "script.py", line 5, in <module>
    result = 10 / 0
ZeroDivisionError: division by zero
"""