def is_anagram(string1, string2):
    sorted_string1 = sorted(string1)
    sorted_string2 = sorted(string2)
    if sorted_string1 == sorted_string2:
        return True
    else:
        return False
    

    
print(is_anagram('listen', 'silent'))  # Output: True
print(is_anagram('hello', 'world'))  # Output: False
