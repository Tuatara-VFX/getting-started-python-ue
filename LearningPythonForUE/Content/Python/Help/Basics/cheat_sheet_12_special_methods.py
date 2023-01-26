# Define a class with special methods
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "MyClass({}, {})".format(self.x, self.y)

# Create an instance of the class
# At this moment, __init__ is called
my_object = MyClass(1, 2) 

# Use special methods
# At this moment, __str__ is called
print(my_object) # MyClass(1, 2)
