
from collections import defaultdict
n, m = map(int, input().split())

friends = [set() for _ in range(n)]
ious = []

for _ in range(m):
    a, b, c = map(int, input().split())
    friends[a].add(b)
    friends[b].add(a)
    ious.append((a, b, c))

def dfs(x, y, ious, visited):
    if x == y:
        return ious
    visited[x] = True
    for i in range(len(ious)):
        if not visited[ious[i][0]]:
            ious[i] = (ious[i][0], ious[i][1], ious[i][2] - min(ious[i][2], dfs(ious[i][0], y, ious, visited)))
        elif ious[i][1] == y:
            ious[i] = (ious[i][0], ious[i][1], 0)
    return ious

for i in range(n):
    if len(friends[i]) == 0:
        continue
    for j in range(len(ious)):
        if not ious[j][0] == i:
            continue
        ious = dfs(i, ious[j][1], ious, [False for _ in range(n)])

res = 0
for i in range(len(ious)):
    if ious[i][2] > 0:
        res += 1

print(res)
for i in range(len(ious)):
    if ious[i][2] > 0:
        print(ious[i][0], ious[i][1], ious[i][2])
