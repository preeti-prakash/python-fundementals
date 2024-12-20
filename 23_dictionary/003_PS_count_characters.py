def count_characters(str):
    char_occurances = {}
    for char in str:
        if char in char_occurances:
            char_occurances[char] += 1
        else:
            char_occurances[char] = 1
    return char_occurances
    
print(count_characters("apple"))
# {'a': 1, 'p': 2, 'l': 1, 'e': 1}