
class Engine:
    def __init__(self):
        super().__init__()
        
    def start_engine(self):
        return 'Engine started'


class Wheels:
    def __init__(self):
        super().__init__()
    
    def number_of_wheels(self):
        return 4


# multiple Inheritance
class Car(Engine, Wheels): 
    def __init__(self):
        super().__init__()
        
    def drive(Self):
        return "Car is driving"
    
vehicle = Car()

result_start = vehicle.start_engine()
print(result_start) # Output: "Engine started"

result_drive = vehicle.drive()
print(result_drive) # Output: "Car is driving"

num_wheels = vehicle.number_of_wheels()  
print(num_wheels) # Output: 4
        