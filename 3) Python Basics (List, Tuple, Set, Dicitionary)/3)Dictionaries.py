# Creating dictionaries (key-value pairs)
student = {
    "name": "Arjun",
    "age": 25,
    "grade": "A"
}

# Accessing values
print(student["name"])          # "Arjun"
print(student.get("age"))       # 25
print(student.get("marks", 0))  # 0 (default if key not found)

# Adding/Updating
student["city"] = "Delhi"       # Add new key
student["age"] = 26             # Update existing

# Dictionary methods
student.update({"grade": "A+", "course": "CSE"})
print(student.keys())           # Get all keys
print(student.values())         # Get all values
print(student.items())          # Get (key, value) pairs
removed = student.pop("city")   # Remove and return value
student.clear()                 # Remove all items

# Iterating
student = {"name": "Arjun", "age": 25}
for key in student:
    print(key, student[key])

for key, value in student.items():
    print(f"{key}: {value}")

# Nested dictionaries
users = {
    "user1": {"name": "Arjun", "age": 25},
    "user2": {"name": "Priya", "age": 23}
}
print(users["user1"]["name"])  # "Arjun"