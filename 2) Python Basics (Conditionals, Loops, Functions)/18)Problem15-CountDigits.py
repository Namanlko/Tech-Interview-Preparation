# Problem 15: Count Digits: Count number of digits in a number.

def count_digits(n):
    if n == 0:
        return 1
    
    count = 0
    n = abs(n)   # handle negative numbers
    
    while n > 0:
        n = n // 10
        count += 1
    
    return count


num = int(input("Enter number: "))
print("Number of digits:", count_digits(num))
