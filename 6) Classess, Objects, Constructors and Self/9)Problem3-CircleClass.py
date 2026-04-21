# Problem 3:
"""
Create Circle class with:
- Constructor: radius
- Methods: area(), circumference(), diameter()
- Use class variable for PI value
"""

class Circle:
    pi = 3.14
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return self.pi * self.radius * self.radius
    def circumference(self):
        return 2 * self.pi * self.radius
    def diameter(self):
        return 2 * self.radius

c1 = Circle(3)
print("Area:",c1.area())    
print("Circumference:",c1.circumference())    
print("Diameter:",c1.diameter())    