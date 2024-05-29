
def find_maximum_hops(computers, existing_cables):
    graph = {}
    
    for cable in existing_cables:
        a, b = cable
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    
    def bfs(start):
        visited = set()
        queue = [(start, 0)]
        max_hops = 0
        
        while queue:
            node, hops = queue.pop(0)
            visited.add(node)
            max_hops = max(max_hops, hops)
            
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append((neighbor, hops + 1))
        
        return max_hops
    
    max_hops = 0
    for computer in computers:
        max_hops = max(max_hops, bfs(computer))
    
    return max_hops

computers = 6
existing_cables = [(0, 1), (0, 2), (3, 4), (3, 5)]
print(find_maximum_hops(computers, existing_cables))
```
