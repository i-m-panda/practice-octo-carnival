"""description of classes and its usecases"""

# A sample dog class
class Dog():
    """class having attributes and methods fit for a Dog"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self) -> None:
        """Makes the dog bark"""
        print(self.name + " is barking")

    def dog_age(self) -> None:
        """Tells the age of the dog"""
        print(self.name + " is " + str(self.age) + " years old")

lily = Dog("Lily", 3)
lily.bark() # calling methods
lily.dog_age()
print(lily.name) # accessing attributes

# __init__ is class constructor(has no return statement but python
# implicitly returns the an instance representing the one being created)

# "self" has to be passed to each method definition of the class,
# and it should always be the first parameter of the each method
# "self" is the reference to the class instance (it gives individual instance
# the access to the attributes and methods)
