# Define a class with attributes
class MyClass:
    x = 0
    y = 0

# Create an instance of the class
my_object = MyClass()

# Access an attribute
print(my_object.x) # 0

# Set an attribute
my_object.y = 10
print(my_object.y) # 10

# We always name classes in PascalCase
# This is just a style convention that most people follow to make easier to read code
# MyClass       YES
# myClass       NO
# my_class      NO