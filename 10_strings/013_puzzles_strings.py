data = "Hello World"
print(type(data))  # Output : <class 'str'>
 
char = 'A'
count = 0
for c in "ABRACADABRA":
    if c == char:
        count += 1
print(count)        # Output: 5
 
str1 = "apple"
str2 = "banana"
print(str1 < str2) # Output: True
 
text = "Python "
repeated_text = text * 3
print(repeated_text)    # Output: Python Python Python 
 
str1 = "Hello"
str2 = " World"
result = str1 + str2
print(result)            # Output: Hello World
 
str1 = "Python"
str2 = "Java"
print(len(str1) == len(str2))   # Output: False