# LeetCode 1431 - Kids With the Greatest Number of Candies.

class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        # Find the current maximum candies any kid has
        maximum = max(candies)
        # Create empty list to store True/False results
        result = []
        # Check for each kid
        for i in range(len(candies)):
            # If after adding extraCandies,
            # the kid has >= maximum, append True
            if candies[i] + extraCandies >= maximum:
                result.append(True)
            else:
                result.append(False)
        # Return final boolean list
        return result

# -------- Test Cases --------
if __name__ == "__main__":
    s = Solution()
    # Test Case 1
    # Maximum = 5
    print(s.kidsWithCandies([2,3,5,1,3], 3))
    # Expected: [True, True, True, False, True]
    # Test Case 2
    print(s.kidsWithCandies([4,2,1,1,2], 1))
    # Expected: [True, False, False, False, False]
    # Test Case 3
    print(s.kidsWithCandies([12,1,12], 10))

    # Expected: [True, False, True]
