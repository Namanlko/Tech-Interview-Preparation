# Problem 3: Program to print the given digit in words

def printValue(n):
    if n==0:
        print("Zero", end=" ")
    elif n==1:
        print("One", end=" ")
    elif n==2:
        print("Two", end=" ")
    elif n==3:
        print("Three", end=" ")
    elif n==4:
        print("Four", end=" ")
    elif n==5:
        print("Five", end=" ")
    elif n==6:
        print("Six", end=" ")
    elif n==7:
        print("Seven", end=" ")
    elif n==8:
        print("Eight", end=" ")
    elif n==9:
        print("Nine", end=" ")

n = input("Enter Number: ")

for i in range(len(n)):
    printValue(int(n[i]))
