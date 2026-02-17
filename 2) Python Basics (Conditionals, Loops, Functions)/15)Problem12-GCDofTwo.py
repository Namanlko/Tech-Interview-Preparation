# Problem 12: GCD Calculator: Find GCD of two numbers.

def gcd(a, b):
    smallest = min(a, b)
    
    for i in range(smallest, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("GCD is:", gcd(num1, num2))
