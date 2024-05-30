
MOD = 998244353

def count_monotonic_renumerations(n, a):
    freq = {}
    for num in a:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    num_counts = list(freq.values())
    
    num_counts.sort()
    
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for count in num_counts:
        new_dp = [0] * (n + 1)
        for i in range(n + 1):
            new_dp[i] = (dp[i] + dp[i + 1] * count) % MOD
        dp = new_dp
        
    return dp[0]

# Input reading
n = int(input())
a = list(map(int, input().split()))

# Calculate and print the result
result = count_monotonic_renumerations(n, a)
print(result)
```
