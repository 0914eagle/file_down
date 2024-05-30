
def max_points(n, sequence):
    max_num = max(sequence)
    frequencies = [0] * (max_num + 1)
    for num in sequence:
        frequencies[num] += num

    dp = [0] * (max_num + 1)
    dp[0] = 0
    dp[1] = frequencies[1]

    for i in range(2, max_num + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + frequencies[i])

    return dp[max_num]

# Reading input
n = int(input())
sequence = list(map(int, input().split()))

# Calling the function and printing the result
print(max_points(n, sequence))
```
