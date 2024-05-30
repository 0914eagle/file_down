
def max_chocolates(n, a):
    dp = [0] * n
    dp[0] = a[0]
    
    for i in range(1, n):
        dp[i] = a[i]
        for j in range(i):
            if a[i] >= a[j]:
                dp[i] = max(dp[i], dp[j] + a[i])
    
    return max(dp)

# Input parsing
n = int(input())
a = list(map(int, input().split()))

# Call the function and print the result
print(max_chocolates(n, a))
```
