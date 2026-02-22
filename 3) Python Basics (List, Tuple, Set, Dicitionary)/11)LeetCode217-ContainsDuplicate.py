# LeetCode 217 - Contains Duplicate

class Solution:
    def containsDuplicate(self, nums):
        # Get length of list
        n = len(nums)
        # Compare each element with elements after it
        for i in range(n - 1):
            for j in range(i + 1, n):
                # If any two elements are equal, duplicate exists
                if nums[i] == nums[j]:
                    return True
        # If no duplicates found
        return False

# -------- Test Cases --------
if __name__ == "__main__":
    s = Solution()
    # Test Case 1
    print(s.containsDuplicate([1,2,3,1]))  
    # Expected: True
    # Test Case 2
    print(s.containsDuplicate([1,2,3,4]))  
    # Expected: False
    # Test Case 3
    print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))  
    # Expected: True