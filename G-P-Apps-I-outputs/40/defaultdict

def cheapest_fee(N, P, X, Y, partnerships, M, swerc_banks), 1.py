
from collections import defaultdict

def cheapest_fee(N, P, X, Y, partnerships, M, swerc_banks):
    graph = defaultdict(dict)
    for a, b, c in partnerships:
        graph[a][b] = c
        graph[b][a] = c

    def dijkstra(start, end, max_fee):
        visited = set()
        min_fees = {node: float('inf') for node in graph}
        min_fees[start] = 0

        while True:
            min_node = None
            min_cost = float('inf')
            for node in graph:
                if node not in visited and min_fees[node] < min_cost:
                    min_node = node
                    min_cost = min_fees[node]
            
            if min_node is None:
                break

            visited.add(min_node)

            for neighbor, cost in graph[min_node].items():
                total_cost = min_fees[min_node] + cost
                if total_cost < min_fees[neighbor] and cost <= max_fee:
                    min_fees[neighbor] = total_cost
        
        return min_fees[end]

    min_fee = float('inf')
    for i in range(len(swerc_banks)):
        min_fee = min(min_fee, dijkstra(X, Y, dijkstra(X, swerc_banks[i], float('inf'))))

    if min_fee == float('inf'):
        return "Impossible"
    elif min_fee == 0:
        return "Infinity"
    else:
        return min_fee

# Input parsing
data = input().strip().split()
N, P, X, Y = map(int, data[:4])
partnerships = [tuple(map(int, data[i:i+3])) for i in range(4, 4 + P)]
M = int(data[4 + P])
swerc_banks = list(map(int, data[5 + P + 1:]))

# Call the function and print the result
result = cheapest_fee(N, P, X, Y, partnerships, M, swerc_banks)
print(result)
```
