# LeetCode 349 - Intersection of Two Arrays

class Solution:
    def intersection(self, nums1, nums2):
        # Create empty list to store result
        result = []
        # Convert both lists into sets (removes duplicates)
        nums1 = set(nums1)
        nums2 = set(nums2)
        # Check each element of nums1
        for i in nums1:
            # If element exists in nums2, add to result
            if i in nums2:
                result.append(i)
        # Return final intersection list
        return result

# -------- Test Cases --------
if __name__ == "__main__":    
    s = Solution()
    # Test Case 1
    print(s.intersection([1,2,2,1], [2,2]))
    # Expected: [2]
    # Test Case 2
    print(s.intersection([4,9,5], [9,4,9,8,4]))
    # Expected: [9,4] (order may vary)
    # Test Case 3
    print(s.intersection([1,3,5,7], [2,4,6,8]))
    # Expected: []