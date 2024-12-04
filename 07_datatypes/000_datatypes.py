# numbers are represented by two fundamental data types: integers and floating-point numbers, referred to as int and float

# INTEGERS - whole number, without a fraction
print(type(5))  # Output: <class 'int'>

# FLOATING POINT NUMBERS - represent real numbers
print(type(2.5))  # Output: <class 'float'>
print(type(5/2))  # Output: <class 'float'>
print(4/2)  # Output: 2.0

# a division operation always returns a float, even if the result is a whole number.

# OPERATIONS
value1 = 4.5
value2 = 3.2
print(value1 + value2)  # Output: 7.7
print(value1 - value2)  # Output: 1.2999999999999998  , floating point numbers cannot always precisely represent real numbers
print(value1 / value2)  # Output: 1.40625
print(value1 % value2)  # Output: 1.2999999999999998

# Operations can also be performed between int and float. The result of an operation between an int and a float is always a float.
i = 10
print(i + value1)  # Output: 14.5
print(i - value1)  # Output: 5.5
print(i / value1)  # Output: 2.2222222222222223
