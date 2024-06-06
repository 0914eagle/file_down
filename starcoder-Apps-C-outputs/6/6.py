
import sys
from collections import defaultdict
n = int(sys.stdin.readline())
dp = [10**6 for _ in range(n+1)]
dp[0] = 0
graph = defaultdict(set)
for _ in range(n):
    p = int(sys.stdin.readline())
    for _ in range(p):
        line = sys.stdin.readline().split()
        l, k = int(line[0]), int(line[1])
        for i in line[2:]:
            graph[int(i)].add(_)
        dp[_] = min(dp[_], l)
def dfs(v):
    for i in graph[v]:
        dp[i] = min(dp[i], dp[v] + dp[i])
        dfs(i)
dfs(0)
print(dp[0])
