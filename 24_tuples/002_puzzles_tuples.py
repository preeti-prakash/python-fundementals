my_tuple = (4, 5, 6, 7, 8)
print(len(my_tuple))
# Output: 5
 
my_tuple = (100, 200, 300)
a, b, c = my_tuple
print(b)
# Output: 200
 
tuple_1 = (1, 2, 3)
tuple_2 = (4, 5, 6)
result = tuple_1 + tuple_2
print(result)
# Output: (1,2,3,4,5,6)
 
def my_function(x, y):
    return x + y, x - y
result = my_function(10, 5)
print(result)
# Output: (15,5)
 
nested_tuple = ((1, 2), (3, 4), (5, 6)) #Nested Tuples
print(nested_tuple[1][0])
# Output: 3
 
my_tuple = (10, 20, 30, 40, 50) # Tuple Slicing
print(my_tuple[-1])
print(my_tuple[1:4])
print(my_tuple[1:-1])
# Output:
# 50
# (20,30,40)
# (20,30,40)
 
 
my_tuple = (10, 20, 30, 40, 10)
print(my_tuple.count(10))
print(my_tuple.index(30))
# Output:
# 2
# 2
 
a, b, c = 10, 20, 30 # Tuple Packing and Unpacking
my_tuple = a, b, c
x, y, z = my_tuple
print(x + y + z)
# Output: 60
