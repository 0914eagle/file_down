
def max_contest_problems(n, difficulties):
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if difficulties[i] <= 2 * difficulties[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# Read input
n = int(input())
difficulties = list(map(int, input().split()))

# Call the function and print the result
print(max_contest_problems(n, difficulties))