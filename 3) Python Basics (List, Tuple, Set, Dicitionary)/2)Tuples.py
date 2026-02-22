# Creating tuples (immutable)
coordinates = (10, 20)
single = (5,)           # Single element tuple
person = ("Arjun", 25, "Delhi")

# Accessing elements
print(coordinates[0])   # 10
print(person[-1])       # "Delhi"

# Tuple methods
numbers = (1, 2, 3, 2, 4, 2)
print(numbers.count(2))     # 3
print(numbers.index(3))     # 2

# Tuple unpacking
name, age, city = person
x, y = coordinates

# Tuples are immutable
# coordinates[0] = 15  # Error!

# But can create new tuple
new_coords = (15, 20)