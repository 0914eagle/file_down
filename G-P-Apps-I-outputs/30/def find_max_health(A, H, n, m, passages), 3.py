
def find_max_health(A, H, n, m, passages):
    graph = {}
    for i in range(1, n + 1):
        graph[i] = []
    
    for passage in passages:
        e, b, a, h = passage
        graph[e].append((b, a, h))
    
    visited = [False] * (n + 1)
    max_health = [0] * (n + 1)

    def dfs(node):
        if node == n:
            max_health[node] = H
            return True
        
        visited[node] = True
        curr_max_health = 0

        for neighbor, a, h in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor):
                    if H - a <= 0:
                        return False
                    curr_max_health = max(curr_max_health, max_health[neighbor] - a)

        max_health[node] = curr_max_health
        visited[node] = False

        return curr_max_health > 0

    if dfs(1):
        return max_health[1]
    else:
        return 'Oh no'

# Input
A, H = map(int, input().split())
n, m = map(int, input().split())
passages = [list(map(int, input().split())) for _ in range(m)]

# Output
result = find_max_health(A, H, n, m, passages)
print(result)
```
