# The break statement is used to exit a loop when a specific condition is met

for i in range(1, 11):
    if i == 5:
       break
    print(i, end=' ')
print("done")

# Output - 1 2 3 4 done

# The continue statement is used to skip the current iteration of a loop and proceed to the next iteration.

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i, end=' ')
print("done")

# Output - 1 3 5 7 9 done