#  COMPARING STRINGS
str1 = "test"
str2 = "test1"
 
print(str1)  # Output: test
print(str2)  # Output: test1


print(str1 == str2)  # Output: False

str2 = "test"
print(str1 == str2)  # Output: True

# When comparing strings, ensure that both the strings are of the same case and contain the same characters in the same order, as the comparison is case-sensitive and character-sensitive.

# To avoid case-sensitivity use .lower() / .upper()


string1 = "Hey"
string2 = "HEY"

print(string1.lower() == string2.lower()) # Output: True

# Remember that strings are compared character by character, based on the ASCII value of the characters

str1 = 'A'
str2 = 'Z'

print(str1 > str2)  # Output: False


# ASCII Values:A to Z  -> 65 - 90
print(ord('A'))
print(ord('Z'))

# ASCII Values:a to z  -> 97 - 122
print(ord('a'))
print(ord('Z'))


print('a' > 'A')   # Output: True


