
from collections import defaultdict

def largest_committee(N, K, politicians):
    graph = defaultdict(set)
    
    for i, disagrees_with in enumerate(politicians):
        for p in disagrees_with[1:]:
            graph[i].add(p)
            graph[p].add(i)
    
    committee = set()
    
    def dfs(node, visited):
        if len(visited) > K:
            return
        committee.add(node)
        visited.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, visited.copy())
    
    for i in range(N):
        dfs(i, set())
    
    return len(committee)

# Input parsing
N, K = map(int, input().split())
politicians = []
for _ in range(N):
    politician_info = list(map(int, input().split()))
    politicians.append(politician_info[1:])

# Call the function with input
result = largest_committee(N, K, politicians)

# Output the result
print(result)
```
