# UNDERSTANDING DATA TYPES OF BASIC VALUES
# Python treats even basic data types like integers, booleans, strings, and floats as objects.
print(type(5))  # Output: <class 'int'>
print(type(True))  # Output: <class 'bool'>
print(type('Hello'))  # Output: <class 'str'>
print(type(5.5))  # Output: <class 'float'>

# EVEN A FUNCTION IS AN OBJECT

def do_something():
    print("something")
 
# Functions as objects
print(do_something)  # Output: <function do_something at some_memory_address>
 
# Assigning functions to variables
test = do_something
test()  # Output: something