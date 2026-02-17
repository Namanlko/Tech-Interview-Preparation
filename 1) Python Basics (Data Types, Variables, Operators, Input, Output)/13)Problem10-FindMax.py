# Problem 13: Find Maximum: Find max of 3 numbers using comparison operators.

a = int(input("Enter First Number :)"))
b = int(input("Enter Second Number :)"))
c = int(input("Enter Third Number :)"))

if a>b:
    if a>c:
        max = a
    else:
        max = c
elif b>c:
    max = b
else:
    max = c

print("Maximum Number is",max)