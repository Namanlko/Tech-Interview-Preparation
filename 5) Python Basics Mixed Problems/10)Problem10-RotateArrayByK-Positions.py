# Problem 10: Rotate Array by K positions.

def Rotate_Array_Left(arr,k):
    n = len(arr)
    k = k%n
    return arr[k:] + arr[:k]

def Rotate_Array_Right(arr,k):
    n = len(arr)
    k = k%n
    if k==0:
        return arr
    return arr[-k:] + arr[:-k]

print(Rotate_Array_Left([1, 2, 3, 4, 5], 2))  
# Expected: [3, 4, 5, 1, 2]
print(Rotate_Array_Right([1, 2, 3, 4, 5], 2))  
# Expected: [4, 5, 1, 2, 3]