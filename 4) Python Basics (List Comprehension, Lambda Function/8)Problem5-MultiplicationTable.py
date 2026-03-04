# Problem 5: Nested List Comprehension: Create multiplication table (1-10) using nested list comprehension.

table = [[i * j for i in range(1, 11)] for j in range(1, 11)]
for row in table:
    print(row)