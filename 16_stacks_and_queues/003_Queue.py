# QUEUE - FIFO

# Enqueue (Add to rear of queue)

numbers = []
 
numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
 
print("Queue after enqueues:", numbers)  # Output: Queue after enqueues: [1, 2, 3, 4]

# Dequeue (Remove front of queue)
print("Dequeued element:", numbers.pop(0))  # Output: Dequeued element: 1
print("Queue after Dequeues:", numbers)  # Output: Queue after Dequeues: [2, 3, 4]

# Front (Inspect front of queue)
print("Front of queue:", numbers[0])  # Output: Front of queue: 2
print("Queue after front of queue:", numbers)  # Output: Queue after Dequeues: [2, 3, 4]

# IsEmpty (Check if queue is empty)
print("Is queue empty?", not bool(numbers))  # Output: Is queue empty? False
