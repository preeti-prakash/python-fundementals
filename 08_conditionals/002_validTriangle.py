def is_valid_triangle(angle1, angle2, angle3):
    if angle1<=0:
        return False
    if angle2<=0:
        return False
    if angle3<=0:
        return False
    if (angle1+angle2+angle3) == 180:
        return True
print(is_valid_triangle(30, 60, 90) )
    