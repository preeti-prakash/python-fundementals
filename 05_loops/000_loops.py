# A for loop in Python is used to iterate over a sequence of values.
# for val in sequence:
    #Body of for
    
for i in range(1,10):
    print(i)                #prints numbers from 1 to 9
    
help(range) #getting help for range function

# Indentation
# for i in range(1,10):
# Incorrect indentation
# IndentationError: expected an indented block
# print(i)h


for i in range (1,11):
    print(i * i)   #we're squaring numbers from 1 to 10.
    
    
# Calculating Sum with for Loop
sum = 0
 
for i in range (1,11):
    sum = sum + i
 
print(sum)


# multiplication table
for i in range(1, 11):
        print(f"5 * {i} = {5 * i}")   #formatted string literals, also known as f-strings
    

# Counting DOWN with for Loop
for i in range (10,0,-1):
   print(i)
   
   