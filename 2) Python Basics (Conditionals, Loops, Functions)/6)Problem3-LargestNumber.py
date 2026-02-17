# Problem 3: Largest of 3: Find largest among 3 numbers.

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

if a>b:
    if b>c:
        max = a
    else:
        max = c
elif b>c:
    max = b
else:
    max = c

print("Largest Number is",max)