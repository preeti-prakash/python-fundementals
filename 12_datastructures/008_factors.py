def find_factors(number):
    factors = []
    for num in range(1,number+1):
        if number % num == 0:
            factors.append(num)
    return factors

print(find_factors(12))  # Output: [1, 2, 3, 4, 6, 12]
print(find_factors(15))  # Output: [1, 3, 5, 15]
print(find_factors(7))   # Output: [1, 7]
