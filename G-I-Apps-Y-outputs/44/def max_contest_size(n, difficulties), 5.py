
def max_contest_size(n, difficulties):
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if difficulties[i] <= 2 * difficulties[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# Reading input
n = int(input())
difficulties = list(map(int, input().split()))

# Calling the function and printing the result
print(max_contest_size(n, difficulties))
```
