# Define a function
# name is an argument of the function
def greet(name):
    print("Hello " + name)

# Call a function
greet("John")

# Return a value from a function
def square(number):
    return number ** 2

# Store the return value in a variable
result = square(10)
print(result)

# Function with multiple parameters
def add(a, b):
    return a + b

result = add(10, 20)
print(result)

# Function with default parameters
def greet(name, greeting="Hello"):
    print(greeting + " " + name)

greet("John")
greet("Jane", "Hi")