# Problem 10: Fibonacci Series: Print first N fibonacci numbers.

n = int(input("Enter Value of n?"))

a = 0
b = 1

if n<=0:
    print("Enter Positive Number")
elif n==1:
    print(a)
else:
    print(a,b,end=" ")
    for i in range(2,n):
        c = a + b
        print(c, end=" ")
        a = b
        b = c
