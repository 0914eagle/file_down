
from sys import stdin
from collections import defaultdict
input = stdin.readline

n = int(input())
a = list(map(int, input().split()))
adj = defaultdict(list)
for _ in range(n - 1):
    v, u = map(int, input().split())
    adj[v].append(u)
    adj[u].append(v)

def dfs(v, p, color, res):
    if color == 0:
        res[0] += 1
    else:
        res[color] += 1
    for u in adj[v]:
        if u != p:
            dfs(u, v, color, res)

res = [0, 0, 0]
for v in range(1, n + 1):
    if a[v - 1] != 0:
        dfs(v, 0, a[v - 1], res)
        break

print(res[0] * res[1] - (n - 1))

