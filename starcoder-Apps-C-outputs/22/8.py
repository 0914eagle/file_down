
from collections import defaultdict, deque
from heapq import heapify, heappop, heappush

n, m, h = map(int, input().split())

up = list(map(int, input().split()))

client_data = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    client_data[a].append(b)
    client_data[b].append(a)

q = deque()
q.append(1)

visited = set()
visited.add(1)

while q:
    u = q.popleft()
    for v in client_data[u]:
        if v not in visited:
            q.append(v)
            visited.add(v)

visited = set()

q.append(2)

visited.add(2)

while q:
    u = q.popleft()
    for v in client_data[u]:
        if v not in visited:
            q.append(v)
            visited.add(v)

ans = []

for i in range(n):
    if i + 1 not in visited:
        ans.append(i + 1)

print(len(ans))
print(*ans)
