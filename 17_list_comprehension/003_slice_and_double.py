def slice_and_double(list, a, b):
    if a < 0:
        a=0
        
    if b > len(list):
        b = len(list)
        
    sliced_list = list[a:b]
    double_the_list= []
    # print(sliced_list)
    
    double_the_sliced_list = [item * 2 for item in sliced_list]
    # print(double_the_sliced_list)
    
    list[a:b] = double_the_sliced_list
    
    return list

print(slice_and_double([1, 2, 3, 4, 5], 1,4))


# Output - [1, 4, 6, 8, 5]