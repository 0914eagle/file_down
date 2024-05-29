
def max_hops(c, l, cables):
    adj_list = {i: [] for i in range(c)}
    for a, b in cables:
        adj_list[a].append(b)
        adj_list[b].append(a)
    
    visited = set()
    
    def dfs(node, parent, hops):
        nonlocal max_hops
        visited.add(node)
        max_hops = max(max_hops, hops)
        
        for neighbor in adj_list[node]:
            if neighbor != parent and neighbor not in visited:
                dfs(neighbor, node, hops + 1)
    
    max_hops = 0
    dfs(0, -1, 0)
    
    return max_hops

input_data = 

lines = input_data.split('\n')
c, l = map(int, lines[0].split())
cables = [tuple(map(int, line.split())) for line in lines[1:]]

result = max_hops(c, l, cables)
print(result)
```
