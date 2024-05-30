
def longest_non_decreasing_sequence(n, T, arr):
    arr_extended = arr * T
    dp = [1] * len(arr_extended)

    for i in range(1, len(arr_extended)):
        for j in range(i):
            if arr_extended[i] >= arr_extended[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Input parsing
n, T = map(int, input().split())
arr = list(map(int, input().split()))

# Call the function and print the result
result = longest_non_decreasing_sequence(n, T, arr)
print(result)
```
