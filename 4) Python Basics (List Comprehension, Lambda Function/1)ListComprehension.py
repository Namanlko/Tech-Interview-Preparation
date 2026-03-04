# Basic syntax: [expression for item in iterable]

# Traditional way
squares = []
for i in range(10):
    squares.append(i ** 2)

# List comprehension way
squares = [i ** 2 for i in range(10)]

# With condition
# [expression for item in iterable if condition]
even_squares = [i ** 2 for i in range(10) if i % 2 == 0]

# Multiple conditions
nums = [i for i in range(20) if i % 2 == 0 if i % 3 == 0]

# if-else in expression
result = ["Even" if i % 2 == 0 else "Odd" for i in range(5)]

# Nested list comprehension
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
# [[1,2,3], [2,4,6], [3,6,9]]

# Flatten 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
# [1,2,3,4,5,6,7,8,9]

# Dictionary comprehension
squares_dict = {i: i ** 2 for i in range(5)}
# {0:0, 1:1, 2:4, 3:9, 4:16}

# Set comprehension
unique_lengths = {len(word) for word in ["hi", "hello", "hey", "python"]}