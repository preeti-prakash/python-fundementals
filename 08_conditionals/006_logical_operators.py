#LOGICAL and OPERATOR
# The and operator returns True only when both operands are True.

# 1. Logical and Operator
print(True and True)         # output: True
 
print(True and False)        # output: False
 
print(False and True)        # output: False
 
print(False and False)       # output: False


# LOGICAL or OPERATOR
# The or operator returns True if at least one of the operands is True.

# 2. Logical or Operator
print(True or False)         # output: True
 
print(False or True)         # output: True
 
print(True or True)          # output: True
 
print(False or False)        # output: False


# LOGICAL not OPERATOR
# The not operator returns the negation of the bool value.

# 3. Logical not Operator
print(not True)              # output: False
 
print(not(True))             # output: False
 
print(not False)             # output: True
 
print(not(False))            # output: True


# LOGICAL ^ (XOR) OPERATOR
# The ^ operator, also known as the exclusive or (xor) operator, returns True when the operands have different boolean values.

# 4. Logical ^ (XOR) Operator
 
print(True ^ True)           # output: False
 
print(True ^ False)          # output: True
 
print(False ^ True)          # output: True
 
print(False ^ False)         # output: False