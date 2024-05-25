"""user input and while loops and some important points"""
# use input() to take user input, it pauses your program and waits until user inputs something
message = input("Give me a message to print out\n")
print(message)

# input() takes everything as a string

# in python 2.7 use raw_input() instead of input()

# while loop runs as long as a certain condition is true

# you can use break and continue statements within loops to manipulate it

# avoid infinite loops

# for loops are effective for looping through a list but you
# shouldn't modify a list inside for loop because python will
# have a hard time keeping track of items in the list. To modify
# the list as you work through it use while loop


# you can consider the code below to move items from one list to another
freshFruits = ["apple", "banana", "orange", "watermelon", "strawberry"]
fruitBasket = []

while freshFruits:
    fruitBasket.append(freshFruits.pop())
for fruit in fruitBasket:
    print("You have " + fruit + " in your basket")

# to remove all instances of specific values from a list consider this code:
animalsList = ["dog", "cat", "elephant", "cat", "hawk", "fish", "cat", "bear"]
while "cat" in animalsList:
    animalsList.remove("cat")
print(animalsList)

# we can fill a list or dictionary with user input using while loop as well