# Problem 6: Print Pattern: Print right-angled triangle pattern.

n = int(input("Enter Number: "))

for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print(end="\n")