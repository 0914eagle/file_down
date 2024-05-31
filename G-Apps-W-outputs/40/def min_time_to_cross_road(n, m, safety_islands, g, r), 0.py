
from collections import deque

def min_time_to_cross_road(n, m, safety_islands, g, r):
    INF = float('inf')
    dist = [[[INF] * 2 for _ in range(m)] for _ in range(n + 1)]
    
    q = deque()
    q.append((0, 0, 0))
    dist[0][0][0] = 0
    
    while q:
        v, mod, state = q.popleft()
        
        # Moving ahead with green light
        if state == 0:
            if v + 1 <= n and dist[v + 1][mod][1] > dist[v][mod][0] + 1:
                dist[v + 1][mod][1] = dist[v][mod][0] + 1
                q.append((v + 1, mod, 1))
                
            if v - 1 >= 0 and dist[v - 1][mod][1] > dist[v][mod][0] + 1:
                dist[v - 1][mod][1] = dist[v][mod][0] + 1
                q.append((v - 1, mod, 1))
        
        # Waiting on safety island during red light
        elif state == 1:
            if dist[v][1 - mod][0] > dist[v][mod][1] + g:
                dist[v][1 - mod][0] = dist[v][mod][1] + g
                q.append((v, 1 - mod, 0))
                
        # Changing direction on safety island
        if v in safety_islands and dist[v][mod][1] > dist[v][mod][0] + 1:
            dist[v][mod][1] = dist[v][mod][0] + 1
            q.append((v, mod, 1))
    
    ans = min(dist[n][0][0], dist[n][1][0])
    return ans if ans != INF else -1

# Input parsing
n, m = map(int, input().split())
safety_islands = list(map(int, input().split()))
g, r = map(int, input().split())

# Call the function and output the result
print(min_time_to_cross_road(n, m, safety_islands, g, r))
