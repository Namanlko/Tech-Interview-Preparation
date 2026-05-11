# Problem 19: Second Largest Element in an Array.

def SecondMax(arr):
    n = len(arr)
    max = arr[0]
    for i in range(n):
        if (arr[i]>max):
            max = arr[i]
    secMax = float('-inf')
    for i in range(n):
        if (arr[i]!=max and arr[i]> secMax):
            secMax = arr[i]
    return secMax

arr = [1,2,3,4,5]
print(SecondMax(arr))