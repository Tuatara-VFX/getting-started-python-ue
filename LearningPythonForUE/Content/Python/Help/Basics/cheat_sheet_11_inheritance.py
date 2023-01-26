# Define a base class
class MyBaseClass:
    def my_method(self):
        print("Hello from MyBaseClass!")

# Define a derived class
class MyDerivedClass(MyBaseClass):
    pass

# Create an instance of the derived class
my_object = MyDerivedClass()

# Call a method from the base class
my_object.my_method() # Hello from MyBaseClass!