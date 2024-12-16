# Object Composition

# 1. Define the Book class
class Book(object):
    
    def __init__(self, id, name, author):
        self.id = id
        self.name = name
        self.author = author
        self.reviews = []  # Empty list for storing reviews
 
  
    def __repr__(self):
        return repr((self.id, self.name, self.author, self.reviews))
        
    # Add the add_review method to the Book class
    def add_review(self, review):
        self.reviews.append(review)
        
        
# Create a Book instance
book = Book(123, 'Object Oriented Programming with Python', 'Ranga')
print(book)  # Output: (123, 'Object Oriented Programming with Python', 'Ranga', [])


# 2. Creating the Review Class

class Review:
   
    def __init__(self, id, description, rating):
        self.id = id
        self.description = description
        self.rating = rating
 
   
    def __repr__(self):
        return repr((self.id, self.description, self.rating))
        
# Create a Review instance
review = Review(10, 'Great Book', 5)
print(review)  # Output: (10, 'Great Book', 5)
book.add_review(Review(10, 'Great Book', 5))
book.add_review(Review(101, 'Awesome', 5))
print(book)  # Output: (123, 'Object Oriented Programming with Python', 'Ranga', [(10, 'Great Book', 5), (101, 'Awesome', 5)])