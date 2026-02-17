# Basic function
def greet():
    print("Hello!")

greet()  # Function call

# Function with parameters
def add(a, b):
    return a + b

result = add(5, 3)  # 8

# Default parameters
def power(base, exp=2):
    return base ** exp

print(power(5))      # 25 (5^2)
print(power(5, 3))   # 125 (5^3)

# Multiple return values
def get_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([1, 5, 3, 9, 2])

# *args and **kwargs
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))  # 15

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Arjun", age=25, city="Delhi")

# Recursive function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120