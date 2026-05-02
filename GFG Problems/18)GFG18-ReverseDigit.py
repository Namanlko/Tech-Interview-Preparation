# Problem 18: Write a program to reverse digits of a number.

def Reverse(n):
    sum = 0
    while(n>0):
        sum = sum *10 + n%10
        n = n//10
    return sum

print(Reverse(321))