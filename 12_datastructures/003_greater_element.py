def has_greater_element(numbers, value):
    for num in numbers:
        if num > value:
            return True
    return False
    

print(has_greater_element([10, 20, 30], 15))      # Output: True
print(has_greater_element([5, 7, 8], 10))        # Output: False
print(has_greater_element([], 5))                 # Output: False