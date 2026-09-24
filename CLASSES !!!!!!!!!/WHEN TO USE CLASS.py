"""
When to use classes

Best practices and guidelines
​
Programming paradigms
Python supports multiple programming styles. The two main ones are: Functional programming - Using functions to transform data:
"""

#Functional programming - Using functions to transform data:

# Functions operate on data
def clean_text(text):
    return text.strip().lower()

def remove_punctuation(text):
    return text.replace(".", "").replace(",", "")

# Chain functions together
result = remove_punctuation(clean_text("  Hello, World.  "))

# Object-oriented programming - Using classes to bundle data and behavior:

# Class bundles data and methods
class TextProcessor:
    def __init__(self, text):
        self.text = text
    
    def clean(self):
        self.text = self.text.strip().lower()
        return self
    
    def remove_punctuation(self):
        self.text = self.text.replace(".", "").replace(",", "")
        return self

# Chain methods on object
processor = TextProcessor(text="  Hello, World.  ")
result = processor.clean().remove_punctuation().text

"""
Both approaches achieve the same result! Classes don’t unlock new features - they’re just a different way to organize your code. Choose based on what makes your code clearer.
"""

"""
When to use classes
Use classes when you need to:

    Keep track of state between operations
    Group related data and functions together
    Create multiple instances with similar behavior
    Model real-world objects or concepts

​
When to use functions
Use functions when you have:

    Simple transformations (input → output)
    Stateless operations
    One-off calculations
    Small scripts

Start with functions. They’re simpler and often sufficient. Only add classes when you find yourself passing the same data between multiple functions or when you need to maintain state.
​
Common pitfalls
Over-engineering: Don’t create classes for simple operations. A class with one method is usually better as a function. God objects: Classes that do too many things. Keep classes focused on a single responsibility. Static method classes: If all methods are static, you probably want a module with functions instead.

"""