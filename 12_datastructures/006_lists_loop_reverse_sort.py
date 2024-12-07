#  Sorting, Looping, and Reversing Lists


# 1. reverse() - directly modifies the original list.
numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
numbers.reverse()
print(numbers)  # ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One', 'Zero']


# 2. reversed() - access elements in reverse order without changing the original list.
for number in reversed(numbers):
    print(number)
# This prints the elements in reverse order.

# 3. SORTING A LIST

#  sort() - sorting of the list, thereby altering the original list.
numbers.sort()
print(numbers)  # ['Eight', 'Five', 'Four', 'Nine', 'One', 'Seven', 'Six', 'Three', 'Two', 'Zero']


#  sorted() - access to elements in a sorted order without affecting the original list
for number in sorted(numbers):
    print(number)
# This prints the elements in sorted order.

# 4. Sorting by Length

for number in sorted(numbers, key=len):
    print(number)
# This prints elements ordered by their increasing length.

for number in sorted(numbers, key=len, reverse=True):
    print(number)
# This prints the elements in descending order of their length.
