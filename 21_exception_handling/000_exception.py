import builtins
 
# List all names in builtins module
builtin_names = dir(builtins)
 
# Print first 100 names as an example
print("First 100 built-in names:", builtin_names[:100])
 
# Show help for one of the exceptions, e.g., ZeroDivisionError
help(builtins.ZeroDivisionError)