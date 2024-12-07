#  1. Storing Multiple Values Without Data Structures :
mark1 = 45
mark2 = 54
mark3 = 80


# You can calculate the sum and average as follows:

print(mark1 + mark2 + mark3) # Outputs: 179
print((mark1 + mark2 + mark3)/3) # Outputs: 59.666666666666664


# If a new student joins:

mark4 = 43
print((mark1 + mark2 + mark3 + mark4)/3) # Outputs: 74.0
print((mark1 + mark2 + mark3 + mark4)/4) # Outputs: 55.5


#  the change in the formula? This is not efficient.


# Using Lists to Store Multiple Values :
marks = [45, 54, 80]
print(sum(marks)) # Outputs: 179
print(sum(marks)/len(marks)) # Outputs: 59.666666666666664


# new student joins:

marks.append(43)
print(sum(marks)/len(marks)) # Outputs: 55.5
print(type(marks)) # Outputs: <class 'list'>
