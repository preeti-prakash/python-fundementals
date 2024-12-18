# BINARY SEARCH ALGORITHM

def binary_search(lst, target):
    
    low = 0
    high = len(lst) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return None


result = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 9)
 
print("Found at index:", result)

# Output - Found at index: 8
# Time complexity: O(log n) .