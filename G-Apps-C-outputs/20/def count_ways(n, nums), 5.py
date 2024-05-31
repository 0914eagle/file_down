
from math import gcd
MOD = 10**9 + 7

def count_ways(n, nums):
    def dfs(i, j):
        if i == j:
            return 1
        res = 0
        for k in range(i+1, j+1):
            if gcd(nums[i], nums[k]) > 1:
                res += dfs(k, j)
                res %= MOD
        return res

    total_ways = 0
    for i in range(n):
        total_ways += dfs(i, (i+n-1) % n)
        total_ways %= MOD
    return total_ways

# Reading input
n = int(input())
nums = [int(input()) for _ in range(n)]

# Counting the number of ways
result = count_ways(n, nums)
print(result)
