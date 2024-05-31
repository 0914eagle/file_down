
from collections import defaultdict

def process_query(n, p, queries):
    graph = defaultdict(list)
    for i in range(2, n + 1):
        graph[p[i-2]].append(i)

    def dfs(node):
        sequence = [node]
        for child in graph.get(node, []):
            sequence += dfs(child)
        return sequence

    results = []
    for u, k in queries:
        sequence = dfs(u)
        if k <= len(sequence):
            results.append(sequence[k-1])
        else:
            results.append(-1)
    return results

# Input parsing
n, q = map(int, input().split())
p = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(q)]

# Process queries
output = process_query(n, p, queries)

# Output the results
for result in output:
    print(result)
