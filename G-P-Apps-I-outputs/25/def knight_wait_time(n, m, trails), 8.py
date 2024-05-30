
def knight_wait_time(n, m, trails):
    INF = float('inf')
    graph = [[INF for _ in range(n)] for _ in range(n)]
    for u, v, d in trails:
        graph[u][v] = min(graph[u][v], d)
    
    dp = [INF] * n
    dp[0] = 0
    
    for _ in range(12):
        new_dp = dp[:]
        for u in range(n):
            for v in range(n):
                if graph[u][v] != INF:
                    new_dp[v] = min(new_dp[v], dp[u] + graph[u][v])
        dp = new_dp
    
    return dp[n-1]

# Input parsing
n, m = map(int, input().split())
trails = []
for _ in range(m):
    u, v, d = map(int, input().split())
    trails.append((u, v, d))

result = knight_wait_time(n, m, trails)
print(result)
```
