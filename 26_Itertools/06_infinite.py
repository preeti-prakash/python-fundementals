from itertools import count, cycle, repeat


# infinite loop - iterated from 10 - so on
for i in count(10):
    print(i)
    if i == 15:
        break


# cycle again and again after the list of elements - infinite
a = [1, 2, 3]
for i in cycle(a):
    print(i)

# reperats 1 infinitely
for i in repeat(1):
    print(i)

# to repeat n times
for i in repeat(1, 4):
    print(i)
