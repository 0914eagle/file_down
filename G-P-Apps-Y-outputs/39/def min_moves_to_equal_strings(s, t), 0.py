
def min_moves_to_equal_strings(s, t):
    n = len(s)
    m = len(t)
    
    if n == 0 or m == 0:
        return n + m
    
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
    
    return dp[n][m]

# Input reading
s = input().strip()
t = input().strip()

# Output the result
print(min_moves_to_equal_strings(s, t))
```
