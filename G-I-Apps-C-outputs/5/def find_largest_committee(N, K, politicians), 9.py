
def find_largest_committee(N, K, politicians):
    adj_list = [[] for _ in range(N)]
    
    for i in range(N):
        disagree_with = politicians[i][1:]
        for j in disagree_with:
            adj_list[i].append(j)
    
    def dfs(node, visited):
        visited[node] = True
        group_size = 1
        
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                group_size += dfs(neighbor, visited)
        
        return group_size
    
    largest_size = 0
    for i in range(N):
        visited = [False] * N
        group_size = dfs(i, visited)
        largest_size = max(largest_size, group_size)
    
    return largest_size

# Read input
N, K = map(int, input().split())
politicians = []
for _ in range(N):
    data = list(map(int, input().split()))
    politicians.append(data)

# Find and print the largest committee size
largest_committee = find_largest_committee(N, K, politicians)
print(largest_committee)
```
