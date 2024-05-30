
def max_points(n, nums):
    freq = [0] * (10**5 + 2)
    for num in nums:
        freq[num] += num

    dp = [0] * (10**5 + 2)
    dp[0] = 0
    dp[1] = freq[1]

    for i in range(2, 10**5 + 2):
        dp[i] = max(dp[i-1], dp[i-2] + freq[i])

    return dp[10**5 + 1]

# Input processing
n = int(input())
nums = list(map(int, input().split()))

# Output
print(max_points(n, nums))
```
