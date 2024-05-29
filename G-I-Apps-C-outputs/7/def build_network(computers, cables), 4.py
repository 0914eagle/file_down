
def build_network(computers, cables):
    adjacency_list = {}
    for cable in cables:
        a, b = cable
        if a not in adjacency_list:
            adjacency_list[a] = set()
        if b not in adjacency_list:
            adjacency_list[b] = set()
        
        adjacency_list[a].add(b)
        adjacency_list[b].add(a)
    
    max_hops = 0
    visited = set()
    
    def dfs(node, depth):
        nonlocal max_hops
        visited.add(node)
        max_hops = max(max_hops, depth)
        
        if node in adjacency_list:
            for neighbor in adjacency_list[node]:
                if neighbor not in visited:
                    dfs(neighbor, depth + 1)
    
    for node in range(computers):
        if node not in visited:
            dfs(node, 0)
    
    return max_hops

# Input
input_lines = [
    "6 4",
    "0 1",
    "0 2",
    "3 4",
    "3 5"
]

n, m = map(int, input_lines[0].split())
cables = [tuple(map(int, line.split())) for line in input_lines[1:]]

# Output
result = build_network(n, cables)
print(result)
```
