"""lists related methods and manipulation"""
# lists: collection of items in particular order

SIMPLE_LIST = [1, 3, 5, 7, 10, 2, 100, 3]
MIXED_LIST = [100, "hello", "c", "d", True, 20]

# accessing element at position 3
print(MIXED_LIST[3])

# accessing last and second last element
print(SIMPLE_LIST[-1])
print(SIMPLE_LIST[-2])

# updating an element at position 2
SIMPLE_LIST[2] = 4

# adding an element to the end of the list
MIXED_LIST.append("last")

# inserting an element at a particular index
# you can use this to also insert element in the beginning of the list
SIMPLE_LIST.insert(1, 200)

# removing and item using del
del MIXED_LIST[2] # "c" will be deleted

# use pop() to delete items from the end of the list
# it also returns the value of item being deleted
lastItem = MIXED_LIST.pop()

# you can provide index to pop() to remove item on a particular index
secondItem = SIMPLE_LIST.pop(1)

# NOTE: use pop() if you want to use the item else use del

# use remove() to remove item by value, removes first occurence only
SIMPLE_LIST.remove(3)

# ORGANIZING A LIST

# use sorted() to temporarily sort a list
print(sorted(SIMPLE_LIST))

# pass argument reverse = True to sort in reverse order
print(sorted(SIMPLE_LIST, reverse=True))

NEW_SIMPLE_LIST = SIMPLE_LIST[:]

# use sort to permanently sort the list
NEW_SIMPLE_LIST.sort()
print(NEW_SIMPLE_LIST)

# pass argument reverse = True to sort in reverse order permanently
NEW_SIMPLE_LIST.sort(reverse=True)
print(NEW_SIMPLE_LIST)

# NOTE: if the elements are not of same case then sort()/sorted() can produce arbitrary results

NEW_MIXED_LIST = MIXED_LIST[:]

# use reverse() to reverse the list permanently
print(NEW_MIXED_LIST)
NEW_MIXED_LIST.reverse()
print(NEW_MIXED_LIST)

# WORKING WITH LISTS

# use for loop to traverse a list
for element in NEW_MIXED_LIST:
    print(element)

# range() can be used to generate a series of number
for genNumber in range(1, 5):
    print(genNumber) # prints a list of 1, 2, 3, 4

# you can skip numbers in range() as well like below
for genNumber in range(1, 11, 2):
    print(genNumber) # prints a list of 1, 3, 5, 7, 9 (starts at 1 then add 2 everytime)

EVEN_NUMBERS = []
for genNumber in range(2, 11, 2):
    EVEN_NUMBERS.append(genNumber)

# some useful functions for the list

print(min(EVEN_NUMBERS))
print(max(EVEN_NUMBERS))
print(sum(EVEN_NUMBERS))

# !IMPORTANT
# use list comprehensions as much as possible (these are compact code for list generation)

SQUARES_OF_EVEN_NUMBERS = [ evenNumber ** 2 for evenNumber in EVEN_NUMBERS ]
print(SQUARES_OF_EVEN_NUMBERS)

# !IMPORTANT
# slicing a list
print(EVEN_NUMBERS[:3]) # prints elements from index 0 to 2 (or first 3)
print(EVEN_NUMBERS[1:]) # prints elements from index 1 till the end of the list
print(EVEN_NUMBERS[1:4]) # prints elements from index 1 to 3
print(EVEN_NUMBERS[-3:]) # print last 3 elements

# we can use for loop with slicing like below
for subsetEvenNumber in EVEN_NUMBERS[:3] :
    print(subsetEvenNumber)

# NOTE for deep copy use slicing like [:]
# Empty lists evaluate to False non-empty evaluates to True
