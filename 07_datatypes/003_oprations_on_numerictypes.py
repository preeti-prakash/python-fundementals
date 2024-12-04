i=1
i=i+1
print(i) #output: 2


#shorthand operators
i+=1
print(i) #Output:3
# i++
#python does not support ++ --


i-=1
print(i)  #Output:2

i/=1
print(i) #Output:2.0

i*=2
print(i) #Output: 4.0

# Integer Division
number1=5
number2=2
print(number1 / number2) #Output: 2.5
print(number1//number2) #Output:2  , return the integer part of the division, type is int

# exponentiation
print(5 ** 3)   #Output: 125
print(pow(5,3))   #Output: 125

# Dynamic Typing - The type of variable can change during the excecution of a program
i=2
print(type(i))  #Output: <class 'int'>
i=i/2.0
print(i) #Output: <class 'float'>

# Type Conversion - int(), float(), round()

print(int(5.6))  #Output: 5

print(float(5)) #Output: 5.0

print(round(5.6)) #Output: 6
print(round(5.4)) #Output: 5
print(round(5.5)) #Output: 6
print(round(5.67,1)) #Output: 5.7
print(round(5.678,2)) #Output: 5.68
