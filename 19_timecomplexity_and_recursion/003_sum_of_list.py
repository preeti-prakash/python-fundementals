# Sum of a List using Recursion in Python

def sum_of_list(lst, n):
    
    if n== 0:
        return 0
        
    return lst[n-1] + sum_of_list(lst,n-1)
    
    
result = sum_of_list([1,2,3,4,5],5)
print("sum of list is:", result)


# Output: sum of list is: 15