
def longest_non_decreasing_sequence(n, T, arr):
    extended_arr = arr * T
    dp = [1] * len(extended_arr)
    
    for i in range(1, len(extended_arr)):
        for j in range(i):
            if extended_arr[i] >= extended_arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# Read input
n, T = map(int, input().split())
arr = list(map(int, input().split()))

# Call the function and print the result
print(longest_non_decreasing_sequence(n, T, arr))
```
