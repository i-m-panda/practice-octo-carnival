"""storing data in json file and reading data"""
from json import dump, load
# you can use json.dump() to store data and json.load() to read json data

# writing to json file
even_numbers = [even for even in range(2, 11, 2)]
with open("even.json", "w", encoding="utf-8") as file_object:
    dump(even_numbers, file_object)

# reading from a jsson file
with open("even.json", "r", encoding="utf-8") as file_object:
    loaded_even_numbers = load(file_object)

print(loaded_even_numbers)
