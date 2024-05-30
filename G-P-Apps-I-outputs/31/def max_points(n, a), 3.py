
def max_points(n, a):
    freq = [0] * (max(a) + 2)
    for num in a:
        freq[num] += 1

    dp = [0] * (max(a) + 2)
    dp[1] = freq[1]

    for i in range(2, len(dp)):
        dp[i] = max(dp[i - 1], dp[i - 2] + i * freq[i])

    return dp[-1]

# Input processing
n = int(input())
a = list(map(int, input().split()))

# Call the function and print the result
print(max_points(n, a))
```
