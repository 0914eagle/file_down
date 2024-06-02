
import random

def expected_meeting_time(n, m, neighbours, s, t):
    graph = [[] for _ in range(n)]
    for u, v in neighbours:
        graph[u].append(v)
        graph[v].append(u)

    def bfs(start):
        visited = [False] * n
        queue = [(start, 0)]
        visited[start] = True

        while queue:
            node, time = queue.pop(0)
            if node == t:
                return time
            for neighbour in graph[node]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    queue.append((neighbour, time + 1))

        return float('inf')

    total_time = 0
    num_trials = 10000
    for _ in range(num_trials):
        time_alice = bfs(s)
        time_bob = bfs(t)
        total_time += max(time_alice, time_bob)

    expected_time = total_time / num_trials
    if expected_time == float('inf'):
        return "never meet"
    return expected_time

# Input
n, m = map(int, input().split())
neighbours = [tuple(map(int, input().split())) for _ in range(m)]
s, t = map(int, input().split())

# Output
print(expected_meeting_time(n, m, neighbours, s, t))
