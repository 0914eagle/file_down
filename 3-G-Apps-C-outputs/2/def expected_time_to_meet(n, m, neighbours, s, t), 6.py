
import itertools

def expected_time_to_meet(n, m, neighbours, s, t):
    graph = [[0] * n for _ in range(n)]
    for u, v in neighbours:
        graph[u][v] = graph[v][u] = 1

    def all_pairs_shortest_path():
        for k in range(n):
            for i, j in itertools.product(range(n), repeat=2):
                if i != j:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    all_pairs_shortest_path()

    if graph[s][t] == 1:
        return 1

    total_time = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                total_time += 1 / (n * n)

    return total_time

# Input
n, m = map(int, input().split())
neighbours = [tuple(map(int, input().split())) for _ in range(m)]
s, t = map(int, input().split())

# Output
result = expected_time_to_meet(n, m, neighbours, s, t)
if result == 0:
    print("never meet")
else:
    print(result)

