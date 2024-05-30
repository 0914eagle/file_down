
MOD = 998244353

def count_monotonic_renumerations(n, arr):
    freq = {}
    for num in arr:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1
    
    values = sorted(list(set(arr)))
    dp = [0] * (len(values) + 1)
    dp[0] = 1
    
    for i in range(1, len(dp)):
        dp[i] = dp[i-1] + (dp[i-2] if i >= 2 else 0)
    
    result = 1
    for num in values:
        result = (result * dp[freq[num]]) % MOD
    
    return result

n = int(input())
arr = list(map(int, input().split()))

print(count_monotonic_renumerations(n, arr))
```
