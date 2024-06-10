
from sys import stdin
from collections import defaultdict
from itertools import combinations
from functools import reduce

MOD = 10**9+7

def dfs(G, v, path=None):
    if path is None: path = []
    path += [v]
    for w in G[v]:
        if w in path:
            return path[path.index(w):]
        else:
            newpath = dfs(G, w, path)
            if newpath:
                return newpath
    return None

def is_confusing(G):
    for v in G:
        path = dfs(G, v)
        if path:
            return True
    return False

n = int(stdin.readline())
a = [int(x) for x in stdin.readline().split()]
G = defaultdict(list)
for i, v in enumerate(a, 1):
    G[i].append(v)

ans = 0
for i in range(1, n+1):
    for comb in combinations(range(1, n+1), i):
        for v in comb:
            G[v] = [a[v-1]]
        if not is_confusing(G):
            ans += 1
        for v in comb:
            G[v] = [v]

print(ans % MOD)

