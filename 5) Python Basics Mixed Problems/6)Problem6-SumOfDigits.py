# Problem 6: Calculate the sum of digits.

def DigitSum(num):
    total = 0
    while num > 0:
        d = num % 10
        total += d
        num = num // 10
    return total

print(DigitSum(123))
print(DigitSum(1234))
print(DigitSum(12345))