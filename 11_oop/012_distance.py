import math

class Point:

    def __init__(self, x, y): 
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
        return (self.x,self.y)

    def distance_to(self, other):
        x1 = self.x
        y1 = self.y
        x2 = other.x
        y2 = other.y
        
        self.distance = math.sqrt(pow((x2-x1),2)+pow((y2-y1),2))
        return self.distance