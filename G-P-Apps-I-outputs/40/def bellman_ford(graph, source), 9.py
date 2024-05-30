
def bellman_ford(graph, source):
    distance = {node: float('inf') for node in graph}
    distance[source] = 0

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node]:
                if distance[node] + weight < distance[neighbor]:
                    distance[neighbor] = distance[node] + weight

    for node in graph:
        for neighbor, weight in graph[node]:
            if distance[node] + weight < distance[neighbor]:
                return float('inf')

    return max(weight for node in graph for neighbor, weight in graph[node])

N, P, X, Y = map(int, input().split())
partnerships = {}
for _ in range(P):
    a, b, c = map(int, input().split())
    if a not in partnerships:
        partnerships[a] = []
    partnerships[a].append((b, c))
    if b not in partnerships:
        partnerships[b] = []
    partnerships[b].append((a, c))

M = int(input())
banks_owned = list(map(int, input().split()))

graph = {bank: partnerships[bank] for bank in banks_owned}
largest_fee = bellman_ford(graph, X)

if largest_fee == float('inf'):
    print("Infinity")
else:
    print(largest_fee)
```
