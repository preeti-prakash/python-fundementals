def reverse_list(lst):
    start = 0
    end = len(lst) - 1
    
    # Use two pointers to swap elements
    while start < end:
        # Swap elements at start and end
        lst[start], lst[end] = lst[end], lst[start]
        # Move the pointers
        start += 1
        end -= 1
    
    return lst

# Test cases
print(reverse_list([10, 20, 30]))      # Output: [30, 20, 10]
print(reverse_list([5, 15, 25, 35]))   # Output: [35, 25, 15, 5]
print(reverse_list([1]))               # Output: [1]
