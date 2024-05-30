
def max_points(n, a):
    count = [0] * (max(a) + 2)
    for num in a:
        count[num] += 1
    dp = [0] * (max(a) + 2)
    dp[1] = count[1]
    for i in range(2, len(dp)):
        dp[i] = max(dp[i-1], dp[i-2] + count[i]*i)
    return dp[-1]

# Reading input
n = int(input())
a = list(map(int, input().split()))

# Calling the function and printing the result
print(max_points(n, a))
```
