
import random

def expected_meeting_time(n, m, neighbours, s, t):
    graph = [[] for _ in range(n)]
    for u, v in neighbours:
        graph[u].append(v)
        graph[v].append(u)
    
    def dfs(u, v, time):
        if u == v:
            return time
        visited[u] = True
        for next_station in graph[u]:
            if not visited[next_station]:
                result = dfs(next_station, v, time + 1)
                if result != -1:
                    return result
        return -1
    
    for _ in range(10**6):
        visited = [False] * n
        result = dfs(s, t, 0)
        if result != -1:
            return result
    
    return "never meet"

# Input
n, m = map(int, input().split())
neighbours = [tuple(map(int, input().split())) for _ in range(m)]
s, t = map(int, input().split())

# Output
print(expected_meeting_time(n, m, neighbours, s, t))
