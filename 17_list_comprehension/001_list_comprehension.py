#  List Comprehension

# 1. CREATING LISTS IN A TRADITIONAL APPROACH

numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
 
numbers_length_four = []
 
for number in numbers:
    if len(number) == 4:
        numbers_length_four.append(number)
 
print(numbers_length_four)

# 2. CREATING LISTS USING LIST COMPREHENSION
numbers_length_four = [number for number in numbers]
 
print(numbers_length_four)

# 3. Adding a Conditional to Filter Elements:
numbers_length_four = [number for number in numbers if len(number) == 4]
 
print(numbers_length_four)  # Outputs: ['Zero', 'Four', 'Five', 'Nine']