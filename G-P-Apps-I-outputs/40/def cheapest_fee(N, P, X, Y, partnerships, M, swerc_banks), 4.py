
def cheapest_fee(N, P, X, Y, partnerships, M, swerc_banks):
    graph = {}
    for a, b, c in partnerships:
        if a not in graph:
            graph[a] = {}
        if b not in graph:
            graph[b] = {}
        graph[a][b] = c
        graph[b][a] = c

    for m in swerc_banks:
        if m not in graph:
            graph[m] = {}

    def dijkstra(start, end):
        visited = set()
        distance = {node: float('inf') for node in graph}
        distance[start] = 0

        while True:
            min_distance = float('inf')
            current_node = None
            for node in graph:
                if node not in visited and distance[node] < min_distance:
                    min_distance = distance[node]
                    current_node = node

            if current_node is None:
                break

            visited.add(current_node)

            for neighbor, weight in graph[current_node].items():
                new_distance = distance[current_node] + weight
                if new_distance < distance[neighbor]:
                    distance[neighbor] = new_distance

        return distance[end]

    cheapest = dijkstra(X, Y)

    if cheapest == float('inf'):
        return "Infinity"
    else:
        max_fee = 1
        while True:
            max_fee += 1
            if dijkstra(X, Y) < cheapest:
                break

        return max_fee - 1

# Sample Input 1
N = 6
P = 8
X = 1
Y = 6
partnerships = [(1, 2, 5), (1, 3, 1), (2, 6, 6), (2, 3, 6), (4, 2, 3), (3, 4, 1), (4, 5, 1), (5, 6, 1)]
M = 5
swerc_banks = [1, 3, 6, 5, 4]

print(cheapest_fee(N, P, X, Y, partnerships, M, swerc_banks))  # Output: 3

# Sample Input 2
N = 3
P = 4
X = 1
Y = 2
partnerships = [(1, 2, 6), (1, 3, 2), (1, 2, 7), (2, 3, 3)]
M = 2
swerc_banks = [1, 2]

print(cheapest_fee(N, P, X, Y, partnerships, M, swerc_banks))  # Output: Infinity
```
