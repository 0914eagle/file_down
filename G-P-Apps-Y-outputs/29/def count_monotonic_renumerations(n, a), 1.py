
MOD = 998244353

def count_monotonic_renumerations(n, a):
    freq = {}
    for num in a:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for f in freq.values():
        new_dp = dp.copy()
        for i in range(n + 1):
            new_dp[i] %= MOD
            for j in range(f):
                if i + j + 1 <= n:
                    new_dp[i + j + 1] += dp[i]
        dp = new_dp
    
    total = sum(dp) % MOD
    return total

# Read input
n = int(input())
a = list(map(int, input().split()))

# Calculate and print the result
result = count_monotonic_renumerations(n, a)
print(result)
```
