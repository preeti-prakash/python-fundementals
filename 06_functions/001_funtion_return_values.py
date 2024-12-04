# function can have multiple parameters
def product_of_two_numbers(a,b):   #function has no return value
    print(a*b)
product_of_two_numbers(2,3) #function call: prints 6


product = product_of_two_numbers(1,2) #prints 2
print(product) #prints None : function has no return value 

#function with return values

maximum = max(1,2,3,4,5) #built-in function returning value
print(maximum) #returns 5


#function retrning  a value
def product_of_three_numbers(a,b,c):
    product = a*b*c
    return product

print(product_of_three_numbers(1,2,3)) # prints 6
productOfThree = product_of_three_numbers(1,2,3) #function call that returns the product result to the variable productOfThree
print(productOfThree) #prints 6


def calculate_sum_of_three_numbers(a,b,c): #a,b,c are parameters - in the function definition what we are using
    sum=a+b+c
    return sum

total=calculate_sum_of_three_numbers(1,2,3) #1,2,3 are arguments - values used in function call
print(total) #prints 6