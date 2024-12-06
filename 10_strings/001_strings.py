# Strings in Python are represented with str type. 
print("Hello World")  # Output: Hello World
print('Hello World')  # Output: Hello World

# Do not mix single and double quotes - this will throw an error:

message = "Hello World"
print(type(message))  # Output: <class 'str'>

# STRING UTILITY METHODS

# 1. Converting to uppercase and lowercase

message = "hello"
print(message.upper())  # Output: HELLO
print(message.lower())  # Output: hello
print("hello".capitalize())  # Output: Hello
print('hello'.capitalize())  # Output: Hello

# 2. Checking lower case, title case, and upper case
print('hello'.islower())  # Output: True
print('Hello'.islower())  # Output: False
print('Hello'.istitle())  # Output: True
print('hello'.istitle())  # Output: False
print('hello'.isupper())  # Output: False
print('Hello'.isupper())  # Output: False
print('HELLO'.isupper())  # Output: True

# 3. Checking if a string is a numeric value
print('123'.isdigit())  # Output: True
print('A23'.isdigit())  # Output: False
print('2 3'.isdigit())  # Output: False
print('23'.isdigit())   # Output: True

# 4. Checking if a string only contains alphabets or alphabets and numerals
print('23'.isalpha())   # Output: False
print('2A'.isalpha())   # Output: False
print('ABC'.isalpha())  # Output: True
print('ABC123'.isalnum())  # Output: True
print('ABC 123'.isalnum())  # Output: False


#5. Checking if a string ends or starts with a specific substring

print('Hello World'.endswith('World'))   # Output: True
print('Hello World'.endswith('ld'))      # Output: True
print('Hello World'.endswith('old'))     # Output: False
print('Hello World'.endswith('Wo'))      # Output: False
print('Hello World'.startswith('Wo'))    # Output: False
print('Hello World'.startswith('He'))    # Output: True
print('Hello World'.startswith('Hell0')) # Output: False
print('Hello World'.startswith('Hello')) # Output: True

# 6. Finding a substring within a string
print('Hello World'.find('Hello'))   # Output: 0
print('Hello World'.find('ello'))    # Output: 1
print('Hello World'.find('Ello'))    # Output: -1
print('Hello World'.find('bello'))   # Output: -1
print('Hello World'.find('Ello'))    # Output: -1

# 7. USING IN KEYWORD TO CHECK IN A STRING

print('Hello' in 'Hello World')   # Output: True
print('ello' in 'Hello World')    # Output: True
print('Ello' in 'Hello World')   # Output: False
print('bello' in 'Hello World')    # Output: False



