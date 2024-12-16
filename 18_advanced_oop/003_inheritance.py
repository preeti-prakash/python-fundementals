# INHERITANCE

class Animal:
    def bark(self):
        print("bark")

animal = Animal()


# inherit the super class Animal
class Pet(Animal):

    def groom(self):
        print("groom")


dog = Pet()
dog.bark()
dog.groom()