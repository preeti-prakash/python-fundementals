def squares_map(n):
    squares = { num: num ** 2 for num in range(1,n+1) }
    return squares
    
print(squares_map(10))  
 
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}