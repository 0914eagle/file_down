
def find_eulerian_tour(nodes, edges):
    graph = {}
    visited = {}
    for a, b in edges:
        if a not in graph:
            graph[a] = []
        graph[a].append(b)
        visited[(a, b)] = False

    def dfs(node):
        for neighbor in graph.get(node, []):
            if not visited[(node, neighbor)]:
                visited[(node, neighbor)] = True
                dfs(neighbor)

    dfs(nodes[0])
    
    if all(visited.values()):
        print("YES")
        for a, b in edges:
            print(f"{a} {b}")
    else:
        print("NO")

# Input parsing
N, E = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(E)]

find_eulerian_tour(range(1, N+1), roads)
```
