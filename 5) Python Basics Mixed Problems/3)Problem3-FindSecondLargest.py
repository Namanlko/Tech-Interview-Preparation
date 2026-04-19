# Problem 3: Find Second Largest in List.

nums = [1,2,3,4,5,6,7,8,9,0]
max = -1
secmax = -1
for i in range(len(nums)):
    if (nums[i]>max):
        max = nums[i]

for i in range(len(nums)):
    if(nums[i] < max and nums[i]>secmax):
        secmax = nums[i]
print(secmax)