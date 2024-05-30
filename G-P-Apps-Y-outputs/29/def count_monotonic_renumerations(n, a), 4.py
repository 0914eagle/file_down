
MOD = 998244353

def count_monotonic_renumerations(n, a):
    freq = {}
    for num in a:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    counts = list(freq.values())
    counts.sort()
    
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for count in counts:
        new_dp = [0] * (n + 1)
        for i in range(n + 1):
            new_dp[i] = (dp[i] + dp[i - 1] * count) % MOD
        dp = new_dp
    
    return dp[n]

# Input reading
n = int(input())
a = list(map(int, input().split()))

# Calculate and print the result
result = count_monotonic_renumerations(n, a)
print(result)
```
