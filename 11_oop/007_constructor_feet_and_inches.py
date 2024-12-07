class Dimension:
    #TODO: 
    def __init__(self, inches):#convert given inches into feet and inches
        if inches > 0:
            self.inches = inches % 12
            self.feet = inches // 12
        elif inches < 0:
            self.inches = -1
            self.feet = -1
        else:
            self.inches = 0
            self.feet = 0

# Examples
dim = Dimension(25)
print(dim.feet)    # Output: 2
print(dim.inches)  # Output: 1