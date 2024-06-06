
import sys
from collections import defaultdict

input = sys.stdin.readline

n, m = map(int, input().split())
friends = defaultdict(list)

for _ in range(m):
    a, b, c = map(int, input().split())
    friends[a].append((b, c))

def bfs(start, end):
    visited = [False] * n
    queue = [start]
    parent = [0] * n

    while queue:
        s = queue.pop(0)
        visited[s] = True
        for neighbor, weight in friends[s]:
            if not visited[neighbor]:
                queue.append(neighbor)
                parent[neighbor] = s
                if neighbor == end:
                    return weight
    return -1

while True:
    found = False
    for i in range(n):
        for j in range(n):
            if i != j:
                cycle_weight = bfs(i, j)
                if cycle_weight != -1:
                    found = True
                    friends[i].remove((j, cycle_weight))
                    friends[j].remove((i, cycle_weight))
    if not found:
        break

total = 0
for friend in friends:
    total += len(friends[friend])
print(total)
for friend in friends:
    for f in friends[friend]:
        print(f"{friend} {f[0]} {f[1]}")

