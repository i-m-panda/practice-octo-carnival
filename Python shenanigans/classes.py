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

myDog = Dog("Lily", 3)
myDog.bark() # calling methods
myDog.dog_age()
print(myDog.name) # accessing attributes

# __init__ is class constructor(has no return statement but python
# implicitly returns the an instance representing the one being created)

# "self" has to be passed to each method definition of the class,
# and it should always be the first parameter of the each method
# "self" is the reference to the class instance (it gives individual instance
# the access to the attributes and methods)

# every attribute(member variable) in a class needs an initial value
# default value for attributes are set in class constructor __init__

# you can change the value of attribute for an instance,
# directly(myDog.name = "Lucy") or via a class method

# you can use inheritance to inherit attributes and methods from a parent class
# when you inherit a class, all attributes and methods are inherited

# when you create a child class, the parent class must be the part of the current file
# and it must appear before the child class in the file

class Car():
    """class for defining a real world car"""
    def __init__(self, speed: int, transmission: str, name: str):
        self.name = name
        self.speed = speed
        self.transmission = transmission

    def increase_speed(self, speed: int):
        """increases the speed of the car"""
        self.speed += speed

    def show_speed(self):
        """show current speed of the car"""
        print("speed of the car is: " + str(self.speed))

    def fill_gas(self):
        """function for filling up the gas tank of the car"""
        print("Filling up the gas tank...")
        print("Gas tank is full")

class ElectricCar(Car):
    """class for defining an electric car"""
    def __init__(self, speed: int, transmission: str, name: str, battery_capacity: int):
        self.battery_capacity = battery_capacity
        super().__init__(speed, transmission, name)

    def charge_left(self, used: int):
        """displays the charge left for the car"""
        print(self.name + " is at: " + str(self.battery_capacity - used))

    # overriding parent class method
    def fill_gas(self):
        """function for filling up the gas tank of the car"""
        print("This car doesn't have a gas tank")

myTesla = ElectricCar(20, "automatic", "Tesla", 200)
myTesla.charge_left(40)
myTesla.increase_speed(40)
myTesla.show_speed()
myTesla.fill_gas()

# you can overide methods and attribute of parent class in child class

# To manage growing list of attribute of methods of a class, you can always
# break the large classes into smaller classes and then use your small class
# instance as an attribute in main class, like below:

class Engine():
    """class encapsulating methods and attributes associated with a car engine"""
    def __init__(self, transmission: str, speed: int):
        self.speed = speed
        self.transmission = transmission

    def increase_speed(self, speed: int):
        """increases the speed of the car"""
        self.speed += speed

    def show_speed(self):
        """show current speed of the car"""
        print("speed of the car is: " + str(self.speed))

class OtherCar():
    """class for defining a real world car"""
    def __init__(self, speed: int, transmission: str, name: str):
        self.name = name
        self.engine = Engine(transmission, speed)

    def fill_gas(self):
        """function for filling up the gas tank of the car"""
        print("Filling up the gas tank...")
        print("Gas tank is full")

class OtherElectricCar(OtherCar):
    """class for defining an electric car"""
    def __init__(self, speed: int, transmission: str, name: str, battery_capacity: int):
        self.battery_capacity = battery_capacity
        super().__init__(speed, transmission, name)

    def charge_left(self, used: int):
        """displays the charge left for the car"""
        print(self.name + " is at: " + str(self.battery_capacity - used))

    # overriding parent class method
    def fill_gas(self):
        """function for filling up the gas tank of the car"""
        print("This car doesn't have a gas tank")

myNexon = OtherElectricCar(40, "automatic", "Nexon EV", 500)
myNexon.charge_left(20)
myNexon.engine.increase_speed(50)
myNexon.engine.show_speed()
myNexon.fill_gas()

# we can create a module of single or multiple related classes and then import them
# to keep the code clean and managable

# IMPORTING CLASSES
# from module_name import class_name | importing single class
# from module_name import class_name_1, class_name_2 | importing multiple classes
# import module_name | importing entire module, to create instance use dot operator
# from module_name import * | importing all classes(dot operator not required) [not recommended]
