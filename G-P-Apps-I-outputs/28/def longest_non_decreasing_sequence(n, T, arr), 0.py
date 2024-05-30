
def longest_non_decreasing_sequence(n, T, arr):
    repeated_arr = arr * T
    dp = [1] * len(repeated_arr)

    for i in range(1, len(repeated_arr)):
        for j in range(i):
            if repeated_arr[i] >= repeated_arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Input processing
n, T = map(int, input().split())
arr = list(map(int, input().split()))

print(longest_non_decreasing_sequence(n, T, arr))
```
