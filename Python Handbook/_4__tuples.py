"""tuples"""

# Tuple is a list that is immutable
# Tuples contain duplicate elements
# In some ways, a tuple is similar to a Python list in terms of indexing,
# nested objects, and repetition but the main difference between both is Python tuple is immutable

myTuple = (1 ,3 ,5, 2)

print(myTuple[2])

# myTuple[2] = 6 will throw an Error as tuples are immutable

# Some important points regarding immutability
# - One cannot add items to a tuple once it is created.
# - Tuples cannot be appended or extended.
# - We cannot remove items from a tuple once it is created.
# - For creating a tuple with just one element, make sure to add a
# comma after element, else a string will be created
# source: geeksforgeeks
