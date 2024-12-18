def binary_search_recursive(lst, target, low = 0, high = None):

    if high is None:
        high = len(lst) - 1

    if low > high:
        return None
    
    mid = (low + high ) // 2
    if lst[mid] == target:
        return mid
    
    elif lst[mid] < target:
        return binary_search_recursive(lst,target,mid+1,high)
    
    else:
        return binary_search_recursive(lst,target, low, mid-1)
    
result = binary_search_recursive([1, 2, 3, 4, 5, 6, 7, 8, 9], 9)
 
print("Found at index:", result)

# Output - Found at index: 8
# Time complexity: O(log n)