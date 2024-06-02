
import random

def expected_meeting_time(n, m, neighbors, s, t):
    graph = [[] for _ in range(n)]
    for u, v in neighbors:
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
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, time + 1))
        
        return float('inf')
    
    total_time = 0
    num_trials = 10000
    for _ in range(num_trials):
        time_alice = bfs(s)
        time_bob = bfs(t)
        if time_alice == time_bob:
            total_time += time_alice
    
    if total_time == 0:
        return "never meet"
    else:
        return total_time / num_trials

# Input parsing
n, m = map(int, input().split())
neighbors = [tuple(map(int, input().split())) for _ in range(m)]
s, t = map(int, input().split())

result = expected_meeting_time(n, m, neighbors, s, t)
print(result)
