 # Logical Operations - NOT and NOT EQUAL TO
# NOT and !=
x = 5
if not x == 6:
    print("Condition is satisfied")
    
x = 5
if x != 6:
    print("Condition is satisfied")
    

# ANY NON-ZERO VALUE IS TRUE
print(bool(6))  # True
print(bool(-6))  # True
print(bool(0))  # False