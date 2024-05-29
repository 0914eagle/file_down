
def is_tourist_friendly(N, E, roads):
    adj_list = {}
    for road in roads:
        if road[0] not in adj_list:
            adj_list[road[0]] = []
        adj_list[road[0]].append(road[1])

    visited = [False] * (N + 1)

    def dfs(node):
        visited[node] = True
        if node in adj_list:
            for neighbor in adj_list[node]:
                if not visited[neighbor]:
                    dfs(neighbor)

    dfs(1)

    for i in range(1, N + 1):
        if not visited.get(i, False):
            return "NO"

    return "YES"

N, E = map(int, input().split())
roads = []
for _ in range(E):
    a, b = map(int, input().split())
    roads.append((a, b))

result = is_tourist_friendly(N, E, roads)
print(result)
if result == "YES":
    for road in roads:
        print(road[0], road[1])
```
