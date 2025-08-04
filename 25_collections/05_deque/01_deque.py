from collections import deque


d = deque()

d.append(1)
d.append(3)

print(d)
d.appendleft(5)
print(d)


d.pop()
print(d)
d.popleft()
print(d)

d.clear()
print(d)


d.extend([9, 8, 7, 6, 5, 4, 3, 2, 1])
print(d)

d.extendleft([11, 12])
print(d)

d.rotate(1)
print(d)

d.rotate(2)
print(d)

d.rotate(-2)
print(d)
