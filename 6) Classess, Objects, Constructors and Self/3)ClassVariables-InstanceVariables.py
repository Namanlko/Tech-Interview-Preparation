class Employee:
    # Class variable (shared by all instances)
    company_name = "Tech Corp"
    employee_count = 0
    
    def __init__(self, name, salary):
        # Instance variables (unique to each instance)
        self.name = name
        self.salary = salary
        Employee.employee_count += 1
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Company: {Employee.company_name}")

# Creating objects
emp1 = Employee("Arjun", 50000)
emp2 = Employee("Priya", 60000)

print(Employee.employee_count)  # 2

# Accessing Display Function.
emp1.display_info()
emp2.display_info()

# Accessing class variable
print(Employee.company_name)    # "Tech Corp"
print(emp1.company_name)        # "Tech Corp"

# Modifying class variable
Employee.company_name = "Tech Solutions"
print(emp1.company_name)        # "Tech Solutions"
print(emp2.company_name)        # "Tech Solutions"