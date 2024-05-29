
def find_max_hops(computers, cables):
    adj_list = {}
    for a, b in cables:
        if a not in adj_list:
            adj_list[a] = []
        if b not in adj_list:
            adj_list[b] = []
        adj_list[a].append(b)
        adj_list[b].append(a)
    
    def dfs(node, parent, depth):
        max_depth = depth
        for neighbor in adj_list[node]:
            if neighbor != parent:
                max_depth = max(max_depth, dfs(neighbor, node, depth+1))
        return max_depth
    
    max_hops = 0
    for node in range(computers):
        max_hops = max(max_hops, dfs(node, None, 0))
    
    return max_hops

# Sample Input
computers = 6
cables = [(0, 1), (0, 2), (3, 4), (3, 5)]

print(find_max_hops(computers, cables))  # Output: 3
```
