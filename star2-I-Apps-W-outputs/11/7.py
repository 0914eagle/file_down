
from collections import defaultdict
from sys import stdin, stdout
from math import factorial

def read_int():
    return int(stdin.readline().strip())

def read_ints():
    return list(map(int, stdin.readline().strip().split()))

def read_str():
    return stdin.readline().strip()

def read_strs():
    return stdin.readline().strip().split()

def dfs(node, parent):
    global cost
    global ways
    global checkposts
    global n
    global m
    global adj
    global dp
    global fact
    global mod
    if dp[node][parent] != -1:
        return dp[node][parent]
    if node == parent:
        dp[node][parent] = 1
        return 1
    dp[node][parent] = 0
    for child in adj[node]:
        if child != parent:
            dp[node][parent] += dfs(child, node)
            dp[node][parent] %= mod
    if dp[node][parent] == 0:
        dp[node][parent] += cost[node]
    return dp[node][parent]

n = read_int()
cost = read_ints()
m = read_int()
adj = defaultdict(list)
for _ in range(m):
    u, v = read_ints()
    adj[u].append(v)
    adj[v].append(u)
dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
ways = 1
for i in range(1, n + 1):
    ways *= dfs(i, i)
    ways %= mod
print(sum(cost), ways)

