# Problem 11: Program for Armstrong Numbers.

n = int(input("Enter Number: "))
num = str(n)
power = len(num)

total = 0
for digit in num:
    total += int(digit) ** power

if total == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")