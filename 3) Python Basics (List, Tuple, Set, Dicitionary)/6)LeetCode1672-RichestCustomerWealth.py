# LeetCode 1672 - Richest Customer Wealth

class Solution:
    def maximumWealth(self, accounts):
        # Variable to store maximum wealth found
        rich = 0
        # Loop through each customer's account list
        for customer in accounts:
            # Calculate total money of current customer
            total = sum(customer)
            # Update richest value if current total is greater
            rich = max(rich, total)
        # Return maximum wealth
        return rich

# -------- Test Cases --------
if __name__ == "__main__":
    
    s = Solution()
    # Test Case 1
    # Customer 1: 1+2+3 = 6
    # Customer 2: 3+2+1 = 6
    # Output: 6
    print(s.maximumWealth([[1,2,3],[3,2,1]]))  # Expected: 6
    # Test Case 2
    # Customer 1: 1+5 = 6
    # Customer 2: 7+3 = 10
    # Customer 3: 3+5 = 8
    # Output: 10
    print(s.maximumWealth([[1,5],[7,3],[3,5]]))  # Expected: 10
    # Test Case 3
    print(s.maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))  # Expected: 17