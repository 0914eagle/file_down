
def find_waiting_time(n, m, trails):
    adj_list = [[] for _ in range(n)]
    for u, v, d in trails:
        adj_list[u].append((v, d))
    
    def dijkstra(source):
        dist = [float('inf')] * n
        dist[source] = 0
        visited = [False] * n
        
        for _ in range(n):
            u = min((i for i in range(n) if not visited[i]), key=lambda x: dist[x])
            visited[u] = True
            for v, d in adj_list[u]:
                if dist[v] > dist[u] + d:
                    dist[v] = dist[u] + d
        
        return dist
    
    day_dist = dijkstra(0)
    knight_dist = dijkstra(n-1)
    
    waiting_time = 0
    for i in range(n):
        if day_dist[i] + knight_dist[i] <= 12:
            waiting_time = max(waiting_time, knight_dist[i])
    
    return waiting_time

# Input parsing
n, m = map(int, input().split())
trails = [tuple(map(int, input().split())) for _ in range(m)]

# Call the function and output the result
print(find_waiting_time(n, m, trails))
```
