class MotorBike:
    def __init__(self, speed):
        self.speed = speed  # State
 
    def increase_speed(self, how_much):
        self.speed += how_much  # Behavior
 
    def decrease_speed(self, how_much):
        self.speed -= how_much  # Behavior
 
honda = MotorBike(50)
ducati = MotorBike(250)
 
honda.increase_speed(150)
ducati.increase_speed(25)
 
honda.decrease_speed(50)
ducati.decrease_speed(25)
 
print(honda.speed)  # Output: 150
print(ducati.speed)  # Output: 250
