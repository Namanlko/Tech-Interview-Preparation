# Input (always returns string)
name = input("Enter your name: ")
age = int(input("Enter your age: "))  # Convert to int
marks = float(input("Enter marks: "))  # Convert to float

# Output
print("Hello World")
print("Name:", "Arjun", "Age:", 25)
print(f"My name is {name} and I'm {age} years old")  # f-strings
print("Value: {}".format(100))  # format method