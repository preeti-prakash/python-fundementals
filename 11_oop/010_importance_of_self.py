#  EXPLORING IMPORTANCE OF self
    
class Planet:
    def rotate(self):               #  ADDING self to Planet
        print("rotate")
 
    def revolve(self):
        print("revolve")
        
    def rotate_and_revolve(self):           #  USING self TO CHAIN METHOD CALLS
        self.rotate()
        self.revolve()
 
# Create an instance and call its methods
earth = Planet()
earth.rotate_and_revolve()  # Output will be "rotate" followed by "revolve"