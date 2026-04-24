# Problem 17: List prime number between 1 to 100.

def isPrime(n):
    if n<2:
        return False
    else:
        for i in range(2,n):
            if(n%i == 0):
                return False
    return True

n = int(input("Enter Value of n: "))

for i in range(1,n+1):
    if(isPrime(i)):
        print(i, end=" ")