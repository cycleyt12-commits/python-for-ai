"""
Classes

Create your own data types
​
What is object-oriented programming?
Object-oriented programming (OOP) is a way to organize code by grouping related data and functions together. Instead of having separate variables and functions scattered around, you bundle them into objects. Think of it like organizing a toolbox:

    Without OOP: Tools scattered everywhere
    With OOP: Tools organized in labeled compartments

 """


"""
What is a class?
A class is a blueprint for creating objects. It defines:

    Attributes: What data the object stores
    Methods: What the object can do

"""
# Without classes - data and functions separate
name = "OpenAI"
model = "gpt-4o-mini"

def generate_response(prompt):
    # Process prompt...
    return response

# With classes - everything bundled together
class OpenAIClient:
    def __init__(self, name, model):
        self.name = name
        self.model = model
    
    def generate_response(self, prompt):
        # Process prompt...
        return response

# CLASSES help you write more understandable programs as they grow. Here's the typical progression of a Python Developer
make_api_call = "another example"
# 1. Single file scripts (where you started)
# everything.py - All code in one file
api_key = "sk-..."
prompt = "Explain Python"
response = make_api_call(api_key, prompt)
print(response)

# 2. Functions (where you are now):

def setup_api(key):
    return{"key":key, "base_url":"https://api.openai.com"}

def generate_response(api_config, prompt):
    #Make API call
    return response

api = setup_api("sk-...")
result = generate_response(api, "Explain Python")

# 3. Multiple files (getting organized)

#api_utils.py
def setup_api(key):
    return{"key":key,"base_url":"https://api.openai.com"}

#main.py
from api_utils import setup_api
api = setup_api("sk-...")

# 4. Classes (where we are now)

#client.py

class OpenAIClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openai.com"

def generate(self, prompt):
    # ALL logic encapsulated here
    return response

#main.py
from client import OpenAIClient
client = OpenAIClient("sk-...")
response = client.generate("Explain Python")