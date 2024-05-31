
from math import isqrt

def has_divisors(num):
    count = 0
    for i in range(1, isqrt(num)+1):
        if num % i == 0:
            if num // i == i:
                count += 1
            else:
                count += 2
        if count > 7:
            return True
    if count <= 7:
        return False

def shortest_subsequence(arr):
    n = len(arr)
    dp = [float('inf')] * (1 << n)
    for i in range(n):
        if not has_divisors(arr[i]):
            dp[1 << i] = 1
    
    for mask in range(1 << n):
        for i in range(n):
            if mask & (1 << i) == 0:
                new_mask = mask | (1 << i)
                dp[new_mask] = min(dp[new_mask], dp[mask] + 1)
                for j in range(i+1, n):
                    if (mask & (1 << j)) == 0 and not has_divisors(arr[i] * arr[j]):
                        new_mask = mask | (1 << i) | (1 << j)
                        dp[new_mask] = min(dp[new_mask], dp[mask] + 2)
    
    ans = min(dp) if min(dp) != float('inf') else -1
    return ans

# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
print(shortest_subsequence(arr))
