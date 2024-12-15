class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def is_empty(self):
        return len(self.items) == 0
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        
    def top(self):
        if not self.is_empty():
            return self.items[-1]
        
    def display(self):
        print(self.items)


# Create a Stack
s = Stack()
 
# Push elements
s.push(1)  # Adding 1 to the stack
s.push(2)  # Adding 2 to the stack
s.push(3)  # Adding 3 to the stack
 
# Display the stack
s.display()  # Output: [1, 2, 3]
 
# Pop elements
print(s.pop())  # Output: 3 (removing top element)
s.display()  # Output: [1, 2]
 
# Top element
print(s.top())  # Output: 2 (top element)
 
# Check if stack is empty
print(s.is_empty())  # Output: False (stack is not empty)