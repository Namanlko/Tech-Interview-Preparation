# for loop
for i in range(5):          # 0 to 4
    print(i)

for i in range(2, 10):      # 2 to 9
    print(i)

for i in range(1, 10, 2):   # 1, 3, 5, 7, 9
    print(i)

# Iterating over string
for char in "Python":
    print(char)

# while loop
count = 0
while count < 5:
    print(count)
    count += 1

# break and continue
for i in range(10):
    if i == 5:
        break       # Exit loop
    if i == 3:
        continue    # Skip this iteration
    print(i)

# Nested loops
for i in range(3):
    for j in range(3):
        print(f"({i},{j})", end=" ")
    print()