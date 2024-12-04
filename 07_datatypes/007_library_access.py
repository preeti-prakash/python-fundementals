def can_access_library(age):
    accessible = age>=18
    return accessible
    
print(can_access_library(17))  # Output: False
print(can_access_library(19))  # Output: True