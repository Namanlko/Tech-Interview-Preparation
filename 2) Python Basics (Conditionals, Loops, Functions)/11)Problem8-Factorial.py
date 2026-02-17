# Problem 8: Factorial: Calculate factorial using loop.

n = int(input("Enter Number: "))
fact = 1
for i in range(n):
    fact = fact * (i+1)

print("Factorial =",fact)