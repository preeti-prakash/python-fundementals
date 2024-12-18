# finally and else
try:
    i = 1  # Simulating input from user
    j = 10/i
except Exception as error:
    print(error)
    j = 0
else:
    print("Else")
finally:
    print("Finally")
 
print(j)
print("End")


# Output:
# Else
# Finally
# 10.0
# End


# WHEN AN EXCEPTION IS THROWN
try:
    i = 0  # Simulating input from user
    j = 10/i
except Exception as error:
    print(error)
    j = 0
else:
    print("Else")
finally:
    print("Finally")
 
print(j)
print("End")

# Output:
# division by zero
# Finally
# 0
# End