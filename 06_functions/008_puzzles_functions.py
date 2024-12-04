def method_to_understand_indentation():
    for i in range(1,11):
        print(i)
method_to_understand_indentation()

def method_to_understand_indentation1():
    for i in range(1,11):
        print(i)
    print(5)        #out of the loop
method_to_understand_indentation1()

def method_to_understand_indentation2():
    for i in range(1,11):
        print(i)
        print(5) #part of the for loop
method_to_understand_indentation2()

def my_function():
    pass
my_function()

def my_function1():pass
my_function1()

def print_hello_world(no_of_times):
    for i in range(1,no_of_times):pass  #do nothing
print_hello_world(10)

#calling function within a function

def add_two_numbers(a, b):
    return a + b
def multiply_result(x, y):
    result = add_two_numbers(x, y)
    return result * 2
print(multiply_result(1, 2))
 
def greet_user(name="User"):
    print(f"Hello, {name}!")
greet_user()
greet_user("Alice")
greet_user('Alice')
 
def print_string(str="Hello World", no_of_times=5):
     for i in range(1,no_of_times+1):    #concatenation
        print(str)
print_string()
print_string(no_of_times=6)
print_string(7, 8)
print_string(7.5, 8)
# print_string(7.5, "eight") #string cannot be accepted as a number when concatenating
