
def max_hops(c, l, cables):
    graph = {}
    for i in range(c):
        graph[i] = set()
    
    for a, b in cables:
        graph[a].add(b)
        graph[b].add(a)
    
    max_hops = 0
    for i in range(c):
        visited = set()
        queue = [(i, 0)]
        
        while queue:
            node, hops = queue.pop(0)
            visited.add(node)
            max_hops = max(max_hops, hops)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, hops + 1))
    
    return max_hops

c, l = map(int, input().split())
cables = [list(map(int, input().split())) for _ in range(l)]

print(max_hops(c, l, cables))
```
