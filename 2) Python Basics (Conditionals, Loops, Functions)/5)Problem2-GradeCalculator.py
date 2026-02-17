# Problem 2: Grade Calculator: Assign grade based on marks.

marks = int(input("Enter Marks:"))

if marks>=90:
    grade = 'A'
elif marks>=80 and marks<90:
    grade = 'B'
elif marks>=60 and marks<80:
    grade = 'C'
elif marks>=40 and marks<60:
    grade = 'D'
else:
    grade = 'E'
    
print("Grade is",grade)