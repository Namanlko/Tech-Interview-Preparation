# Problem 1: Count number of even and odd elements in an array

list = [1,2,3,4,5,6,8,10]

evenCount = 0
oddCount = 0
for i in range(len(list)):
    if list[i]%2==0:
        evenCount = evenCount + 1
    else:
        oddCount = oddCount + 1

print(evenCount)
print(oddCount)