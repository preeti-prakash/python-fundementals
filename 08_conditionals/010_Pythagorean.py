def is_right_angled_triangle(side1, side2, side3):
    if side1 == 0 or side2 == 0 or side3 == 0:
        return False
    
    if side1*side1 == side2*side2 + side3*side3:
        return True
    if side2*side2 == side1*side1 + side3*side3:
        return True
    if side3*side3 == side1*side1 + side2*side2:
        return True
    return False
    
        
print(is_right_angled_triangle(3, 4, 5))  # Output: True      s