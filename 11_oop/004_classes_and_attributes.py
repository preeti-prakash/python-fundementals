# Step 1: Creating the Planet Class
class Planet:
    pass
 
# Step 2: Creating an Instance of the Planet Class
earth = Planet()
 
# This will throw a SyntaxError
# earth = new Planet()
 
# Step 3: Accessing Non-Existent Attributes
# print(earth.name)  # This will result in an AttributeError
 
# Step 4: Dynamically Adding Attributes
earth.name = 'The Earth'
print(earth.name)  # Output: 'The Earth'
 
# Step 5: Each Object Has Its Own Attributes
venus = Planet()
# print(venus.name)  # This will result in an AttributeError
 
# You need to explicitly set the name for Venus
venus.name = 'Venus'
print(venus.name)  # Output: 'Venus'
 
# Step 6: Accessing Non-Existent Methods
# venus.do_something()  # This will result in an AttributeError
