# if-else
age = 18
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")

# if-elif-else
marks = 85
if marks >= 90:
    grade = 'A'
elif marks >= 80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
else:
    grade = 'F'

# Nested if
num = 15
if num > 0:
    if num % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")

# Ternary operator
result = "Even" if num % 2 == 0 else "Odd"