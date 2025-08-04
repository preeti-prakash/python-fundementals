# Tuples - once a tuple is created, you cannot change its content.

# CREATING AND RETURNING A TUPLE
def create_my_tuple():
    return 'preeti', 1996, 'India'


my_tuple = create_my_tuple()
print(my_tuple)
print(type(my_tuple))

# Output:
# ('preeti', 1996, 'India')
# <class 'tuple'>


# DESTRUCTURING A TUPLE
name, year, country = my_tuple
print(name)       # Outputs: preeti
print(year)       # Outputs: 1996
print(country)    # Outputs: India
# Note - the variables on the LHS = the values in RHS

# TUPLE OPERATIONS

print(len(my_tuple))  # Outputs: 3
print(my_tuple[0])    # Outputs: preeti
print(my_tuple[1])    # Outputs: 1996
print(my_tuple[2])    # Outputs: India
