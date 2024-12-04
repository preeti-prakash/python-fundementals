def sum_of_squares(n):
    sum=0
    for i in range(2,2*n +1,2):
        i=pow(i,2)
        sum=sum+i
    return sum
    
        
print(sum_of_squares(5))