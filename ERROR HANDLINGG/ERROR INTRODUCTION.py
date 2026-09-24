# Syntax errors

# Missing colon
x = 10
if x > 5:  # SyntaxError
    print("Big number")

#Runtime errors.
# Division by zero
result = 10 / 0  # ZeroDivisionError

# Variable doesn't exist
#print(score)  # NameError

# Wrong type
"hello" + 5  # TypeError

"hello" + "hi"  # Will work

#Why handle errors

# This will crash if the file doesn't exist
with open('data.txt', 'r') as f:
    content = f.read()
print("Done!")  # Never reaches here if file missing

#Now program that handles the error

# This keeps running even if file doesn't exist
try:
    with open('data.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("Could not find data.txt")
    content = "default data"
print("Done!")  # Always reaches here