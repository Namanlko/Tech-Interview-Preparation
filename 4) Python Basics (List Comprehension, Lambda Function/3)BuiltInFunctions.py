numbers = [1, 2, 3, 4, 5]

# map() - transform each element
doubled = list(map(lambda x: x * 2, numbers))

# filter() - keep elements that satisfy condition
greater_than_2 = list(filter(lambda x: x > 2, numbers))

# zip() - combine multiple iterables
names = ["Arjun", "Priya", "Rahul"]
ages = [25, 23, 27]
combined = list(zip(names, ages))
# [('Arjun', 25), ('Priya', 23), ('Rahul', 27)]

# enumerate() - get index and value
for idx, name in enumerate(names):
    print(f"{idx}: {name}")

# all() - check if all elements are True
print(all([True, True, True]))    # True
print(all([True, False, True]))   # False

# any() - check if any element is True
print(any([False, False, True]))  # True
print(any([False, False, False])) # False