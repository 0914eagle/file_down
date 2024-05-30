
def wait_time(n, m, trails):
    graph = [[] for _ in range(n)]
    for u, v, d in trails:
        graph[u].append((v, d))
    
    def dfs(node, time_left):
        if node == n - 1:
            return time_left
        
        min_wait = float('inf')
        for neighbor, distance in graph[node]:
            if time_left >= distance:
                wait_time = dfs(neighbor, time_left - distance)
                min_wait = min(min_wait, wait_time)
        return min_wait
    
    return dfs(0, 12)

# Read input
n, m = map(int, input().split())
trails = [list(map(int, input().split())) for _ in range(m)]

# Calculate and print the wait time
print(wait_time(n, m, trails))
```
