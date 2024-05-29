
def shortest_good_subsequence(n, graph, m, path):
    shortest_path_lengths = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] == '1':
                shortest_path_lengths[i][j] = 1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                shortest_path_lengths[i][j] = min(shortest_path_lengths[i][j], shortest_path_lengths[i][k] + shortest_path_lengths[k][j])

    best_length = shortest_path_lengths[path[0] - 1][path[-1] - 1]
    good_subseq = [path[0]]
    current_vertex = path[0]

    for next_vertex in path[1:]:
        if shortest_path_lengths[current_vertex - 1][next_vertex - 1] == best_length:
            good_subseq.append(next_vertex)
        else:
            current_vertex = next_vertex

    return len(good_subseq), good_subseq

# Input parsing
n = int(input())
graph = [input() for _ in range(n)]
m = int(input())
path = list(map(int, input().split()))

# Find and print the shortest good subsequence
k, good_subsequence = shortest_good_subsequence(n, graph, m, path)
print(k)
print(' '.join(map(str, good_subsequence)))
```
