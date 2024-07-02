"""functions related information"""
# def is used to define functions

# defining a function
def say_hello(name: str) -> None:
    """says hello to user"""
    print("Hello " + name)

# calling a method
say_hello("John")

# There are several ways to pass as argument to a function
# When you call a function, python must match each argument in function call
# with the parameters in function definition

# POSTIONAL ARGUMENT(order of arguments provided in function
# call is matched with params in function definition)
# KEYWORD ARGUMENT(is a key-value pair you pass as
# the argument, order doesn't matter in function call)
def pet_describe(animal_type: str, pet_name: str) -> None:
    """Describes the pet"""
    print("I have a " + animal_type)
    print("It's called " + pet_name)

pet_describe(pet_name="Johnny", animal_type="turtle")

#DEFAULT_VALUE(You define default value for params
# in function definition, if value is provided in function
# call then the parameter value is overwritten, else default
# value is used | default arguments should always follow non
# default arguments)
def pet_describe_with_default_animal_type(pet_name: str, animal_type: str = "dog") -> None:
    """Describes the pet"""
    print("I have a " + animal_type)
    print("It's called " + pet_name)

# correct call, default value for animal_type is used
pet_describe_with_default_animal_type("Duke")
# correct call, animal_type is overwritten with cat
pet_describe_with_default_animal_type(animal_type="cat", pet_name="Lucy")
# correct call, animal_type is overwritten with bird
pet_describe_with_default_animal_type("Roger", "bird")

# return value takes a value from inside the function and take
# it to the line where function is called

# lists, dictionaries, etc. are passed by reference to the function
# You can prevent this by creating a deep copy of passed argument

# PASSING AN ARBITRARY NO. OF ARGUMENTS
# toppings will become an empty tuple and anything passed to pizza()
# will be pushed to this tuple
def pizza(*toppings):
    "prints pizza toppings"
    print(toppings)

# NOTE: If you are mixing positional and arbitrary arguments then always
# place them at the end of the parameter lists as python first matches
# positional args, then keywords arguments and then remaining arguments
# in final parameter

# PASSING ARBITRARY NO. OF KEY VALUE PAIR AS ARGUMENTS
# user_info will become an empty dictionary and all the keyword arguments
# will be inserted in this dictionary as key value pair
def build_profile(first_name, last_name, **user_info):
    """builds a user profile"""
    profile = {
        "first_name": first_name,
        "last_name": last_name
    }
    for key,value in user_info.items():
        profile[key] = value
    print(profile)

build_profile("Albert", "Einstein", location="Princeton", field_of_study="Physics")

# You can manage your project by creating modules(files with .py extension) and import
# functions or everything from these modules
# There are several ways to import a module in a file
# 1. import math | # imports everything, accessible by dot(.) operator
# 2. from math import pi | # import specific function/variable
# 3. from math import pi as PI | # use an alias for function/variable
# 4. import math as m | # use an alias for module
# 5. from math import * | # all function and constants/variables are imported,
# don't need to use dot operator (not best approach, as file importing the module
# can overwrite the function with same name)

# alias are used in case of name conflicts
