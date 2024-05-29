
def max_contest_problems(n, difficulties):
    max_problems = 1
    dp = [1] * n
    
    for i in range(1, n):
        j = i - 1
        while j >= 0 and difficulties[i] <= 2 * difficulties[j]:
            j -= 1
        if j >= 0:
            dp[i] = dp[j] + 1
        max_problems = max(max_problems, dp[i])
    
    return max_problems

# Reading input
n = int(input())
difficulties = list(map(int, input().split()))

# Calling the function and printing the result
print(max_contest_problems(n, difficulties))
```
