
from collections import defaultdict
from heapq import *
n = int(input())
a = list(map(int, input().split()))
tree = defaultdict(list)
ans = 0
for i in range(n):
    x, *y = map(int, input().split())
    for j in y:
        tree[j].append(i)
dist = [0 for i in range(n)]
heap = [(0,0)]
while heap:
    w,u = heappop(heap)
    ans = max(ans,w)
    for v in tree[u]:
        dist[v] = max(dist[v],w)
        heappush(heap,(dist[v]+a[v],v))
print(ans)
