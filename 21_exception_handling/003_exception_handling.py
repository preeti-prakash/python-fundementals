#  SPECIFIC EXCEPTIONS
try:
    10/0
except TypeError:
    print("TypeError")
except ZeroDivisionError:
    print("ZeroDivisionError")
 
print("End")

# Output
# ZeroDivisionError
# End


#  INVALID BASE CLASSES IN EXCEPTION
try:
    10/0
except object:
    print("ZeroDivisionError")
# catching classes that do not inherit from BaseException is not allowed
print("End")

# CATCHING ALL EXCEPTIONS
try:
    10/0
except Exception:
    print("Exception")
    
# Output
# Exception


# CATCHING MULTIPLE EXCEPTIONS IN A SINGLE BLOCK
try:
    sum([1, '1'])
except (ZeroDivisionError, TypeError):
    print("Exception")

# Output
# Exception

# ACCESSING EXCEPTION DETAILS
try:
    sum([1, '1'])
except TypeError as error:
    print(error)


# Output
# unsupported operand type(s) for +: 'int' and 'str'
