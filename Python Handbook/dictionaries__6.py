"""dictionary related methods and manipulation"""
# A dictionary in python is a collection of key value pair

apple = { "color": "red", "weight": 200 }

# we can access value by key
print(apple["color"])

# adding a new value
apple["smell"] = "sweet"

# define empty dictionary like below
orange: dict = {}

# for modifying the value, access the value by key and assing it a value
apple["color"] = "brown"

# to remove key value pair use del
del apple["smell"]

# we can use items to loop through all the key value pairs
for key, value in apple.items():
    print("\nkey :" + key)
    print("value: " + str(value))

# for looping through or getting all keys use keys()
apple.keys()
# for looping through or getting all values use values()
apple.values()

# for looping through the dictionary in order, use sorted on keys
for key in sorted(apple.keys()):
    print(apple[key])

# for getting non repetitive values inside dictionary, we can wrap the statement around set()
for value in set(apple.values()):
    print(value)

# Nesting is allowed in dictionaries, several scenarios that are valid are:
# - A list of dictionaries
# - A list in a dictionary
# - A dictionary in a dictionary
