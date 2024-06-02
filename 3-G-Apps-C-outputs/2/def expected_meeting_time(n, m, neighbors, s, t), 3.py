
import random

def expected_meeting_time(n, m, neighbors, s, t):
    adj_list = [[] for _ in range(n)]
    for u, v in neighbors:
        adj_list[u].append(v)
        adj_list[v].append(u)

    def bfs(s, t):
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

    expected_time = 0
    num_trials = 100000
    for _ in range(num_trials):
        time_to_meet = bfs(s, t)
        if time_to_meet == -1:
            return "never meet"
        expected_time += time_to_meet

        s = random.choice(adj_list[s])
        t = random.choice(adj_list[t])

    return expected_time / num_trials

# Input processing
n, m = map(int, input().split())
neighbors = [tuple(map(int, input().split())) for _ in range(m)]
s, t = map(int, input().split())

result = expected_meeting_time(n, m, neighbors, s, t)
print(result)
