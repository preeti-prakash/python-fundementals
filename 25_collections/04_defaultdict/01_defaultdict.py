# returns a default value for the key not present in the dictionary - follows the type mentioned

from collections import defaultdict
d = defaultdict(int)


d['a'] = 1
d['c'] = 4
# print(d)   {'a': 1, 'c': 4}
# print(d['f'])     0
