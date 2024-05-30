
def max_chocolates(n, chocolates):
    dp = [0] * n
    dp[0] = chocolates[0]
    
    for i in range(1, n):
        dp[i] = max(chocolates[i], dp[i-1] if chocolates[i] > 0 else 0)
    
    return sum(dp)

# Input parsing
n = int(input())
chocolates = list(map(int, input().split()))

# Calculate and print the result
print(max_chocolates(n, chocolates))
```
