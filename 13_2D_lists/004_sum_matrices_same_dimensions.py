def add_matrices(matrix1, matrix2):
    if not matrix1 or not matrix2:
        return []
    sum_matrix = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j]+matrix2[i][j])
        sum_matrix.append(row)
    return sum_matrix

# Testing the function
print(add_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]]))  # Output: [[6, 8], [10, 12]]
print(add_matrices([], []))  # Output: []