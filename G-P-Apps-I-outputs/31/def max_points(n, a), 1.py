
def max_points(n, a):
    freq = [0] * 100001
    dp = [0] * 100001

    for num in a:
        freq[num] += 1

    dp[0] = 0
    dp[1] = freq[1]

    for i in range(2, 100001):
        dp[i] = max(dp[i-1], dp[i-2] + i * freq[i])

    return dp[100000]

# Read input
n = int(input())
a = list(map(int, input().split()))

# Call the function and print the result
print(max_points(n, a))
```
