class Calculator:
    pi = 3.14159  # Class variable
    
    def __init__(self, brand):
        self.brand = brand
    
    # Instance method (needs self)
    def add(self, a, b):
        return a + b
    
    # Class method (works with class variables)
    @classmethod
    def circle_area(cls, radius):
        return cls.pi * radius * radius
    
    # Static method (doesn't need self or cls)
    @staticmethod
    def is_even(num):
        return num % 2 == 0

# Using methods
calc = Calculator("Casio")

# Instance method
print(calc.add(5, 3))  # 8

# Class method
print(Calculator.circle_area(5))  # 78.53975
print(calc.circle_area(5))  # 78.53975

# Static method
print(Calculator.is_even(4))  # True
print(calc.is_even(7))        # False