number = 10
while number > 0:
    print(number)
    number -= 2 
 
# Output
# 10
# 8
# 6
# 4
# 2

i = 5
while i*i < 10:
    print(i)
print("done")  #the condition is not satisfied, the statement outside loop is executed

#  Output - done
    
 
i = 2 
while i * i < 10: 
  print(i, end=" ") 
print('done')               #infinite loop since no increment is mentioned
 
#  Error details
# Your code took too long to execute.
 
i = 2
while i*i < 10:
 print(i,  end=' ')
 i = i + 1
print("done")               #the values that satified the condition are printed and after the loop completion the ouside print stmt is also executed

# Output - 2 3 done
 
 
for i in range(1,11):
    if i==5:
       break
    print(i)
print("done")

# Output
# 1
# 2
# 3
# 4
# done
 
 
for i in range(1,11):
    if i%2:
       break
    print(i)
print("done")    

# Output
# done
 
 
for i in range(1,11):
   if i%2==0:
     continue
   print(i)
print("done")

# Output
# 1
# 3
# 5
# 7
# 9
# done