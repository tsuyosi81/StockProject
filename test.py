# # NOTE Inheritance
# # Inheritance allows us to define a class that inherits all the methods and properties from another class.

# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)

# # Use the Person class to create an object, and then execute the printname method:

# x = Person("John", "Doe")
# x.printname()

# import mymodule

# mymodule.greeting("Jonathan")

# a = mymodule.person["age"]
# print(a)

# NOTE There are several built-in modules in Python, which you can import whenever you like.

# Example:
# Import and use the platform module:

import platform

# x = platform.system()
# print(x)

# There is a build-in function to list all the function names(or variable names) in a module. The "dir()" function:

# Example
# List all the defined names belonging to the platform module:

# x = dir(platform)
# print(x)
# You can choose to import only parts from a module, bu using the from keyword.

# Example:
# The module name mymodule has one function and one dictionary:

# from mymodule import person

# print(person["age"])