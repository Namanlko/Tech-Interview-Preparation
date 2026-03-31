# Problem 12: Factorial of a Number.

def Fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

print(Fact(1))
print(Fact(2))
print(Fact(3))
print(Fact(4))
print(Fact(5))