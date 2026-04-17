# LeetCode 771 - Jewels and Stones

class Solution:
    def numJewelsInStones(self, jewels, stones):
        # Counter to store number of jewels found
        count = 0
        # Check each jewel
        for i in range(len(jewels)):
            # Compare with each stone
            for j in range(len(stones)):
                # If jewel matches stone, increase count
                if jewels[i] == stones[j]:
                    count += 1
        # Return total matches
        return count

# -------- Test Cases --------
if __name__ == "__main__":
    s = Solution()
    # Test Case 1
    print(s.numJewelsInStones("aA", "aAAbbbb"))
    # Expected: 3
    # Test Case 2
    print(s.numJewelsInStones("z", "ZZ"))
    # Expected: 0
    # Test Case 3
    print(s.numJewelsInStones("abc", "aabbccdd"))
    # Expected: 6