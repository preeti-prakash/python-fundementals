# Variable Arguments

# 1. USING *args
# *args  - variable number of positional arguments to a function.


# FINDING MAXIMUM
def find_max(*args):
    if not args:
        return None
    max_value = args[0]
    for num in args:
        if num > max_value:
            max_value = num
    return max_value
result = find_max(3, 8, 2, 10, 5)
print(result)  # Outputs: 10



# COMBINING STRINGS
def combine_strings(*args):
    return ' '.join(args)
result = combine_strings('Hello', 'world', 'from', 'Python')
print(result)  # Outputs: Hello world from Python