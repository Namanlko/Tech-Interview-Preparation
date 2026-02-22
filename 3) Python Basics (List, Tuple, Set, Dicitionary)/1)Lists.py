# Creating lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
empty = []

# Accessing elements
print(fruits[0])        # "apple" (indexing)
print(fruits[-1])       # "cherry" (negative indexing)
print(fruits[0:2])      # ["apple", "banana"] (slicing)

# List methods
fruits.append("orange")         # Add at end
fruits.insert(1, "mango")       # Insert at index
fruits.remove("banana")         # Remove specific item
popped = fruits.pop()           # Remove and return last item
fruits.pop(0)                   # Remove at index
fruits.clear()                  # Remove all items

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()                  # Sort in place
numbers.reverse()               # Reverse in place
print(numbers.count(1))         # Count occurrences
print(numbers.index(4))         # Find index of element

# List operations
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2        # Concatenation
repeated = list1 * 3            # Repetition
print(len(list1))               # Length
print(max(numbers))             # Maximum
print(min(numbers))             # Minimum
print(sum(numbers))             # Sum

# Nested lists (2D arrays)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][2])  # 6