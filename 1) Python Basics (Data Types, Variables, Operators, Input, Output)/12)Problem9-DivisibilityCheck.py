# Problem 12: Divisibility Check: Check if number is divisible by both 3 and 5.

n = int(input("Enter Number :)"))

if (n%3 == 0 and n%5 == 0):
    print("Number is Divisible by both 3 and 5.")
else:
    print("Number is not Divisible by both 3 and 5.")