# Keywords are reserved words that have special meanings and are part of the language's syntax.

# for = 5 #SyntaxError: invalid syntax

for i in range(1, 11):
    print(i)
    
def add_numbers(a, b):
    return a + b
    
# Keywords in above code
# def: Used to define a new function

# return: Used inside a function to exit the function and return a value to the caller.



# Other keywords include:

# if, else, elif: Used for conditional execution of code.

# and, or, not: Used for logical operations.

# True, False: Represent boolean values, which can be used in conditional expressions.

# None: Represents the absence of a value or a null value.

def my_function_which_does_not_return_anything():
    pass
 
print(my_function_which_does_not_return_anything()) #prints None