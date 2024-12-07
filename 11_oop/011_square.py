
class Square:
    def __init__(self, side): 
        self.side = side
    

    def calculate_area(self):
        if self.side <= 0:
            return -1
        else:
            self.area = self.side * self.side
            return self.area
        
        
    

    def calculate_perimeter(self):
        if self.side <= 0:
            return -1
        else:
            self.perimeter = 4 * self.side
            return self.perimeter

square = Square(5)
print(square.calculate_area())       # Output: 25
print(square.calculate_perimeter())  # Output: 20


square_with_zero_side = Square(0)
print(square_with_zero_side.calculate_area())       # Output: -1
print(square_with_zero_side.calculate_perimeter())  # Output: -1