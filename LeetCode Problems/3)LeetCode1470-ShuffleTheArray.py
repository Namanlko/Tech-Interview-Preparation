# LeetCode 1470 - Shuffle the Array

class Solution:
    def shuffle(self, nums, n):
        # Create empty list to store result
        result = []
        # Loop from 0 to n-1
        # First half: nums[0 to n-1]
        # Second half: nums[n to 2n-1]
        for i in range(n):  
            # Add element from first half
            result.append(nums[i])
            # Add element from second half
            result.append(nums[i + n])
        # Return shuffled list
        return result
# -------- Test Cases --------
if __name__ == "__main__":
    s = Solution()
    # Test Case 1
    # Input: [2,5,1,3,4,7], n=3
    # Output: [2,3,5,4,1,7]
    print(s.shuffle([2,5,1,3,4,7], 3))  # Expected: [2,3,5,4,1,7]
    # Test Case 2
    # Input: [1,2,3,4,4,3,2,1], n=4
    print(s.shuffle([1,2,3,4,4,3,2,1], 4))  # Expected: [1,4,2,3,3,2,4,1]
    # Test Case 3
    # Input: [1,1,2,2], n=2
    print(s.shuffle([1,1,2,2], 2))  # Expected: [1,2,1,2]