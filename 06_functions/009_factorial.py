def calculate_factorial(n):
    factorial=1
    for i in range(n,0,-1):
        factorial=factorial*i
    return factorial
    
print(calculate_factorial(5))