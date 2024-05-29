
def find_tourist_friendly_scheme(N, E, roads):
    graph = {}
    for a, b in roads:
        if a not in graph:
            graph[a] = []
        graph[a].append(b)

    # Function to perform Depth First Search
    def dfs(city, path):
        if len(path) == E:
            return True
        if city in visited:
            return False
        visited.add(city)
        for next_city in graph.get(city, []):
            if dfs(next_city, path + [(city, next_city)]):
                return True
        visited.remove(city)
        return False

    # Check if there exists a tourist-friendly scheme
    visited = set()
    for city in range(1, N+1):
        if dfs(city, []):
            return True

    return False

# Input parsing
N, E = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(E)]

# Check for tourist-friendly scheme
if find_tourist_friendly_scheme(N, E, roads):
    print("YES")
    for a, b in roads:
        print(a, b)
else:
    print("NO")
```
