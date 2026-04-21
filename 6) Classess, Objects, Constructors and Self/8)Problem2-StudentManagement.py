# Problem 2: 
"""
Create Student class with:
- Constructor: name, roll_no, marks (list of 5 subjects)
- Methods: 
  - calculate_total()
  - calculate_percentage()
  - get_grade() - based on percentage
  - display_report()
"""
    
class Student:
    
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    
    def calculate_total(self):
        total = 0
        for i in range(len(self.marks)):
            total += self.marks[i]
        return total
    
    def calculate_percentage(self):
        total = self.calculate_total()
        return (total / 500) * 100
    
    def get_grade(self):
        grade = self.calculate_percentage()
        
        if grade >= 90:
            return 'A'
        elif grade >= 80:
            return 'B'
        elif grade >= 70:
            return 'C'
        elif grade >= 60:
            return 'D'
        else:
            return 'F'
    
    def display_report(self):
        print("Student Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)
        print("Total:", self.calculate_total())
        print("Percentage:", self.calculate_percentage())
        print("Grade:", self.get_grade())

s = Student("Aman", 103, [60, 70, 80, 90, 100])
s.display_report()