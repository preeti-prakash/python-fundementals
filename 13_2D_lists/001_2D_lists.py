   # 1. Implementing 2D List in Python
two_d_list = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


# 2. Initialize a 2D list with 3 rows and 4 columns using nested for-loops
rows, cols = 3, 4
two_d_list = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(i * 10 + j)
    two_d_list.append(row)
 
print("Initial 2D list:", two_d_list)  
# Initial 2D list: [[0, 1, 2, 3], [10, 11, 12, 13], [20, 21, 22, 23]]

# Visualization

# [
#     [0,   1,  2,  3], 
#     [10, 11, 12, 13], 
#     [20, 21, 22, 23]
# ]

# 3. Access a specific element in the 2D list
print(f"Element at position [1][2]: {two_d_list[1][2]}")

# 4. # Set elements at specific positions
two_d_list[0][0] = 1
two_d_list[0][1] = 2
two_d_list[1][2] = 3
two_d_list[2][3] = 4
 
print("After updation:", two_d_list)  



# 5. # Traverse and print the 2D list
print("2D list traversal:")
for i in range(rows):
    for j in range(cols):
        print(two_d_list[i][j], end=' ')
    print()  