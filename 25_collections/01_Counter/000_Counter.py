# A counter is a container that has elements as dictionary keys and their count and dict values.


from collections import Counter

x = "aaaaabbbbcccd"
my_counter = Counter(x)
# print(my_counter) ({'a': 5, 'b': 4, 'c': 3, 'd': 1})

y = "abbcccdddd"
my_other_counter = Counter(y)
# print(my_other_counter) ({'d': 4, 'c': 3, 'b': 2, 'a': 1})

# print(my_counter.keys()) (['a', 'b', 'c', 'd'])
# print(my_counter.values())   ([5, 4, 3, 1])


# most common element or elements in the Counter
# print(my_counter.most_common(1))       [('a', 5)]
# print(my_counter.most_common(1)[0])    ('a', 5)
# print(my_counter.most_common(1)[0][0])    a

# two most common elements

# print(my_counter.most_common(2))      [('a', 5), ('b', 4)]

# list
# print(list(my_counter.elements()))       ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'd']
