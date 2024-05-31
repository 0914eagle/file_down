
from collections import defaultdict

def construct_command_sequence(n, p, queries):
    graph = defaultdict(list)
    for i in range(2, n+1):
        graph[p[i-2]].append(i)

    def dfs(node):
        sequence = [node]
        for child in sorted(graph[node]):
            sequence += dfs(child)
        return sequence

    results = []
    for query in queries:
        u, k = query
        sequence = dfs(u)
        if k <= len(sequence):
            results.append(sequence[k-1])
        else:
            results.append(-1)
    
    return results

# Input parsing
n, q = map(int, input().split())
p = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(q)]

# Call the function and print the results
for result in construct_command_sequence(n, p, queries):
    print(result)
