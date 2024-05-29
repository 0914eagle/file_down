
def calculate_convenience(n, stations):
    connections = [0] * (n+1)
    for i, p in enumerate(stations, 1):
        connections[i] = p
    
    conveniences = [0] * (n+1)
    for i in range(1, n+1):
        visited = [False] * (n+1)
        current = i
        while not visited[current]:
            visited[current] = True
            current = connections[current]
            conveniences[i] += 1

    total_convenience = sum([conveniences[x] for x in range(1, n+1)])
    
    max_convenience = total_convenience
    for i in range(1, n+1):
        p1, p2 = i, connections[i]
        max_convenience = max(max_convenience, total_convenience + conveniences[p1] + conveniences[p2] - 2)

    return max_convenience

# Read input
n = int(input())
stations = list(map(int, input().split()))

# Output result
print(calculate_convenience(n, stations))
```
