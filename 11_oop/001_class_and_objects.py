#  a class acts as a blueprint for creating objects. 

# 1. Creating an Empty Class

class Country:
    pass


#  2. Creating an Instance of a Class

#  india, usa, and netherlands are objects of the Country class.

india = Country()

# 3. Adding State to Objects
india.name = 'India'
india.capital = 'New Delhi'


usa = Country()
usa.name = 'USA'
usa.capital = 'Washington'


netherlands = Country()
netherlands.name = 'Netherlands'
netherlands.capital = 'Amsterdam'

# name and capital attribute to each of our Country instances.

# 4. Accessing Object Attributes
print(india.name)  # Output: 'India'
print(usa.capital)  # Output: 'Washington'





