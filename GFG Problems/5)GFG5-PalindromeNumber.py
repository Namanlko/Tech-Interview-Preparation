# Problem 5: Check if a number is Palindrome.

n = int(input("Enter Number: "))
num = n
sum = 0

while(n>0):
    sum = (sum * 10) + (n%10)
    n = n//10

if (sum==num):
    print("Palindrome")
else:
    print("Not Palindrome")