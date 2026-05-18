# Problem 20: Display the Longest Name from a list of strings.

def LonggestName(name):
    max = 0
    for i in range(len(name)):
        if (len(name[i]) > max):
            max = len(name[i])
            index = i
    return name[index]

name = ["Naman", "Abhishek", "Riya", "Raj", "Arjun", "Priyanka", "Raj Vikram Aditya"]
print(LonggestName(name))