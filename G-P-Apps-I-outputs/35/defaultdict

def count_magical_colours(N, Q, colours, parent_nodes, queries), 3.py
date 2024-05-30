
from collections import defaultdict

def count_magical_colours(N, Q, colours, parent_nodes, queries):
    tree = defaultdict(list)
    for i in range(1, N):
        tree[parent_nodes[i]].append(i+1)
    
    def dfs(node, subtree_colours):
        subtree_colours[colours[node-1]] += 1
        for child in tree[node]:
            dfs(child, subtree_colours.copy())
        
    dfs(1, defaultdict(int))
    
    for k, x in queries:
        if k == 0:
            print(sum(1 for count in dfs(x, defaultdict(int)).values() if count % 2 == 1))
        else:
            colours[x-1] = k
            dfs(1, defaultdict(int))

N, Q = map(int, input().split())
colours = list(map(int, input().split()))
parent_nodes = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(Q)]

count_magical_colours(N, Q, colours, parent_nodes, queries)
```
