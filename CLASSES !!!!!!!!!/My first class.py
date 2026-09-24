"""

Your first class

Create a simple class
​
How classes work
Working with classes follows a simple pattern:

    Define the class - Create a blueprint with the class keyword
    Add an __init__ method - Set up initial data when objects are created
    Create instances - Make actual objects from your class
    Access the data - Use the attributes you defined

Let’s go through each step to build your first class.

"""

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

class Cat:
    def __init__(self, breed, gender):
        self.breed = breed
        self.gender = gender

Max = Dog(name = "Max", breed="Pitbull")

Max.breed

class Dog:
    def __init__(self, name):
        self.name = name #self.name belongs to this speicfic dog

#Using positional argument

dog1 = Dog(name = "Buddy")

dog2 = Dog(name = "Jerry")

print(dog1.name)
print(dog2.name)

#Real world example in AI agents

class APIConfig:
    def __init__(self, api_key, model = "gpt-6-astra", max_tokens = 100):
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens
        self.base_url = "https://api.openai.com/v1"

# Create different configurations


dev_config = APIConfig(api_key = "sk-dev-key", max_tokens = 50)

prod_config = APIConfig("sk-dev-key",model = "gpt-4",  max_tokens = 1000)

# Access the configuration
print(dev_config.model)  #gpt-6-astra
print(prod_config.model) #gpt-4
print(prod_config.max_tokens) #1000
print(dev_config.max_tokens)  #50

# Class vs instance

# APIConfig is the class
# config1 and config2 are instances
config1 = APIConfig(api_key="key1", max_tokens=50)
config2 = APIConfig(api_key="key2", max_tokens=200)

# Each instance has its own data
print(config1.max_tokens)  # 50
print(config2.max_tokens)  # 200

# Changing one doesn't affect the other
config1.max_tokens = 75
print(config1.max_tokens)  # 75
print(config2.max_tokens)  # 200 (unchanged)

