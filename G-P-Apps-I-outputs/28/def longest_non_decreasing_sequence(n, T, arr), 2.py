
def longest_non_decreasing_sequence(n, T, arr):
    full_arr = arr * T
    dp = [1] * len(full_arr)
    for i in range(1, len(full_arr)):
        for j in range(i):
            if full_arr[i] >= full_arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# Input parsing
n, T = map(int, input().split())
arr = list(map(int, input().split()))

# Output
print(longest_non_decreasing_sequence(n, T, arr))
```
