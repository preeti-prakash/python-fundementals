def rotate_strings(strings, n):
    if not strings or n == 0:
        return strings
    for number in range(n):
        last_element = strings[-1]
        for i in range(len(strings)-1, 0, -1):
            strings[i] = strings[i-1]
        strings[0]=last_element
    return strings
    

print(rotate_strings(['a', 'b', 'c'], 2))      # Output: ['b', 'c', 'a']
print(rotate_strings(['apple', 'banana', 'cherry', 'date'], 1))   # Output: ['date', 'apple', 'banana', 'cherry']
print(rotate_strings(['hello', 'world'], 3))    # Output: ['world', 'hello']