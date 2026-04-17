# Problem 16: Segregate 0s and 1s in an array.

def Segregate(arr):
    count = 0
    for i in range(len(arr)):
        if (arr[i] == 0):
            count += 1
    for i in range(count):
        arr[i] = 0
    for i in range(count,len(arr)):
        arr[i] = 1
    return arr

arr = [1,0,1,0,1,0,1,0]
print(Segregate(arr))