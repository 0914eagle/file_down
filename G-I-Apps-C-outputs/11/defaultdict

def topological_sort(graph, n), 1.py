
from collections import defaultdict

def topological_sort(graph, n):
    in_degree = [0] * n
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    
    sources = [node for node in range(n) if in_degree[node] == 0]
    max_sources = len(sources)
    
    while sources:
        node = sources.pop(0)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                sources.append(neighbor)
    
    return max_sources

def main():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
    
    print(topological_sort(graph, n))

if __name__ == "__main__":
    main()
```
