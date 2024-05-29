
def max_contest_problems(n, difficulties):
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if difficulties[i] <= difficulties[j] * 2:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# Reading input
n = int(input())
difficulties = list(map(int, input().split()))

# Calculate and print the result
result = max_contest_problems(n, difficulties)
print(result)
