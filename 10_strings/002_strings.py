#  Both type(message[0]) and type(message) return the same type: str.
message = "Hello World"
print(message[0])  # Output: 'H'
print(type(message[0]))  # Output: <class 'str'>
print(type(message))    # Output: <class 'str'>

#  IndexError for Out-of-Range Index
print(message[0])  # Output: 'H'
print(message[1])  # Output: 'e'
print(message[2])  # Output: 'l'
print(message[3])  # Output: 'l'
# This will throw an error:
# print(message[100])  # IndexError: string index out of range


# Iterating Through Characters
for ch in message:
    print(ch, end="")
    
