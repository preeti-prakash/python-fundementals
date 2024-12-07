#  constructors - to set an initial state for those instances.

class MotorBike:
    def __init__(self):                 # Contructor
        print("MotorBike instance created")
 
honda = MotorBike()  # Output: "MotorBike instance created"
ducati = MotorBike()  # Output: "MotorBike instance created"


#  ADDING PARAMETERS TO A CONSTRUCTOR
class MotorBike:
    def __init__(self, speed):
        print(speed)
 
honda = MotorBike(50)  # Output: 50
ducati = MotorBike(250)  # Output: 250


#  INITIALIZING ATTRIBUTES IN A CONSTRUCTOR
class MotorBike:
    def __init__(self, speed):
        self.speed = speed              #settinf the initaial state when the repective instanes were created with their speeds
 
honda = MotorBike(50)
ducati = MotorBike(250)
 
print(honda.speed)  # Output: 50
print(ducati.speed)  # Output: 250

