
def max_profit(n, snacks):
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        dp[i] = max(dp[i], dp[i-1])
        f, p, m, s = snacks[i-1]
        if i + 1 <= n:
            f_next, p_next, m_next, s_next = snacks[i]
            dp[f_next] = max(dp[f_next], dp[i] + (m_next - p_next) * s_next)
    
    return dp[n]

# Sample Input 1
n1 = 3
snacks1 = [(1, 2, 3, 1), (2, 3, 4, 1), (3, 4, 5, 1)]
print(max_profit(n1, snacks1))  # Output: 3

# Sample Input 2
n2 = 3
snacks2 = [(2, 2, 3, 8), (3, 1, 5, 6), (1, 9, 4, 7)]
print(max_profit(n2, snacks2))  # Output: 39
```
