
from math import log2
def solve(n, k):
    n = int(n, 2)
    res = 0
    for i in range(1, n + 1):
        if bin(i).count('1') == k:
            res += 1
    return res % (10**9 + 7)

n = input()
k = int(input())
print(solve(n, k))

