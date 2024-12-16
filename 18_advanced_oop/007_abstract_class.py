#  Abstract Classes in Python

# An abstract class can’t be instantiated, meaning you can’t create objects of an abstract class.
from abc import ABC, abstractmethod
 
class AbstractAnimal(ABC):
    @abstractmethod
    def bark(self): pass


# IMPLEMENTING ABSTRACT METHODS IN A SUBCLASS
class Dog(AbstractAnimal):
    def bark(self):
        print("Bow Bow")
 
Dog().bark()  # Output: "Bow Bow"
