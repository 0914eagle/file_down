
def find_min_distance(n, m, roads, q, queries):
    graph = [[float('inf')] * n for _ in range(n)]
    for a, b, w in roads:
        graph[a-1][b-1] = w
        graph[b-1][a-1] = w
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] | graph[k][j])
    
    results = []
    for s, t in queries:
        results.append(graph[s-1][t-1])
    
    return results

# Reading input
n, m = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(m)]
q = int(input())
queries = [list(map(int, input().split())) for _ in range(q)]

# Finding transportation costs
results = find_min_distance(n, m, roads, q, queries)

# Outputting results
for cost in results:
    print(cost)
