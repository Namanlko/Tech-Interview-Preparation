# Problem 3: Sort by Second Element: Sort list of tuples by second element using lambda

# data = [(1, 5), (3, 2), (2, 8), (4, 1)]
# Output: [(4, 1), (3, 2), (1, 5), (2, 8)]

data = [(1, 5), (3, 2), (2, 8), (4, 1)]
# Sort by second element
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)