# Problem 7: Sum of N numbers: Calculate sum of first N natural numbers.

n = int(input("Enter Number: "))
sum = 0

for i in range(n+1):
    sum = sum + i

print("Sum =",sum)