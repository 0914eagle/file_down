
import random

def expected_meeting_time(n, m, neighbors, s, t):
    adj_list = [[] for _ in range(n)]
    for u, v in neighbors:
        adj_list[u].append(v)
        adj_list[v].append(u)

    def bfs():
        visited = [False] * n
        queue = [(s, 0)]
        visited[s] = True

        while queue:
            curr_station, time = queue.pop(0)

            if curr_station == t:
                return time

            for neighbor in adj_list[curr_station]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, time + 1))

        return -1

    total_time = 0
    num_trials = 10000

    for _ in range(num_trials):
        meeting_time = bfs()
        if meeting_time == -1:
            return "never meet"
        total_time += meeting_time

    return total_time / num_trials

# Input parsing
n, m = map(int, input().split())
neighbors = [tuple(map(int, input().split())) for _ in range(m)]
s, t = map(int, input().split())

result = expected_meeting_time(n, m, neighbors, s, t)
print(result)
