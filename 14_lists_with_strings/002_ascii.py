# The American Standard Code for Information Interchange (ASCII)
# 'A' corresponds to 65
# 'a' corresponds to 97
# '1' corresponds to 49


# ord() - ASCII values of characters can be found using the ord() function.
ascii_value_A = ord('A')
print(ascii_value_A)  # Outputs: 65


# GETTING THE NEXT ASCII VALUE
char = 'C'
next_ascii_value = ord(char) + 1
print(f"The next ASCII value after {char} is: {next_ascii_value}")

# Output:
# The next ASCII value after C is: 68


# CONVERTING ASCII VALUE TO CHARACTER
ascii_val = 68
character = chr(ascii_val)
print(f"The character representation of ASCII value {ascii_val} is: {character}")

# Output:
# The character representation of ASCII value 68 is: D


def next_character(char):
    next_ascii_val = ord(char)+1
    next_character = chr(next_ascii_val)
    return next_character

char = 'Y'
print(f"The given character is {char}")
print(f"The next character is: {next_character(char)}")

# Output
# The given character is Y
# The next character is: Z