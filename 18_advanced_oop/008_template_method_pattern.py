# Template Method Pattern

from abc import ABC, abstractmethod
 
class AbstractRecipe(ABC):
 
    # template method
    def execute(self):
        self.prepare()
        self.recipe()
        self.cleanup()
 
    @abstractmethod
    def prepare(self): pass
 
    @abstractmethod
    def recipe(self): pass
 
    @abstractmethod
    def cleanup(self): pass

# subclass that implements the abstract methods of the Abstract class
class Recipe1(AbstractRecipe):
 
    def prepare(self):
        print('do the dishes')
        print('get raw materials')
 
    def recipe(self):
        print('execute the steps')
 
    def cleanup(self): pass
 
Recipe1().execute()

# Output:
# do the dishes
# get raw materials
# execute the steps


class MicrowaveRecipe(AbstractRecipe):
 
    def prepare(self):
        print('do the dishes')
        print('get raw materials')
        print('switch on microwave')
 
    def recipe(self):
        print('execute the steps')
 
    def cleanup(self):
        print('switch off microwave')
 
MicrowaveRecipe().execute()

# Output:

# do the dishes
# get raw materials
# switch on microwave
# execute the steps
# switch off microwave