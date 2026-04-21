# Problem 5:
"""
Create Temperature class with:
- Constructor: value, unit ('C' or 'F')
- Methods: to_celsius(), to_fahrenheit(), to_kelvin()
- __str__ method for display
"""

class Temperature:
    
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit.upper()  # normalize to C or F

    def to_celsius(self):
        if self.unit == 'C':
            return self.value
        elif self.unit == 'F':
            return (self.value - 32) * 5/9
        else:
            return None

    def to_fahrenheit(self):
        if self.unit == 'F':
            return self.value
        elif self.unit == 'C':
            return (self.value * 9/5) + 32
        else:
            return None

    def to_kelvin(self):
        celsius = self.to_celsius()
        return celsius + 273.15

    def __str__(self):
        return f"{self.value}°{self.unit}"
    

t1 = Temperature(100, 'C')
t2 = Temperature(212, 'F')

print(t1)  # 100°C
print("Celsius:", t1.to_celsius())
print("Fahrenheit:", t1.to_fahrenheit())
print("Kelvin:", t1.to_kelvin())

print("-----")

print(t2)  # 212°F
print("Celsius:", t2.to_celsius())
print("Fahrenheit:", t2.to_fahrenheit())
print("Kelvin:", t2.to_kelvin())