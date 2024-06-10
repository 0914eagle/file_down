
def min_vert_moves(n, m, shops):
    def key(t):
        return t[0]
    
    shops.sort(key=key)
    
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = dp[i-1][j]
            
            if shops[i-1][2] == j:
                dp[i][j] = min(dp[i][j], dp[i-1][j-1])
            
            dp[i][j] += abs(shops[i-1][1])
    
    return dp[n][m]

n, m = map(int, input().split())

shops = []
for _ in range(n):
    shops.append(list(map(int, input().split())))

print(min_vert_moves(n, m, shops))

