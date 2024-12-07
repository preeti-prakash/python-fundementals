#  1. CREATING A CONSTRUCTOR IN THE Book CLASS
class Book:
    def __init__(self, name):
        self.name = name
 
learning_python = Book('Learning Python In 100 Steps')
print(learning_python.name)  # Output: "Learning Python In 100 Steps"


#  2. WHAT HAPPENS IF  self IS MISSING?

class Planet:
    def __init__(): pass
 
# planet = Planet()
 
# Error details: Planet.__init__() takes 0 positional arguments but 1 was given
# because Python automatically passes self to the __init__() method.

# 3. CAN WE HAVE MULTIPLE CONSTRUCTORS

# nly the last constructor is available. If you want to handle multiple scenarios, you can use default parameter values.
class Planet:
    def __init__(self, name): pass
    def __init__(self): pass

#  4. BUILDING CONSTRUCTORS WITH DEFAULT VALUES FOR PARAMETERS

class Planet:
    def __init__(self, name="Earth"):
        self.name = name
 
planet1 = Planet()
print(planet1.name)  # Output: "Earth"
planet2 = Planet("Jupiter")
print(planet2.name)  # Output: "Jupiter"

#  5. BEST PRACTICE: INITIALIZE ALL ATTRIBUTES IN A CONSTRUCTOR

class Planet:
    def __init__(self, name="Earth"):
        self.name = name
        self.speed = 10
        self.distance_from_sun = 10000
 
planet = Planet()
 
print(planet.speed)  # Output: 10
 
print(planet.distance_from_sun)  # Output: 10000
