def find_intersection(num1,num2,limit):
    if num1 == 0 or num2 == 0:
        return set()
        
    multiples_num1 = { num for num in range(num1, limit + 1) if num % num1 == 0 }
    # print(multiples_num1)
    multiples_num2 = { num for num in range(num2, limit + 1) if num % num2 == 0 }
    # print(multiples_num2)
    
    result = multiples_num1 & multiples_num2
    return result
    
    
print(find_intersection(4, 6, 30))  # Output: {24,12}
print(find_intersection(3, 5, 20))  # Output: {15}