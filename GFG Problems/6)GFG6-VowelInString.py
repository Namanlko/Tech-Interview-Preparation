# Problem 6: Program to count vowels in a string.

str = input("Enter String: ")

def VowelCount(str):
    count = 0
    for i in str:
        if i=="a":
            count +=1
        elif i=="e":
            count +=1
        elif i=="i":
            count +=1
        elif i=="o":
            count +=1
        elif i=="u":
            count +=1
        elif i=="A":
            count +=1
        elif i=="E":
            count +=1
        elif i=="I":
            count +=1
        elif i=="O":
            count +=1
        elif i=="U":
            count +=1
    return count

print(VowelCount(str))


