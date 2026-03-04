# Problem 1: Square of Even Numbers: Use list comprehension to get squares of even numbers from 1 to 20.

list = [i**2 for i in range(1,21) if i%2==0]
print(list)