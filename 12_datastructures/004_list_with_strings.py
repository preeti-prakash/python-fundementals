#  1. CREATING A LIST

animals = ['Cat', 'Dog', 'Elephant']
print(animals)
# Output: ['Cat', 'Dog', 'Elephant']


#  2. FINDING LENGTH OF A LIST

print(len(animals))
# Output: 3


#  3. ACCESSING LIST ELEMENTS

print(animals[2])
# Output: Elephant
 
print(animals[1])
# Output: Dog
 
print(animals[0])
# Output: Cat


#  4. HANDLING LIST ERRORS
# This line will cause an error if executed:
# print(animals[4])
# Expected Output: IndexError: list index out of range


#  5. DELETING AN ELEMENT FROM THE LIST
del animals[2]
print(animals)
# Output after deletion: ['Cat', 'Dog']


#  6. EXTENDING A LIST
animals.extend(['Giraffe', 'Horse'])
print(animals)
# Output: ['Cat', 'Dog', 'Giraffe', 'Horse']
 
animals += ['Lion', 'Monkey']
print(animals)
# Output: ['Cat', 'Dog', 'Giraffe', 'Horse', 'Lion', 'Monkey']

#  7. APPENDING TO A LIST
animals.append(10)
print(animals)
# Output: ['Cat', 'Dog', 'Giraffe', 'Horse', 'Lion', 'Monkey', 10]


#  8. List support different data try:
mixed_list = [1, "Python", 3.14, ["another", "list"]]
print(mixed_list[3])    #Output ["another","list"]


#  9. Other methods in list
numbers = [4, 2, 9, 1]
numbers.sort()
print(numbers)  #Output - [1, 2, 4, 9]
numbers.reverse()
print(numbers)      #Output - [9, 4, 2, 1]
