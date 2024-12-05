i = 1

while i < 11:
    if i == 5:
        break               #comes out of loop when condition is satisfied
    print(i, end=' ')

    i += 1
print("done")

# Output - 1 2 3 4 done



i = 1

while i< 11:

    if i%2 == 0:
        i += 1
        continue
    print(i, end=' ')

    i+=1

print("done")

# Output - 1 3 5 7 9 done
