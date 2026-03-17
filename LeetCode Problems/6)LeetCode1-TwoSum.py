# LeetCode 1 - Two Sum

class Solution:
    def twoSum(self, nums, target):
        # Get length of list
        n = len(nums)
        # Loop through each element
        for i in range(n - 1):
            # Compare with elements after index i
            for j in range(i + 1, n):
                # Check if sum equals target
                if nums[i] + nums[j] == target:
                    return [i, j]
        # If no pair found, return empty list
        return []

# -------- Test Cases --------
if __name__ == "__main__":    
    s = Solution()
    # Test Case 1
    print(s.twoSum([2,7,11,15], 9))  
    # Expected: [0,1]
    # Test Case 2
    print(s.twoSum([3,2,4], 6))  
    # Expected: [1,2]
    # Test Case 3
    print(s.twoSum([3,3], 6))  
    # Expected: [0,1]