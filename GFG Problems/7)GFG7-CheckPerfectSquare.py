# Problem 7: Check if given number is perfect square.

def PerfectSquare(n):
    if n>0:
        s = int(n ** 0.5)
        if (s*s) == n:
            return True
    return False

print(PerfectSquare(64))
print(PerfectSquare(4))
print(PerfectSquare(16))
print(PerfectSquare(20))