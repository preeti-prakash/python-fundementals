# use the * operator to unpack elements from a list and pass them as arguments to a function.


# UNPACKING ELEMENTS FROM A LIST
def print_values_of_list(num1, num2, num3):
    print(num1)
    print(num2)
    print(num3)
 
numbers = [10, 20, 30]
print_values_of_list(*numbers)
# print_values_of_list(10,20,30)


# UNPACKING ELEMENTS FROM A SET
def print_values_of_set(num1, num2,num3):
    print(num1)
    print(num2)
    print(num3)

scores = {35, 46, 68}
print_values_of_set(*scores)
# print_values_of_set(35, 68, 46)