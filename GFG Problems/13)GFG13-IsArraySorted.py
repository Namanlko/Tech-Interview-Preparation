# Problem 13: Check if an Array is Sorted in ascending order.

def IsSorted(arr):
    n = len(arr)
    for i in range(n-1):
        if (arr[i]>arr[i+1]):
            return False
    return True

arr1 = [1,2,3,4,5]
arr2 = [4,2,3,4,5]
arr3 = [1,2,5,4,2]

print(IsSorted(arr1))
print(IsSorted(arr2))
print(IsSorted(arr3))