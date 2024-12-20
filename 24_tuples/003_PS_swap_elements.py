def swap_elements(input_tuple):
    return input_tuple[-1], *input_tuple[1:-1],input_tuple[0]
    
    
print(swap_elements((1, 2, 3, 4)))          # Output: (4, 2, 3, 1)
print(swap_elements((7, 14, 21, 28)))      # Output: (28, 14, 21, 7)
print(swap_elements(('apple', 'banana', 'cherry'))) # Output: ('cherry', 'banana', 'apple')
print(swap_elements((5, 10)))               # Output: (10, 5)
