
def traverse_cave_system(A, H, n, m, passages):
    dp = [[0 for _ in range(H+1)] for _ in range(n)]
    
    for i in range(1, n):
        dp[i][0] = -1
    
    for e, b, a, h in passages:
        for j in range(H, -1, -1):
            if j >= h:
                dp[b-1][j-h] = max(dp[b-1][j-h], dp[e-1][j] + 1)
            if j >= a:
                dp[e-1][j-a] = max(dp[e-1][j-a], dp[b-1][j] + 1)
    
    max_health = max(dp[n-1])
    if max_health == 0:
        return "Oh no"
    else:
        return H - max_health

# Sample Input 1
A, H = 1, 2
n, m = 3, 2
passages = [(1, 2, 1, 2), (2, 3, 1, 2)]
print(traverse_cave_system(A, H, n, m, passages))  # Output: Oh no

# Sample Input 2
A, H = 1, 3
n, m = 3, 2
passages = [(1, 2, 1, 2), (2, 3, 1, 2)]
print(traverse_cave_system(A, H, n, m, passages))  # Output: 1
```
