numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
print(numbers[3:8])

# Output - ['Three', 'Four', 'Five', 'Six', 'Seven']

numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
print(numbers[3:])

# Output - ['Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']]

numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
print(numbers[::4])
# Output- ['Zero', 'Four', 'Eight']

numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
print(numbers[2:9:2])
# Output - ['Two', 'Four', 'Six', 'Eight']

numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
print(numbers[::-2])
# Output -['Nine', 'Seven', 'Five', 'Three', 'One']

numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
numbers[1:6] = [1, 2, 3, 4, 5]
print(numbers)
# Output - ['Zero', 1, 2, 3, 4, 5, 'Six', 'Seven', 'Eight', 'Nine']