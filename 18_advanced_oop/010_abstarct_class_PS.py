from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Rectangle class inheriting from Shape
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        self.area = self.length * self.width
        return self.area

    def perimeter(self):
        self.perimeter = 2*(self.length + self.width)
        return self.perimeter

# Circle class inheriting from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        self.area = 3.14*(self.radius ** 2)
        return self.area

    def perimeter(self):
        self.perimeter = 2 * 3.14 * self.radius
        return self.perimeter