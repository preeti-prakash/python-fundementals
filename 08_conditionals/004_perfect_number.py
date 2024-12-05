'''Positive divisors of 6 are 1, 2, 3, and 6. However, when checking if a number is perfect, we exclude the number itself.
So, for our purposes, the divisors are 1, 2, and 3.
When you sum these divisors, you get 1 + 2 + 3 = 6, which is the original number. Therefore, 6 is a perfect number.'''


def is_perfect_number(number):
    if number <= 0:
        return False
    divisor_sum = 0
    for i in range(1, number):
        if(number % i == 0):
            divisor_sum+=i
    if divisor_sum == number:
        return True
    if divisor_sum != number:
        return False

print(is_perfect_number(6))  # Output: True
print(is_perfect_number(28))  # Output: True
print(is_perfect_number(5))  # Output: False