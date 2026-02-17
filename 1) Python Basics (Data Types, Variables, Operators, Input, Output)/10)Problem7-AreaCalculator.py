# Problem 7: Area Calculator: Calculate area of circle, rectangle, triangle.

# Area of Circle.
r = float(input("Enter Value of Radius :"))
ac = 3.14 * r * r
print("Area of Circle = ",ac)

# Area of Rectangle.
a = float(input("Enter Value of Length :"))
b = float(input("Enter Value of Breath :"))
ar = a * b
print("Area of Rectangle = ",ar)

# Area of Triangle.
l = float(input("Enter Value of Base :"))
h = float(input("Enter Value of height :"))
at = 0.5 * l * h
print("Area of Triangle = ",at)