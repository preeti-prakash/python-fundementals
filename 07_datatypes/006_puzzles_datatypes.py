x = 5
y = 3.5
z = True
print(type(x))
print(type(y))
print(type(z))
 
a = 5
b = 2.5
result = a + b
print(result)
 
c = True
d = False
result = c + d
print(result)  #Output: 1 , true is 1, false is 0
 
num_int = 7
num_float = float(num_int)
print(num_float)    #Output: 7.0
 
num_float = 3.14
num_int = int(num_float)
print(num_int)      #Output:3
 
is_raining = True
int_value = int(is_raining)
print(int_value)    #Output:1
 
str_num = "123"
num = int(str_num)
print(num+3)          #Output:126
 
str_num = "3.14"
num = float(str_num)
print(num)          #Output:3.14
 
num = 10
str_num = str(num)
print(str_num)          #Output:10
 
is_true = True
str_bool = str(is_true)
print(str_bool)         #Output:True
 
print(bool('True'))         #Output:True
print(bool('true'))         #Output:True
print(bool('false'))        #Output:True, boolean of false string also returns true
print(bool(''))             #Output:False  , boolean for an empty string returns fasle