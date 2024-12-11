# Lists of Custom Types

# 1. CREATING Country CLASS
class Country:
 
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
 
    def __repr__(self):
        return repr((self.name,self.population,self.area))
        
        
# 2. CREATING COUNTRY INSTANCES
countries = [Country('India',1200,100),
             Country('China', 1400, 200),
             Country('USA', 120, 300)]
 
countries.append(Country('Russia',80,900))


# 3. SORTING COUNTRIES
from operator import attrgetter
 
countries.sort(key=attrgetter('population'), reverse=True)
 
print(countries)


#4. FINDING Max AND Min
print(max(countries, key=attrgetter('population')))
print(min(countries, key=attrgetter('population')))
print(min(countries, key=attrgetter('area')))
print(max(countries, key=attrgetter('area')))