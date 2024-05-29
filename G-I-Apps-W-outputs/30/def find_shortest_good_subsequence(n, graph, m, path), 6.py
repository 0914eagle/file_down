
from collections import deque

def find_shortest_good_subsequence(n, graph, m, path):
    dist = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        queue = deque([(i, 0)])
        dist[i][i] = 0
        
        while queue:
            node, d = queue.popleft()
            for j in range(n):
                if graph[node][j] == '1' and d + 1 < dist[i][j]:
                    dist[i][j] = d + 1
                    queue.append((j, d + 1))
    
    shortest_length = float('inf')
    shortest_subsequence = None
    
    for i in range(m):
        for j in range(i, m):
            if path[i] == path[j] and i != j:
                continue
            
            length = dist[path[i]-1][path[j]-1] + 1
            if length < shortest_length:
                shortest_length = length
                shortest_subsequence = path[i:j+1]
    
    return shortest_subsequence

# Read input
n = int(input())
graph = [input() for _ in range(n)]
m = int(input())
path = list(map(int, input().split()))

result = find_shortest_good_subsequence(n, graph, m, path)

# Output result
print(len(result))
print(' '.join(map(str, result)))
```
