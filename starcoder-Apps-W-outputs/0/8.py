
from collections import defaultdict
n, m = map(int, input().split())
E = list(map(int, input().split()))
graph = defaultdict(list)

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

ans = 0
stack = []
vis = set()
for i in range(n):
    if E[i] == 1:
        if i not in vis:
            ans += 1
            stack.append(i)
            while stack:
                x = stack.pop()
                vis.add(x)
                for e in graph[x]:
                    if e not in vis:
                        stack.append(e)

print(ans)
