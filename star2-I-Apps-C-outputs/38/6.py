
from functools import lru_cache

@lru_cache(maxsize=None)
def solve(n, k):
    if n == 1:
        return 1
    if k == 0:
        return 0
    if n & 1:
        return solve(n >> 1, k - 1)
    return solve(n >> 1, k) + solve(n >> 1, k - 1)

n, k = map(int, input().split())
print(solve(n, k) % (10**9 + 7))

