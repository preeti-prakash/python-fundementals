#  1. Creating and Analyzing a List

marks = [23, 56, 67]

print(sum(marks))
print(max(marks))
print(min(marks))
print(len(marks))


#  2. Adding and Removing Elements

marks.append(76)
print(marks)  # Outputs: [23, 56, 67, 76]
 
marks.insert(2, 60)
print(marks)  # Outputs: [23, 56, 60, 67, 76]

marks.remove(60)
print(marks)  # Outputs: [23, 56, 67, 76]


# 3. Searching and Checking Existence :

print(55 in marks)  # Outputs: False
print(56 in marks)  # Outputs: True
print(marks.index(67))  # Outputs: 2
print(marks)  # Outputs: [23, 56, 67, 76]

# Uncomment the below line to see the error
# print(marks.index(69))


#  4. Iterating Through a List :
for mark in marks:
    print(mark)
# Outputs:
# 23
# 56
# 67
# 76
