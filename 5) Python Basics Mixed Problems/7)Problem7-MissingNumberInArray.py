# Problem 7: Find Missing Number in Array (1 to N)

def Missing_Number(arr,N):
    expected_sum = (N*(N+1))/2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

print(Missing_Number([1, 2, 3, 5, 6, 7, 8, 9, 10], 10))  # Expected: 4
print(Missing_Number([2, 3, 4, 5], 5))  # Expected: 1