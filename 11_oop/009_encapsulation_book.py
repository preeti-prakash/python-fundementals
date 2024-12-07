class Book:
    def __init__(self, name, copies = 0):
        self.name = name
        self.copies = copies

    def increase_copies(self, how_much):            #ADDING METHODS TO MODIFY copies
        self.copies += how_much

    def decrease_copies(self, how_much):
        self.copies -= how_much

the_art_of_computer_programming = Book("The Art of Computer Programming")
print(the_art_of_computer_programming.name) #Output - The Art of Computer Programming
print(the_art_of_computer_programming.copies)   #Output - 0

the_art_of_computer_programming.increase_copies(100)
print(the_art_of_computer_programming.copies)   #Output - 100

the_art_of_computer_programming.decrease_copies(50)
print(the_art_of_computer_programming.copies)   #Output - 50




