def is_leap_year(year):
    if year <=0:
        return False
    
    year_divisible_by_4 = year % 4 == 0
    year_divisible_by_100 = year % 100 == 0
    year_divisible_by_400= year % 400 == 0
    
    # print(f"year_divisible_by_4 - {year_divisible_by_4}")
    # print(f"year_divisible_by_100 - {year_divisible_by_100}")
    # print(f"year_divisible_by_400 - {year_divisible_by_400}")
    
    if not year_divisible_by_4:
        return False
    
    if not year_divisible_by_100:
        return True
    
    if year_divisible_by_400:
        return True
    
    if not year_divisible_by_400:
        return False

print(is_leap_year(2048))
print(is_leap_year(2000))
print(is_leap_year(2400))
print(is_leap_year(2100))
print(is_leap_year(2300))
    