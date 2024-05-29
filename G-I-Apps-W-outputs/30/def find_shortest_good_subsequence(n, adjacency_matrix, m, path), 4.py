
from collections import deque

def find_shortest_good_subsequence(n, adjacency_matrix, m, path):
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if adjacency_matrix[i][j] == '1':
                graph[i].append(j)

    path_set = set(path)
    visited = [[False for _ in range(n)] for _ in range(m)]
    queue = deque([(0, [path[0]])])

    while queue:
        v, seq = queue.popleft()

        if len(seq) > 1 and seq[0] == path[0] and seq[-1] == path[-1] and len(set(seq)) == len(seq) and all(visited[i][v] for i, v in enumerate(seq)):
            return len(seq), seq

        for u in graph[v]:
            if u in path_set and not visited[path.index(u)][u]:
                visited[path.index(u)][u] = True
                queue.append((u, seq + [u]))

    return None

# Input parsing
n = int(input())
adjacency_matrix = [input() for _ in range(n)]
m = int(input())
path = list(map(int, input().split()))

# Find shortest good subsequence
length, subsequence = find_shortest_good_subsequence(n, adjacency_matrix, m, path)

# Output the result
print(length)
print(" ".join(map(str, subsequence)))
