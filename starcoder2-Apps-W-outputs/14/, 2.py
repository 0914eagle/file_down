
# -*- coding: utf-8 -*-


import sys

n = int(input())

adj = [[] for i in range(n+1)]

for i in range(n-1):
    a, b, z = map(int, sys.stdin.readline().split())
    adj[a].append((b, z))
    adj[b].append((a, z))

order = list(map(int, sys.stdin.readline().split()))

xor = [0] * (n+1)

for i in range(n-1):
    a, b = adj[order[i]][0]
    xor[a] ^= adj[a][0][1]
    xor[b] ^= adj[b][0][1]
    adj[a].pop(0)
    adj[b].pop(0)

ans = [0] * (n+1)

def dfs(u, p, x):
    ans[u] = x
    for v, z in adj[u]:
        if v != p:
            dfs(v, u, x ^ z)

dfs(1, 0, 0)

for i in range(1, n+1):
    print(ans[i])
