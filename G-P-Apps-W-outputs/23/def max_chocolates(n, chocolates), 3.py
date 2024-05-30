
def max_chocolates(n, chocolates):
    dp = [0] * n
    for i in range(n):
        dp[i] = chocolates[i]
        for j in range(i):
            if chocolates[i] >= chocolates[j]:
                dp[i] = max(dp[i], chocolates[i] + dp[j])
    return max(dp)

# Read input
n = int(input())
chocolates = list(map(int, input().split()))

# Call the function and print the result
print(max_chocolates(n, chocolates))
