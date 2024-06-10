
from collections import defaultdict

def solve(n, m, h, u, c):
    adj = defaultdict(list)
    for i in range(m):
        adj[c[i][0]].append(c[i][1])
        adj[c[i][1]].append(c[i][0])
    
    vis = [False] * (n+1)
    queue = []
    queue.append(1)
    vis[1] = True
    while queue:
        curr = queue.pop(0)
        for neigh in adj[curr]:
            if not vis[neigh]:
                vis[neigh] = True
                queue.append(neigh)
    
    for i in range(1, n+1):
        if not vis[i]:
            return 0
    
    min_centers = 0
    for i in range(1, n+1):
        if u[i] == h-1:
            min_centers += 1
    
    return min_centers

n, m, h = map(int, input().split())
u = [0] * (n+1)
u[0] = -1
u = u + list(map(int, input().split()))
c = []
for i in range(m):
    c.append(list(map(int, input().split())))

print(solve(n, m, h, u, c))

