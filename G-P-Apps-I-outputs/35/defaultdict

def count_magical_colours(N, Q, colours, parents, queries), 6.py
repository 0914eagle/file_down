
from collections import defaultdict

def count_magical_colours(N, Q, colours, parents, queries):
    graph = defaultdict(list)
    for i in range(1, N):
        graph[parents[i-1]].append(i+1)
    
    def dfs(node):
        count = defaultdict(int)
        for child in graph[node]:
            child_count = dfs(child)
            for key, value in child_count.items():
                count[key] += value
        count[colours[node-1]] += 1
        return count
    
    def is_magical(count):
        magical_count = 0
        for key, value in count.items():
            if value % 2 == 1:
                magical_count += 1
        return magical_count
    
    result = []
    for query in queries:
        k, x = query
        if k == 0:
            count = dfs(x)
            result.append(is_magical(count))
        else:
            colours[x-1] = k
    
    return result

# Input parsing
N, Q = map(int, input().split())
colours = list(map(int, input().split()))
parents = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(Q)]

# Get the result
output = count_magical_colours(N, Q, colours, parents, queries)

# Output the result
for value in output:
    print(value)
```
