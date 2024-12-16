#  Multiple Inheritance

class LandAnimal:
    def __init__(self):
        # constructor for the object class
        super().__init__()
        self.walking_speed = 5
        
    def increase_walking_speed(self, how_much):
        self.walking_speed += how_much
        
class WaterAnimal:
    def __init__(self):
        super().__init__()
        self.swimming_speed = 10
    
    def increase_swimming_speed(self, how_much):
        self.swimming_speed += how_much
        
class Amphibian(WaterAnimal, LandAnimal):
    def __init__(self):
        # constructor for the super class WaterAnimal and LandAnimal
        super().__init__()
        
amphibian = Amphibian()
print(amphibian.swimming_speed)  # Output: 10
print(amphibian.walking_speed)  # Output: 5
amphibian.increase_swimming_speed(25)
amphibian.increase_walking_speed(50)
print(amphibian.swimming_speed)  # Output: 35
print(amphibian.walking_speed)  # Output: 55