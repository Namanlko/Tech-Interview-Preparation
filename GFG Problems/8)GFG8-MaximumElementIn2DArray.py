# Problem 8: Program to find the maximum element in a Matrix.

import sys

def Max(mat):
    max = -sys.maxsize - 1
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] > max:
                max = mat[i][j]
    return max

ma = [[1,2,3],[4,5,6],[7,8,9]]
print(Max(ma))