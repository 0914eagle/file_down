
def longest_non_decreasing_sequence(n, T, arr):
    extended_arr = arr * T
    length = len(extended_arr)
    dp = [1] * length
    
    for i in range(1, length):
        for j in range(i):
            if extended_arr[i] >= extended_arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# Input processing
n, T = map(int, input().split())
arr = list(map(int, input().split()))

# Call the function
result = longest_non_decreasing_sequence(n, T, arr)
print(result)
```
