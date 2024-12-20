#  dictionary - a collection of key-value pairs.

occurances = dict(a = 5, b = 6, c = 8)
print(occurances)       # {'a': 5, 'b': 6, 'c': 8}
print(type(occurances)) # <class 'dict'>



#  ACCESSING AND MODIFYING VALUES

occurances['d'] = 15
print(occurances)  # {'a': 5, 'b': 6, 'c': 8, 'd': 15}
# Modifying the value of key 'd'
occurances['d'] = 10
print(occurances)  # {'a': 5, 'b': 6, 'c': 8, 'd': 10}
print(occurances['d'])  # 10


#  HANDLING NON EXISTING KEYS
# print(occurances['e'])  # Uncommenting this will raise KeyError: 'e'

print(occurances.get('d'))  # 10
print(occurances.get('e'))  # None
print(occurances.get('e', 10))  # 10

# DICTIONARY METHODS

print(occurances.keys())  # dict_keys(['a', 'b', 'c', 'd'])
print(occurances.values())  # dict_values([5, 6, 8, 10])
print(occurances.items())  # dict_items([('a', 5), ('b', 6), ('c', 8), ('d', 10)])


# ITERATING A DICTIONARY
for (key, value) in occurances.items():
    print(f"{key} {value}") 
    
# Expected output:
# a 5
# b 6
# c 8
# d 10


#  DELETING FROM A DICTIONARY
del occurances['a']
print(occurances)  # {'b': 6, 'c': 8, 'd': 10}