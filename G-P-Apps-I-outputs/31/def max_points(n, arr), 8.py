
def max_points(n, arr):
    count = [0] * (10**5 + 1)
    for num in arr:
        count[num] += 1

    dp = [0] * (10**5 + 1)
    dp[1] = count[1]

    for i in range(2, 10**5 + 1):
        dp[i] = max(dp[i-1], dp[i-2] + count[i] * i)

    return dp[10**5]

# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
print(max_points(n, arr))
```
