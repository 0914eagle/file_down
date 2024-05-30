
def is_canonical(n, denominations):
    for x in range(1, sum(denominations[-2:])):
        dp = [float('inf')] * (x + 1)
        dp[0] = 0
        
        for i in range(n):
            for j in range(denominations[i], x + 1):
                dp[j] = min(dp[j], dp[j - denominations[i]] + 1)
        
        greedy_count = 0
        for i in range(n):
            greedy_count += x // denominations[i]
            x %= denominations[i]
        
        if dp[-1] != greedy_count:
            return "non-canonical"
    
    return "canonical"

# Input
n = int(input())
denominations = list(map(int, input().split()))

# Output
print(is_canonical(n, denominations))
```
