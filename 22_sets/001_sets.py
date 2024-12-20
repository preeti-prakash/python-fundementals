#  A set -  does not contain duplicates.

#  1. create a set:
numbers_set = {1, 2, 3, 4}

# create a set from a list of numbers 
numbers = [1,2,3,2,1]
numbers_set = set(numbers)
print(numbers_set)  # Output: {1, 2, 3}


# 3. Adding to a set
numbers_set.add(3)
print(numbers_set)  # Output: {1, 2, 3}

numbers_set.add(0)

# 4. alreasy existed element in the set, when added remains unchanged
numbers_set.add(2)
print(numbers_set)  # Output: {0,1, 2, 3}


# 5. Removing an element from the set
numbers_set.remove(0)
print(numbers_set)  # Output: {1, 2, 3}


# 6. Check existence of a number in the set
print(1 in numbers_set)  # Output: True
print(5 in numbers_set)  # Output: False

#  7. Perform aggregate operations on a set
print(min(numbers_set))  # Output: 1
print(max(numbers_set))  # Output: 3
print(sum(numbers_set))  # Output: 6
print(len(numbers_set))  # Output: 3

#  Union, Inteserction and Difference
numbers_1_to_5_set = set(range(1,6))
print(numbers_1_to_5_set)  # Output: {1, 2, 3, 4, 5}
numbers_4_to_10_set = set(range(4,11))
print(numbers_4_to_10_set)  # Output: {4, 5, 6, 7, 8, 9, 10}

# Union

print(numbers_1_to_5_set | numbers_4_to_10_set)   #Output: {1,2,3,4,5,6,7,8,9,10}


# Intersection
print( numbers_1_to_5_set & numbers_4_to_10_set)  #Output: {4,5}

# Difference
print( numbers_1_to_5_set - numbers_4_to_10_set) #Output: {1,2,3}
print( numbers_4_to_10_set - numbers_1_to_5_set) #Output: {6,7,8,9,10}

