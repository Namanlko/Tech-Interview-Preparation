# Problem 9: Prime Number: Check if number is prime.

n = int(input("Enter Number: "))

if n<2:
    prime = False
else:
    prime = True
    for i in range(2,n):
        if(n%i == 0):
            prime = False
            break

if(prime):
    print("Prime Number")
else:
    print("Not Prime Number")