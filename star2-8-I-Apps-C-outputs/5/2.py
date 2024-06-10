
from sys import stdin, stdout
from collections import deque

def BFS(adj_list, D):
    queue = deque()
    queue.append((0, 0)) # node 0 at depth 0
    marked = [False] * len(adj_list)
    max_depth = 0
    while queue:
        node, depth = queue.popleft()
        if not marked[node]:
            marked[node] = True
            max_depth = max(max_depth, depth)
        for neighbor in adj_list[node]:
            if not marked[neighbor] and depth + 1 >= D:
                queue.append((neighbor, depth + 1))
    return max_depth

N, D = map(int, stdin.readline().split())
adj_list = [[] for _ in range(N)]
for i in range(1, N):
    x = int(stdin.readline())
    adj_list[x].append(i)
    adj_list[i].append(x)
max_depth = BFS(adj_list, D)
stdout.write(str(max_depth + 1) + '\n')

