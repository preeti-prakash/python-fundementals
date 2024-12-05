if(False):
   print("False") #Output: Nothig is printed
 
if(True):
   print("True") #Output:True
 
#  Any non-zero value is considered to be true
x = -6
if x:
   print("something") #Output: Something
 
 
k = 15
if (k > 20):
  print(1)
elif (k > 10):
  print(2)          #Output: 2 : Condition is satisfied
elif (k < 20):
  print(3)
else:
  print(4)
 
 
l = 15
if (l < 20):
    print("l<20")       #Output: l<20 : Condition is satisfied

if (l > 20):
    print("l>20")
else:
    print("Who am I?")  #Output: Who am I? : else part executed
 
a = 10
b = 20
if a > 5:
    if b < 30:
        print("Inner condition met")       #Output: Inner condition met
    else:
        print("Inner condition not met")
else:
    print("Outer condition not met")
 
 
m = 15
if m>20:
    if m<20:
        print("m>20")
    else:
        print("Who am I?")  #Output: Nothing is printed : condition not satisfied
 
 
number = 5
if number < 0:
  number = number + 10
number = number + 5
print(number)          #Output:10 : The Condition is not satisfied but the below lines are not part of the if stmt, so executed
 
 
number = 5
if number < 0:
  number = number + 10
  number = number + 5
print(number)           #Output:5 : The Condition is not satisfied but the below line is not part of the if stmt, so executed
 
number = 5
if(number%2==0):
   isEven = True
else:
   isEven = False
print(isEven)       #Output:False
 
x = 10
y = 5
if x > 5 and y < 10:
    print("Condition 1")    #Output:Condition 1
elif x == 10 or y == 5:
    print("Condition 2")
else:
    print("Condition 3")
 
x = 5
if not x == 3:
    print("x is not equal to 3") #Output: x is not equal to 3
else:
    print("x is equal to 3")
 
 
number = 4
isEven = True if number%2==0 else False
print(isEven)  #Output: True , Condition not satified : returns nothing, prints the variable value