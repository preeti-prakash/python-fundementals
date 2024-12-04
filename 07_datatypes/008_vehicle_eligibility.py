def is_eligible_for_race(max_speed):
    result= max_speed == 200
    return result
    
print(is_eligible_for_race(150))  # Output: False
print(is_eligible_for_race(200))  # Output: True