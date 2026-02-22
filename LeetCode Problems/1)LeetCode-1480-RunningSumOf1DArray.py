# LeetCode 1480 - Running Sum of 1d Array

class Solution:
    def runningSum(self, nums):
        # Loop starts from index 1 (second element)
        # Because first element remains same
        for i in range(1, len(nums)):
            # Add previous element value to current element
            # Example: nums[i] = nums[i] + nums[i-1]
            nums[i] = nums[i] + nums[i - 1]
        # Return updated list
        return nums

# -------- Test Cases --------
if __name__ == "__main__":
    s = Solution()
    # Test case 1
    # 1 -> 1
    # 2 -> 1+2 = 3
    # 3 -> 3+3 = 6
    # 4 -> 6+4 = 10
    print(s.runningSum([1, 2, 3, 4]))        # Output: [1, 3, 6, 10]
    # Test case 2
    print(s.runningSum([1, 1, 1, 1, 1]))     # Output: [1, 2, 3, 4, 5]
    # Test case 3
    print(s.runningSum([3, 1, 2, 10, 1]))    # Output: [3, 4, 6, 16, 17]