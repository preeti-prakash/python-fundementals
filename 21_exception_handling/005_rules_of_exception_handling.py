# when exception occurs -  try, except, else
# try:
#     i = 0
#     j = 10 / i
    
# except ZeroDivisionError as error:
#     print(error)
    
# else:
#     print("else block")
    
# Output:
# division by zero


# when no exception - try, except, else

# try:
#     i = 1
#     j = 10 / i
    
# except ZeroDivisionError as error:
#     print(error)
    
# else:
#     print("else block")
    
# Output:
# else block

# note : else block follows one or more except blocks

# When exception occurs - try , except and finally
try:
    i = 0  
    j = 10 / i
except:
    print("exception")
finally:
    print("Finally")  
    
# Output:
# exception
# Finally

# When exception occurs - try and finally
try:
    i = 0  
    j = 10 / i
finally:
    print("Finally")
    
# Output:

# Error
# Error details
# division by zero