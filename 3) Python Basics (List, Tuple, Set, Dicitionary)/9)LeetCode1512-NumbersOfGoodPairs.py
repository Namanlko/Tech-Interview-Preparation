# LeetCode 1512 - Number of Good Pairs

class Solution:
    def numIdenticalPairs(self, nums):
        # Initialize counter for good pairs
        count = 0
        # Loop through each element
        for i in range(len(nums)):
            # Compare with elements after index i
            # This avoids checking same pair twice
            for j in range(i + 1, len(nums)):
                # If values are equal, increase count
                if nums[i] == nums[j]:
                    count += 1
        # Return total good pairs
        return count

# -------- Test Cases --------
if __name__ == "__main__":    
    s = Solution()
    # Test Case 1
    # Pairs: (0,3), (1,2), (4,5)
    print(s.numIdenticalPairs([1,2,3,1,1,3]))  # Expected: 4
    # Test Case 2
    print(s.numIdenticalPairs([1,1,1,1]))  # Expected: 6
    # Test Case 3
    print(s.numIdenticalPairs([1,2,3]))  # Expected: 0