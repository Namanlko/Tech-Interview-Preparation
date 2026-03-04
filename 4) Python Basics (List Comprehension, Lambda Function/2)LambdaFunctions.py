# Anonymous functions: lambda arguments: expression

# Regular function
def add(x, y):
    return x + y

# Lambda equivalent
add = lambda x, y: x + y
print(add(5, 3))  # 8

# Common use cases

# 1. With map() - apply function to all items
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
# [1, 4, 9, 16, 25]

# 2. With filter() - filter items based on condition
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4]

# 3. With sorted() - custom sorting
students = [
    {"name": "Arjun", "marks": 85},
    {"name": "Priya", "marks": 92},
    {"name": "Rahul", "marks": 78}
]
sorted_students = sorted(students, key=lambda s: s["marks"], reverse=True)

# 4. With reduce() - accumulate values
from functools import reduce
sum_all = reduce(lambda x, y: x + y, numbers)
# 15

# Multiple arguments
multiply = lambda x, y, z: x * y * z
print(multiply(2, 3, 4))  # 24

# Lambda with conditionals
max_val = lambda a, b: a if a > b else b
print(max_val(10, 20))  # 20