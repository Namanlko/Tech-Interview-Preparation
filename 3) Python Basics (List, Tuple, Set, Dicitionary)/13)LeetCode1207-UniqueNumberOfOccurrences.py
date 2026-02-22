# LeetCode 1207 - Unique Number of Occurrences

class Solution:
    def uniqueOccurrences(self, arr):
        flag = False
        n = len(arr)        
        for i in range(n - 1):
            for j in range(i + 1, n):
                if arr[i] == arr[j]:
                    flag = True
        return flag

# -------- Test Cases --------
if __name__ == "__main__":    
    s = Solution()
    # Test Case 1
    print(s.uniqueOccurrences([1,2,2,1,1,3]))
    # Test Case 2
    print(s.uniqueOccurrences([1,2]))
    # Test Case 3
    print(s.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))