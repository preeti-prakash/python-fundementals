# BASIC IF STATEMENT
i = 2
print("before if statement")
if i>3:
    print(f"{i} is greater than 3")
print("after if statement")             #Output: both the print statements are executedBlue



i = 2
print("before if statement")
if i>3:
    print(f"{i} is greater than 3")
    print("after if statement")   #Output: the first print statement is executed, skipping the conditional code since the code is not satisfied



i = 2
if i>3:
    print(f"{i} is greater than 3")
else:
    print(f"{i} is less than 3")  #Output: the else part is satisfied, the second print statement is executed

i=1
if i==1:                        #Output: the comaprison operator( assignment )  
    print(f"{i} is equal to 1")


#IF STATEMENT WITH BOOLEAN VALUES

if(False):
  print("False")  # This will not be executed as the condition is False
if(True):
  print("True")  # This will be executed as the condition is True
# Output: True