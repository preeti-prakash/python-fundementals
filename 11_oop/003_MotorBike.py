class MotorBike:
    pass

honda = MotorBike()
ducati = MotorBike()        #instances of class

print(honda)        #<__main__.MotorBike object at 0x1025bd400>
print(ducati)       # <__main__.MotorBike object at 0x1025665d0>  - memory locations of an object

# Adding STATE
honda.speed = 50
ducati.speed = 250

# Accessing State
print(honda.speed)  # Output: 5

print(ducati.speed) # Output: 250
