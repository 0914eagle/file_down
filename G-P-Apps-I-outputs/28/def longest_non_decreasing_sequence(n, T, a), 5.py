
def longest_non_decreasing_sequence(n, T, a):
    extended_array = a * T
    dp = [1] * len(extended_array)
    
    for i in range(1, len(extended_array)):
        for j in range(i):
            if extended_array[i] >= extended_array[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# Input
n, T = map(int, input().split())
a = list(map(int, input().split()))

# Output
print(longest_non_decreasing_sequence(n, T, a))
```
