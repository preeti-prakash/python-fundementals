# object CLASS: A BASE FOR ALL PYTHON CLASSES
# all Python 3 classes inherit from the object class by default.
# object class provides default implementations for common methods like __repr__.
# override the default __repr__ method to change the string representation of an instance.



# Define a Book class with a custom __repr__ method
class Book():
    def __repr__(self):
        return repr('new book')
 
# Create an instance of Book and print it
book = Book()
print(book)  # Output: 'new book'