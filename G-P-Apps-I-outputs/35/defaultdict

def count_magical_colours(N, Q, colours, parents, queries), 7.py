
from collections import defaultdict

def count_magical_colours(N, Q, colours, parents, queries):
    tree = defaultdict(list)
    for node, parent in enumerate(parents, start=2):
        tree[parent].append(node)
    
    def dfs(node):
        count = defaultdict(int)
        count[colours[node-1]] += 1
        
        for child in tree[node]:
            child_count = dfs(child)
            for color, freq in child_count.items():
                count[color] += freq
            
        magical_count = 0
        for freq in count.values():
            if freq % 2 == 1:
                magical_count += 1
        
        return count, magical_count
    
    results = []
    for k, x in queries:
        if k == 0:
            results.append(dfs(x)[1])
        else:
            colours[x-1] = k

    return results

# Read input
N, Q = map(int, input().split())
colours = list(map(int, input().split()))
parents = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(Q)]

# Call function
results = count_magical_colours(N, Q, colours, parents, queries)

# Print output
for res in results:
    print(res)
```
