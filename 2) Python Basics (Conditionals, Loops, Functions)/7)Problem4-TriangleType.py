# Problem 4: Triangle Type: Check if triangle is equilateral, isosceles, or scalene.

a = int(input("Enter 1st Side: "))
b = int(input("Enter 2nd Side: "))
c = int(input("Enter 3rd Side: "))

if (a==b and b ==c):
    print("Equilateral Triangle")
elif (a==b or b==c or c==a):
    print("Isosceles Triangle")
else:
    print("Scalene Triangle") 