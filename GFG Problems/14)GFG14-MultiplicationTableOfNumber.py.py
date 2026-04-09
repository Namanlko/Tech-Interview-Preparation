# Problem 14: Program for multiplication table.

n = int(input("Enter Number: "))
for i in range(1,11):
    print(n,"X",i,"=",(n*i),end="\n")