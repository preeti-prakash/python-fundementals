names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
result = [name for name in names if 'e' in name]
print(result)  # output - ['Alice', 'Charlie', 'Eve']

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [num for num in numbers if num % 2 == 0]
print(result)  # output - [2, 4, 6, 8, 10]

sentence = "The quick brown fox jumps over the lazy dog"
result = [char for char in sentence if char.lower() in 'aeiou']
print(result)  # output - ['e', 'u', 'i', 'o', 'o', 'u', 'o', 'e', 'e', 'a', 'o']

original_list = [1, 2, 3, 4, 5]
result = [num**2 for num in original_list]
print(result)  # output - [1, 4, 9, 16, 25]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = ['even' if num % 2 == 0 else 'odd' for num in numbers]
print(result)  # output - ['odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even']


sentence = "Hello World! How are you doing?"
result = [len(word) for word in sentence.split()]
print(result)   #output - [5, 6, 3, 3, 3, 6]