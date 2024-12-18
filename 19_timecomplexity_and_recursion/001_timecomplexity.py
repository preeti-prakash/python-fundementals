# Time complexity - the runtime of an algorithm grows as the size of the input grows.

# CONSTANT TIME COMPLEXITY - O(1)

def get_first_element(arr):
    return arr[0]
 
# Try it out
print(get_first_element([1, 2, 3]))  # Output: 1


# LINEAR TIME COMPLEXITY - O(n)
def find_max(arr):
 
    max_val = arr[0]
 
    for num in arr:
        if num > max_val:
            max_val = num
 
    return max_val
 
 
 
 
print(find_max([1, 2, 3]))  # Output: 3



# QUADRATIC TIME COMPLEXITY - O(n^2)

def print_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)
 
# Try it out
print_pairs([1, 2, 3])
# Output: 
# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3
# 3 1
# 3 2
# 3 3