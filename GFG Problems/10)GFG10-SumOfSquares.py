# Problem 10: Difference between sum of the squares of first n natural numbers and square of sum.

n = int(input("Enter Value of n: "))
sum1 = 0
sum2 = 0

for i in range(1,n+1):
    sum1 += i
    sum2 += i**2

result = abs((sum1**2) - sum2)
print(result)