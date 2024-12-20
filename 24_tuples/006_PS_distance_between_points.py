import math

def calculate_distance(point1, point2):
    x1,y1 = point1
    x2,y2 = point2
    
    
    distance = math.sqrt((x2 - x1) ** 2  + (y2 - y1) ** 2)
    return distance
    
print(calculate_distance((1.0, 2.0), (4.0, 6.0)))  # Output: 5.0
print(calculate_distance((0.0, 0.0), (0.0, 5.0)))  # Output: 5.0