# Problem 13: Armstrong Number: Check if number is Armstrong number.

def Is_Armstrong(n):
    num_str = str(n)
    power = len(num_str)
    total = 0

    for digit in num_str:
        total += int(digit) ** power

    return total == n

num = int(input("Enter number: "))

if Is_Armstrong(num):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
