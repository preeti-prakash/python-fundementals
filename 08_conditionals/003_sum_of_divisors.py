def calculate_sum_of_divisors(number):
    sum=0
    if(number <= 0):
        return sum
    for i in range(1,number+1):
        if(number%i == 0):
            sum+=i
    return sum
print(calculate_sum_of_divisors(6))   # Output: 12
print(calculate_sum_of_divisors(15))  # Output: 24