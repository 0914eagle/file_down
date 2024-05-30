
def max_points(n, arr):
    freq = [0] * (max(arr) + 2)
    for num in arr:
        freq[num] += 1

    dp = [0] * (max(arr) + 2)
    dp[1] = freq[1]

    for i in range(2, len(dp)):
        dp[i] = max(dp[i-1], dp[i-2] + i * freq[i])

    return dp[-1]

# Read input
n = int(input())
arr = list(map(int, input().split()))

# Call the function and print the result
print(max_points(n, arr))
```
