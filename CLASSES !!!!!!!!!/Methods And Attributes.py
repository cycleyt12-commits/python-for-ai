"""
Methods and attributes
(methods are basically functions but they're called methods in classes)
Add functionality to classes
​
Attributes: storing data
Attributes are variables that belong to an object. There are two types:
"""
# Instance attributes (unique to each object)

class APIClient:
    def __init__(self, api_key, base_url):
        self.api_key = api_key      # Each client has its own key
        self.base_url = base_url    # Each client has its own URL
        self.request_count = 0      # Track requests per client

# Creating instances with named arguments
client1 = APIClient(api_key="key1", base_url="https://api1.com")
client2 = APIClient(api_key="key2", base_url="https://api2.com")

# Class attributes (shared by all objects):

class APIClient2:
    version = "1.0"           #Same for all clients
    max_retries = 3           # Same for all clients

# However, when we start using a function (def __init__...), the class becomes an instance (unique to each client)

"""
Methods: adding behavior
Methods are functions that belong to a class. They always have self as the first parameter, but you don’t pass it when calling:
"""
class DataValidator:
    def __init__(self):
        self.errors = []
    
    def validate_email(self, email):
        if "@" not in email:
            self.errors.append(f"Invalid email: {email}")
            return False
        return True
    
    def validate_age(self, age):
        if age < 0 or age > 150:
            self.errors.append(f"Invalid age: {age}")
            return False
        return True
    
    def get_errors(self):
        return self.errors

# Use the validator
validator = DataValidator()

# Notice: we don't pass self, just the email
validator.validate_email(email="bad-email")
validator.validate_age(age=200)

# Or using positional arguments
validator.validate_email("another-bad-email")
validator.validate_age(150)
print(validator.get_errors())
# ['Invalid email: bad-email', 'Invalid age: 200', 'Invalid email: another-bad-email']
#--------------------------------------------------------------------------------------




# PROJECT BY ME

tally_spreadsheet = {
    "email":{"shapetru1108@gmail.com", "danvictor72@gmail.com", "ruxidavid3109@gmail.com"}
}

class Data_Analyze:
    def __init__(self):
        self.errors = []

    def validate_data(self, email):
        if email in tally_spreadsheet:
            print(f"Success! I did find {email} in my spreadsheet. ")
            return False
        return True
    def validate_age2(self, age):
        if age < 18 or age > 100:
            print(f"Age {age} is invalid. Please insert a valid age")
            return False
        else:
            print(f"Age {age} is valid. You are good to go!")
            return True
        return True

phone_number = "+40 786 293 100"
class Qualified_Lead:
    def __init__(self, budget):
        self.budget = budget
    def check_qualify(self, budget):
        if budget >= 2000 and budget < 100000:
            print(f"You are a qualified lead. Contact me whenever you can at {phone_number} to get in touch and help you build your personal AI agent!")
        else:
            print("Budget must be more than $2000 to be a qualified lead. Sorry.")

analyzet = Data_Analyze()
analyzet.validate_data(email="bad-email")
analyzet.validate_age2(age=200)

print(analyzet.get_errors())

qualify = Qualified_Lead()
qualify.check_qualify(budget = int(input("Enter your budget (only the number): ")))

print(qualify.get_errors())

#-------------------------------------------------------------------------------------------------

# BY DAVE

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("Bark!!!")

jerry = Dog(name = "jerry")

jerry.name
jerry.bark()


