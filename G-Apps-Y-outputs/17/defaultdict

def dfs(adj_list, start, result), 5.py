
from collections import defaultdict

def dfs(adj_list, start, result):
    stack = [(start, 1)]
    
    while stack:
        node, level = stack.pop()
        result.append(node)
        
        for child in adj_list[node]:
            stack.append((child, level + 1))

def process_query(n, q, adj_list, queries):
    results = []
    
    for u, k in queries:
        result = []
        dfs(adj_list, u, result)
        
        if k <= len(result):
            results.append(result[k - 1])
        else:
            results.append(-1)
    
    return results

# Input
n, q = map(int, input().split())
parents = list(map(int, input().split()))
adj_list = defaultdict(list)

for i, parent in enumerate(parents, start=2):
    adj_list[parent].append(i)

queries = [tuple(map(int, input().split())) for _ in range(q)]

# Process queries
output = process_query(n, q, adj_list, queries)

# Output
for result in output:
    print(result)
