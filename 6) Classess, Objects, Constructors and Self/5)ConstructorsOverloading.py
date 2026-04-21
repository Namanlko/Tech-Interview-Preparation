class Rectangle:
    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

# Different ways to create objects
r1 = Rectangle()           # length=0, width=0
print(r1.area())
print(r1.perimeter())

r2 = Rectangle(10)         # length=10, width=0
print(r2.area())
print(r2.perimeter())

r3 = Rectangle(10, 5)      # length=10, width=5
print(r3.area())
print(r3.perimeter())

r4 = Rectangle(width=7, length=3)  # Named arguments
print(r4.area())
print(r4.perimeter())