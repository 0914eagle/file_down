
def max_chocolates(n, chocolates):
    dp = [0] * n
    dp[0] = chocolates[0]
    
    for i in range(1, n):
        dp[i] = chocolates[i]
        for j in range(i):
            if chocolates[i] >= chocolates[j]:
                dp[i] = max(dp[i], dp[j] + chocolates[i])
    
    return max(dp)

# Read input
n = int(input())
chocolates = list(map(int, input().split()))

# Call function and print result
print(max_chocolates(n, chocolates))
```
