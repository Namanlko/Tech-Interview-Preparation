# Creating sets (unique, unordered)
numbers = {1, 2, 3, 4, 5}
fruits = {"apple", "banana", "cherry"}
empty_set = set()  # Note: {} creates empty dict

# Adding/Removing
fruits.add("orange")
fruits.remove("banana")         # Error if not found
fruits.discard("mango")         # No error if not found
popped = fruits.pop()           # Remove random element

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1 | set2)              # Union: {1,2,3,4,5,6}
print(set1 & set2)              # Intersection: {3,4}
print(set1 - set2)              # Difference: {1,2}
print(set1 ^ set2)              # Symmetric difference: {1,2,5,6}

# Checking membership
print(3 in set1)                # True
print(7 not in set1)            # True

# Set from list (removes duplicates)
nums = [1, 2, 2, 3, 3, 3, 4]
unique = set(nums)              # {1, 2, 3, 4}