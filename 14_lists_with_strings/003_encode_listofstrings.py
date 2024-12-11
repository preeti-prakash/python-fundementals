def encode_strings(strings):
    result = []
    for string in strings:
        result_string = ''
        for letter in string:
            if 'a' <= letter <= 'z':  # Handle lowercase letters
                encoded_letter = 'a' if letter == 'z' else chr(ord(letter) + 1)
            elif 'A' <= letter <= 'Z':  # Handle uppercase letters
                encoded_letter = 'A' if letter == 'Z' else chr(ord(letter) + 1)
            else:  # Non-alphabetic characters remain unchanged
                encoded_letter = letter
            result_string += encoded_letter
        result.append(result_string)
    return result

# Test cases
print(encode_strings(['abc', 'def']))  # Output: ['bcd', 'efg']
print(encode_strings(['hello', 'WORLD']))  # Output: ['ifmmp', 'XPSME']
