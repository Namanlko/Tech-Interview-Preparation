# Problem 5: Filter Names: Given list of names, filter names starting with 'A' using filter and lambda.

names = ["Aman", "Naman", "Ankit", "Abhinav", "Ohm", "Vishal", "Aditya"]
result = list(filter(lambda x: x[0]=='A' or x[0]=='a', names))
print(result)