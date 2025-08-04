# add10 = lambda x: x+10
# print(add10(5))


points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D)
# print(points2D)
print(points2D_sorted)


# to sort the tuples in the list based on the  y keys
points2D_sorted = sorted(points2D, key=lambda x: x[1])
# print(points2D)
print(points2D_sorted)

# sort based on the sum of tuples in the list
points2D_sorted = sorted(points2D, key=lambda x: x[0]+x[1])
# print(points2D)
print(points2D_sorted)
