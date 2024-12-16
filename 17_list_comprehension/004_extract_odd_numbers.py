def extract_odd_numbers(values):
    if values == []:
        return []
    list_of_odd_numbers = []
    list_of_odd_numbers = [value for value in values if value % 2 ==1]
    return list_of_odd_numbers
    
print(extract_odd_numbers([3, 6, 9, 1, 4, 15, 6, 3]))  # Output: [3, 9, 1, 15, 3]
print(extract_odd_numbers([10, 22, 33, 40, 55, 60]))  # Output: [33, 55]
print(extract_odd_numbers([]))  # Output: []