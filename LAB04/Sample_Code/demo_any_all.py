'''
    The any(iter) and all(iter) built-ins look at the truth values of an iterable’s contents.
    any() returns True if any element in the iterable is a true value, and 
    all() returns True if all of the elements are true values
'''

numbers = [4, 2, 11, 4, 9]

result = any(num > 10 for num in numbers)
print(result)  # Output: True (because 11 is greater than 10)


result = all(num > 0 for num in numbers)
print(result)  # Output: True (all numbers are positive)


'''More examples with any() and all() '''

animals = [
    {'type': 'Dog', 'name': 'Lucy'},
    {'type': 'Cat', 'name': 'Buddy'},
    {'type': 'Rabbit', 'name': 'Jack'},
    {'type': 'Cat', 'name': 'Duke'},
    {'type': 'Rabbit', 'name': 'Sadie'},
    {'type': 'Dog', 'name': 'Bella'},
]


allIsDog = all(map(lambda animal: animal['type'] == 'Dog', animals))
print(allIsDog)


filterDogs = [i for i in animals if i['type'] == 'Dog']
allIsDog = all(map(lambda animal: animal['type'] == 'Dog', filterDogs))
print(allIsDog)


anyIsDog = any(map(lambda animal: animal['type'] == 'Dog', animals))
print(anyIsDog)


anyIsHamster = any(map(lambda animal: animal['type'] == 'Hamster', animals))
print(anyIsHamster)
