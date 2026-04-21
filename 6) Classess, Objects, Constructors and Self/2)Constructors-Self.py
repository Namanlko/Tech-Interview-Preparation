# Proper class with constructor
class Student:
    # Constructor - called when object is created
    def __init__(self, name, roll_no, marks):
        self.name = name        # Instance variable
        self.roll_no = roll_no
        self.marks = marks
    
    # Instance method
    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")
    
    def get_grade(self):
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 80:
            return 'B'
        elif self.marks >= 70:
            return 'C'
        else:
            return 'F'

# Creating objects
s1 = Student("Arjun", 101, 85)
s2 = Student("Priya", 102, 92)

# Calling methods
s1.display()
print(f"Grade: {s1.get_grade()}")

s2.display()
print(f"Grade: {s2.get_grade()}")

# Accessing attributes
print(s1.name)  # "Arjun"
s1.marks = 95   # Modifying attribute
s1.display()
print(f"Grade: {s1.get_grade()}")