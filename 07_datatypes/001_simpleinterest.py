def calculate_simple_interest(principal, interest,duration):
    total = principal+(principal*interest*0.01*duration)
    return total

print(calculate_simple_interest(10000,5,5))