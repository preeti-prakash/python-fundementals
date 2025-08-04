from itertools import accumulate
import operator
a = [1, 2, 3, 4]

# acc = accumulate(a)
# print(a)
# print(list(acc))


accu = accumulate(a, func=operator.mul)
print(a)
print(list(accu))
# output
# [1, 2, 3, 4]
# [1, 2, 6, 24]

b = [1, 2, 3, 5, 1, 3]
accum = accumulate(b, func=max)
print(b)
print(list(accum))
# Output
# [1, 2, 3, 5, 1, 3]
# [1, 2, 3, 5, 5, 5]
