# Problem 2: Program for average of an array.

arr = [1,2,3,4,5,6,7,8,9,10]

n = len(arr)
sum = 0

for i in range(n):
    sum = sum + arr[i]

print("Average Value is",(sum/n))