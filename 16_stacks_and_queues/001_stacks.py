# STACK - LIFO

# 1. Push (Add to top of stack)

numbers = []
 
numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)

print("Stack after pushes:", numbers)  # Output: Stack after pushes: [1, 2, 3, 4]


#  2. Pop (Remove top of stack)
print("Popped element:", numbers.pop())  # Output: Popped element: 4
print("Stack after pop:", numbers) # Output: Stack after pop: [1, 2, 3]


# 3. Top (Inspect top of stack)
print("Top of stack:", numbers[-1])  # Output: Top of stack: 3
print("Stack after top of stack:", numbers) #Output: Stack after top of stack: [1, 2, 3]

#  4. IsEmpty (Check if stack is empty)
print("Is stack empty?", not bool(numbers))  # Output: Is stack empty? False