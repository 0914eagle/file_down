
# -*- coding: utf-8 -*-


import sys

sys.setrecursionlimit(10**6)

n = int(input())

graph = [[] for _ in range(n)]

for _ in range(n - 1):
    a, b, z = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((b, z))
    graph[b].append((a, z))

order = list(map(int, input().split()))

def dfs(v, p, xor):
    ans = 0
    if xor == 0:
        ans += 1
    for to, z in graph[v]:
        if to == p:
            continue
        ans += dfs(to, v, xor ^ z)
    return ans

ans = [0] * n

for i in range(n - 1):
    ans[i + 1] = ans[i]
    a, b, z = graph[order[i]]
    ans[i + 1] += dfs(a, b, z)

print(*ans, sep='\n')
