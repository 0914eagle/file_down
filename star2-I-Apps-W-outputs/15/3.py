
import sys

def solve(N, X, Y):
    adj = [[] for _ in range(N)]
    for i in range(N-1):
        adj[i].append(i+1)
        adj[i+1].append(i)
    adj[X-1].append(Y-1)
    adj[Y-1].append(X-1)
    
    dist = [[-1] * N for _ in range(N)]
    for i in range(N):
        queue = [i]
        dist[i][i] = 0
        while queue:
            v = queue.pop()
            for u in adj[v]:
                if dist[i][u] == -1:
                    dist[i][u] = dist[i][v] + 1
                    queue.append(u)
    
    for k in range(1, N):
        count = 0
        for i in range(N):
            for j in range(i+1, N):
                if dist[i][j] == k:
                    count += 1
        print(count)

N, X, Y = map(int, input().split())
solve(N, X, Y)

