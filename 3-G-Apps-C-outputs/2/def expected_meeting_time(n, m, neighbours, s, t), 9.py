
import random

def expected_meeting_time(n, m, neighbours, s, t):
    graph = [[] for _ in range(n)]
    for u, v in neighbours:
        graph[u].append(v)
        graph[v].append(u)
    
    def bfs(s, t):
        visited = [False] * n
        queue = [(s, 0)]
        visited[s] = True
        
        while queue:
            curr, time = queue.pop(0)
            if curr == t:
                return time
            for neighbour in graph[curr]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    queue.append((neighbour, time + 1))
        
        return -1
    
    meeting_time = bfs(s, t)
    if meeting_time == -1:
        return "never meet"
    return meeting_time

# Input parsing
n, m = map(int, input().split())
neighbours = [tuple(map(int, input().split())) for _ in range(m)]
s, t = map(int, input().split())

# Calculate and output the expected meeting time
print(expected_meeting_time(n, m, neighbours, s, t))
