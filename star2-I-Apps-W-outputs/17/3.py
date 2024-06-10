
import sys
input = sys.stdin.readline

n = int(input())
adj = [[] for _ in range(n)]
for _ in range(n-1):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    adj[u].append(v)
    adj[v].append(u)

def dfs(u, p):
    for v in adj[u]:
        if v == p:
            continue
        dfs(v, u)
        adj[u].append(adj[v][0])

dfs(0, -1)
adj[0].pop()

mex = [0] * n
for i in range(n-1, 0, -1):
    mex[i-1] = mex[i]
    while mex[i-1] in adj[i-1]:
        mex[i-1] += 1

print(*mex[:n-1], sep='\n')

