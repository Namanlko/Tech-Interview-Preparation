# Problem 9: Sum of Digits of a Number.

n = int(input("Enter Number: "))
num = str(n)

sum = 0
for i in range(len(num)):
    sum += int(num[i])

print(sum)